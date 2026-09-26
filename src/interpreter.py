class StackInterpreter:

    def __init__(self):
        self.stack = []
        self.variables = {}

    def run(self, instructions):
        """
        Execute stack-machine instructions.
        """
        for instruction in instructions:
            # Implement PUSH, LOAD, STORE,
            # arithmetic, CALL and RETURN.
            pass
