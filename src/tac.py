class TACInstruction:
    def __init__(self, op, arg1=None, arg2=None, result=None):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def __str__(self):
        return (
            f"{self.result} = {self.arg1} {self.op} {self.arg2}"
            if self.arg2 is not None
            else f"{self.result} = {self.arg1}"
        )


class TACGenerator:
    def __init__(self):
        self.instructions = []
        self.temp_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def generate(self, ast):
        # Traverse AST and generate three-address code.
        pass
