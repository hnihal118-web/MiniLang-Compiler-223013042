# MiniLang Hand-Written Lexer
# Roll: 223013042
# Variant: 2

class Token:
    def __init__(self, token_type, value, line, column):
        self.token_type = token_type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.token_type}, {self.value}, {self.line}:{self.column})"


class Lexer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1

    def tokenize(self):
        """
        Implement the DFA-based scanning logic here.

        Required:
        - identifiers
        - integer/float numbers
        - operators
        - punctuation
        - keywords
        - whitespace
        - line/column tracking
        - invalid-character errors
        """
        pass
