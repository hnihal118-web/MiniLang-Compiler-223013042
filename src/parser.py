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

    def parse(self):
        """
        Recursive-descent parser.

        Grammar must support:
        - program
        - struct declarations
        - function declarations
        - nested functions
        - variable declarations
        - expressions
        - blocks
        """
        pass
