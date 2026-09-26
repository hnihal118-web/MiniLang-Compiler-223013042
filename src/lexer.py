KEYWORDS = {
    "fun2": "FUNCTION",
    "back2": "RETURN",
    "gothon2": "STRUCT",
    "purno2": "INT",
    "dosomik2": "FLOAT",
    "shotto2": "BOOL",
    "jodi2": "IF",
    "nahole2": "ELSE",
    "jotokhon2": "WHILE",
}


class Token:
    def __init__(self, token_type, value, line, column):
        self.token_type = token_type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return (
            f"Token({self.token_type}, "
            f"{self.value!r}, "
            f"{self.line}:{self.column})"
        )


class LexerError(Exception):
    pass


class Lexer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1

    def advance(self):
        ch = self.source[self.position]
        self.position += 1

        if ch == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1

        return ch

    def peek(self):
        if self.position >= len(self.source):
            return "\0"
        return self.source[self.position]

    def skip_whitespace(self):
        while self.peek() in " \t\r\n":
            self.advance()

    def read_identifier(self):
        start_line = self.line
        start_column = self.column
        value = ""

        while self.peek().isalnum() or self.peek() == "_":
            value += self.advance()

        token_type = KEYWORDS.get(value, "IDENTIFIER")

        return Token(
            token_type,
            value,
            start_line,
            start_column
        )

    def read_number(self):
        start_line = self.line
        start_column = self.column
        value = ""

        while self.peek().isdigit():
            value += self.advance()

        if self.peek() == ".":
            value += self.advance()

            if not self.peek().isdigit():
                raise LexerError(
                    f"Invalid number at "
                    f"{self.line}:{self.column}"
                )

            while self.peek().isdigit():
                value += self.advance()

            token_type = "FLOAT_LITERAL"
        else:
            token_type = "INT_LITERAL"

        return Token(
            token_type,
            value,
            start_line,
            start_column
        )

    def tokenize(self):
        tokens = []

        single_char_tokens = {
            "+": "PLUS",
            "-": "MINUS",
            "*": "STAR",
            "/": "SLASH",
            "=": "ASSIGN",
            ";": "SEMICOLON",
            ",": "COMMA",
            ".": "DOT",
            "(": "LPAREN",
            ")": "RPAREN",
            "{": "LBRACE",
            "}": "RBRACE",
        }

        while self.position < len(self.source):

            self.skip_whitespace()

            if self.position >= len(self.source):
                break

            line = self.line
            column = self.column
            ch = self.peek()

            if ch.isalpha() or ch == "_":
                tokens.append(self.read_identifier())
                continue

            if ch.isdigit():
                tokens.append(self.read_number())
                continue

            if ch in single_char_tokens:
                self.advance()

                tokens.append(
                    Token(
                        single_char_tokens[ch],
                        ch,
                        line,
                        column
                    )
                )
                continue

            raise LexerError(
                f"Invalid character {ch!r} "
                f"at line {line}, column {column}"
            )

        tokens.append(
            Token(
                "EOF",
                "",
                self.line,
                self.column
            )
        )

        return tokens
