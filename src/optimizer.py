class Optimizer:

    def constant_folding(self, instructions):
        """
        Example:
        t1 = 10 + 20

        becomes:
        t1 = 30
        """
        pass

    def dead_code_elimination(self, instructions):
        """
        Remove instructions whose results are never used.
        """
        pass

    def optimize(self, instructions):
        instructions = self.constant_folding(instructions)
        instructions = self.dead_code_elimination(instructions)
        return instructions
