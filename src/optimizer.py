from tac import TACInstruction


class Optimizer:
    def __init__(self):
        pass

    # -----------------------------
    # Constant Folding
    # -----------------------------
    def constant_folding(self, instructions):
        optimized = []

        for instruction in instructions:

            if (
                instruction.arg1 is not None
                and instruction.arg2 is not None
                and instruction.op in {"ADD", "SUB", "MUL", "DIV"}
            ):
                try:
                    a = float(instruction.arg1)
                    b = float(instruction.arg2)

                    if instruction.op == "ADD":
                        value = a + b

                    elif instruction.op == "SUB":
                        value = a - b

                    elif instruction.op == "MUL":
                        value = a * b

                    elif instruction.op == "DIV":
                        if b == 0:
                            optimized.append(instruction)
                            continue

                        value = a / b

                    # Convert 5.0 to 5
                    if value.is_integer():
                        value = int(value)

                    new_instruction = TACInstruction(
                        "ASSIGN",
                        arg1=str(value),
                        result=instruction.result
                    )

                    optimized.append(new_instruction)

                except (ValueError, TypeError):
                    optimized.append(instruction)

            else:
                optimized.append(instruction)

        return optimized

    # -----------------------------
    # Dead Code Elimination
    # -----------------------------
    def dead_code_elimination(self, instructions):
        optimized = []

        for i, instruction in enumerate(instructions):

            if instruction.op != "ASSIGN":
                optimized.append(instruction)
                continue

            result = instruction.result

            used_later = False

            for next_instruction in instructions[i + 1:]:

                if (
                    next_instruction.arg1 == result
                    or next_instruction.arg2 == result
                ):
                    used_later = True
                    break

            # Keep final assignments to variables
            if used_later or not result:
                optimized.append(instruction)

            elif not str(result).startswith("t"):
                optimized.append(instruction)

        return optimized

    # -----------------------------
    # Run all optimizations
    # -----------------------------
    def optimize(self, instructions):
        instructions = self.constant_folding(instructions)

        instructions = self.dead_code_elimination(
            instructions
        )

        return instructions
