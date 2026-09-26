import sys

from lexer import Lexer
from parser import Parser
from semantic import SemanticAnalyzer
from tac import TACGenerator
from optimizer import Optimizer
from backend import StackBackend
from interpreter import StackInterpreter


def compile_and_run(source):
    # 1. Lexical analysis
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    # 2. Parsing
    parser = Parser(tokens)
    ast = parser.parse()

    # 3. Semantic analysis
    analyzer = SemanticAnalyzer()
    analyzer.analyze(ast)

    # 4. TAC generation
    generator = TACGenerator()
    tac = generator.generate(ast)

    # 5. Optimization
    optimizer = Optimizer()
    optimized = optimizer.optimize(tac)

    # 6. Backend
    backend = StackBackend()
    machine_code = backend.generate(optimized)

    # 7. Execution
    interpreter = StackInterpreter()
    return interpreter.run(machine_code)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python src/main.py <source-file>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as file:
        source = file.read()

    compile_and_run(source)
