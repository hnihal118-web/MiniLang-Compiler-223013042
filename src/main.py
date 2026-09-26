from lexer import Lexer
from parser import Parser
from semantic import SemanticAnalyzer
from tac import TACGenerator
from optimizer import Optimizer
from backend import Backend


def compile_program(source_code):

    # Step 1: Lexical Analysis
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()

    print("=== TOKENS ===")
    for token in tokens:
        print(token)

    # Step 2: Parsing
    parser = Parser(tokens)
    ast = parser.parse()

    print("\n=== AST CREATED ===")

    # Step 3: Semantic Analysis
    semantic = SemanticAnalyzer()
    semantic.analyze(ast)

    print("Semantic analysis successful")

    # Step 4: TAC Generation
    tac_generator = TACGenerator()

    tac = tac_generator.generate(ast)

    print("\n=== TAC ===")

    for instruction in tac:
        print(instruction)

    # Step 5: Optimization
    optimizer = Optimizer()

    optimized = optimizer.optimize(tac)

    print("\n=== OPTIMIZED TAC ===")

    for instruction in optimized:
        print(instruction)

    # Step 6: Backend Execution
    backend = Backend()

    result = backend.run(optimized)

    print("\n=== VARIABLES ===")
    print(result)

    return result


if __name__ == "__main__":

    example = """

    purno2 x = 10;
    purno2 y = 20;

    """

    compile_program(example)
