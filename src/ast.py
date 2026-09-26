class ASTNode:
    pass


class Program(ASTNode):
    def __init__(self, declarations):
        self.declarations = declarations


class StructDecl(ASTNode):
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields


class FunctionDecl(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body


class VariableDecl(ASTNode):
    def __init__(self, name, type_name, initializer=None):
        self.name = name
        self.type_name = type_name
        self.initializer = initializer


class Block(ASTNode):
    def __init__(self, statements):
        self.statements = statements
