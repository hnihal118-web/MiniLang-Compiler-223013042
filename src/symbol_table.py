class Symbol:
    def __init__(self, name, symbol_type, kind="variable"):
        self.name = name
        self.symbol_type = symbol_type
        self.kind = kind


class Scope:
    def __init__(self, parent=None):
        self.parent = parent
        self.symbols = {}

    def define(self, symbol):
        if symbol.name in self.symbols:
            raise Exception(f"Duplicate declaration: {symbol.name}")
        self.symbols[symbol.name] = symbol

    def lookup(self, name):
        if name in self.symbols:
            return self.symbols[name]

        if self.parent is not None:
            return self.parent.lookup(name)

        return None
