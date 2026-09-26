class SemanticError(Exception):
    pass


class SemanticAnalyzer:
    def __init__(self):
        self.current_scope = None

    def enter_scope(self):
        # Create a new scope whose parent is current_scope.
        pass

    def exit_scope(self):
        # Return to the enclosing scope.
        pass

    def analyze(self, ast):
        # Traverse AST and perform semantic checks.
        pass
