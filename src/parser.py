from ast import (
    Program,
    StructDecl,
    FunctionDecl,
    VariableDecl,
    Block
)


class ParserError(Exception):
    pass


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def advance(self):
        token = self.current()
        self.position += 1
        return token

    def expect(self, token_type):
        token = self.current()

        if token is None or token.token_type != token_type:
            actual = "EOF" if token is None else token.token_type
            raise ParserError(
                f"Expected {token_type}, got {actual}"
            )

        return self.advance()

    def parse(self):
        declarations = []

        while self.current() is not None:
            if self.current().token_type == "EOF":
                break

            declarations.append(self.parse_declaration())

        return Program(declarations)

    def parse_declaration(self):
        token = self.current()

        if token.token_type == "STRUCT":
            return self.parse_struct()

        if token.token_type == "FUNCTION":
            return self.parse_function()

        if token.token_type in ("INT", "FLOAT", "BOOL"):
            return self.parse_variable()

        raise ParserError(
            f"Unexpected token {token.value!r} "
            f"at {token.line}:{token.column}"
        )

    def parse_struct(self):
        self.expect("STRUCT")

        name = self.expect("IDENTIFIER").value

        self.expect("LBRACE")

        fields = []

        while self.current().token_type != "RBRACE":
            field_type = self.advance().value
            field_name = self.expect("IDENTIFIER").value

            self.expect("SEMICOLON")

            fields.append(
                (field_name, field_type)
            )

        self.expect("RBRACE")

        return StructDecl(name, fields)

    def parse_function(self):
        self.expect("FUNCTION")

        name = self.expect("IDENTIFIER").value

        self.expect("LPAREN")

        params = []

        if self.current().token_type != "RPAREN":
            while True:
                type_token = self.advance()
                param_name = self.expect("IDENTIFIER").value

                params.append(
                    (param_name, type_token.value)
                )

                if self.current().token_type != "COMMA":
                    break

                self.advance()

        self.expect("RPAREN")

        body = self.parse_block()

        return FunctionDecl(
            name,
            params,
            body
        )

    def parse_variable(self):
        type_token = self.advance()

        name = self.expect("IDENTIFIER").value

        initializer = None

        if self.current().token_type == "ASSIGN":
            self.advance()

            initializer = self.advance().value

        self.expect("SEMICOLON")

        return VariableDecl(
            name,
            type_token.value,
            initializer
        )

    def parse_block(self):
        self.expect("LBRACE")

        statements = []

        while self.current().token_type != "RBRACE":
            if self.current().token_type == "FUNCTION":
                statements.append(self.parse_function())

            elif self.current().token_type in (
                "INT",
                "FLOAT",
                "BOOL"
            ):
                statements.append(
                    self.parse_variable()
                )

            else:
                self.advance()

        self.expect("RBRACE")

        return Block(statements)
