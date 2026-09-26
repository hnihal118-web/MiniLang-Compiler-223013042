from symbol_table import SymbolTable, Symbol


class SemanticError(Exception):
    pass


class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.structs = {}

    def analyze(self, ast):
        for declaration in ast.declarations:
            self.visit(declaration)

    def visit(self, node):
        if isinstance(node, type(None)):
            return

        method_name = "visit_" + node.__class__.__name__

        method = getattr(
            self,
            method_name,
            self.generic_visit
        )

        return method(node)

    def generic_visit(self, node):
        return None

    def visit_Program(self, node):
        for declaration in node.declarations:
            self.visit(declaration)

    def visit_StructDecl(self, node):
        if node.name in self.structs:
            raise SemanticError(
                f"Duplicate struct: {node.name}"
            )

        fields = {}

        for field_name, field_type in node.fields:
            if field_name in fields:
                raise SemanticError(
                    f"Duplicate field: {field_name}"
                )

            fields[field_name] = field_type

        self.structs[node.name] = fields

        self.symbol_table.define(
            node.name,
            node.name,
            kind="struct"
        )

    def visit_FunctionDecl(self, node):
        if self.symbol_table.lookup(node.name):
            raise SemanticError(
                f"Duplicate function: {node.name}"
            )

        self.symbol_table.define(
            node.name,
            "function",
            kind="function"
        )

        self.symbol_table.enter_scope()

        for param_name, param_type in node.params:
            self.symbol_table.define(
                param_name,
                param_type,
                kind="parameter"
            )

        self.visit(node.body)

        self.symbol_table.exit_scope()

    def visit_VariableDecl(self, node):
        if node.type_name not in (
            "purno2",
            "dosomik2",
            "shotto2"
        ):
            if node.type_name not in self.structs:
                raise SemanticError(
                    f"Unknown type: {node.type_name}"
                )

        if self.symbol_table.lookup(node.name):
            # Allow shadowing only if the name exists
            # in an outer scope.
            current = self.symbol_table.current_scope

            if node.name in current.symbols:
                raise SemanticError(
                    f"Duplicate declaration: {node.name}"
                )

        self.symbol_table.define(
            node.name,
            node.type_name,
            kind="variable"
        )

    def visit_Block(self, node):
        self.symbol_table.enter_scope()

        for statement in node.statements:
            self.visit(statement)

        self.symbol_table.exit_scope()
