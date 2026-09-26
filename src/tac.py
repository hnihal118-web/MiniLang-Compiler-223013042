class TACInstruction:
    def __init__(self, op, arg1=None, arg2=None, result=None):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def __str__(self):
        if self.op == "ASSIGN":
            return f"{self.result} = {self.arg1}"

        if self.op == "RETURN":
            return f"RETURN {self.arg1}"

        if self.arg2 is not None:
            return (
                f"{self.result} = "
                f"{self.arg1} {self.op} {self.arg2}"
            )

        return f"{self.op} {self.arg1}"


class TACGenerator:
    def __init__(self):
        self.instructions = []
        self.temp_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def emit(
        self,
        op,
        arg1=None,
        arg2=None,
        result=None
    ):
        instruction = TACInstruction(
            op,
            arg1,
            arg2,
            result
        )

        self.instructions.append(instruction)

        return instruction

    def generate(self, ast):
        self.instructions = []
        self.temp_count = 0

        for declaration in ast.declarations:
            self.visit(declaration)

        return self.instructions

    def visit(self, node):
        method_name = (
            "visit_" +
            node.__class__.__name__
        )

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

    def visit_VariableDecl(self, node):
        if node.initializer is not None:
            self.emit(
                "ASSIGN",
                arg1=node.initializer,
                result=node.name
            )

    def visit_Block(self, node):
        for statement in node.statements:
            self.visit(statement)

    def visit_FunctionDecl(self, node):
        self.emit(
            "FUNCTION",
            arg1=node.name
        )

        self.visit(node.body)

        self.emit(
            "END_FUNCTION",
            arg1=node.name
        )

    def visit_StructDecl(self, node):
        self.emit(
            "STRUCT",
            arg1=node.name
        )
