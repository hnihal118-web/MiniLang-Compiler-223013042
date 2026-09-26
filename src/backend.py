class Backend:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def run(self, instructions):
        self.variables = {}
        self.functions = {}

        # First collect functions
        for instruction in instructions:
            if instruction.op == "FUNCTION":
                self.functions[instruction.arg1] = True

        # Execute instructions
        for instruction in instructions:
            self.execute(instruction)

        return self.variables

    def execute(self, instruction):

        # Assignment
        if instruction.op == "ASSIGN":
            value = self.get_value(instruction.arg1)
            self.variables[instruction.result] = value

        # Arithmetic operations
        elif instruction.op in {"ADD", "SUB", "MUL", "DIV"}:
            left = self.get_value(instruction.arg1)
            right = self.get_value(instruction.arg2)

            if instruction.op == "ADD":
                result = left + right

            elif instruction.op == "SUB":
                result = left - right

            elif instruction.op == "MUL":
                result = left * right

            elif instruction.op == "DIV":
                if right == 0:
                    raise RuntimeError("Division by zero")
                result = left / right

            self.variables[instruction.result] = result

        # Return
        elif instruction.op == "RETURN":
            return self.get_value(instruction.arg1)

        # Function declaration
        elif instruction.op == "FUNCTION":
            return

        elif instruction.op == "END_FUNCTION":
            return

        # Struct declaration
        elif instruction.op == "STRUCT":
            return

    def get_value(self, value):

        if value is None:
            return None

        # Variable lookup
        if value in self.variables:
            return self.variables[value]

        # Integer
        try:
            return int(value)
        except (ValueError, TypeError):
            pass

        # Float
        try:
            return float(value)
        except (ValueError, TypeError):
            pass

        # Boolean
        if value == "true":
            return True

        if value == "false":
            return False

        # String / unknown value
        return value
