# MiniLang Compiler

Roll Number: 223013042

Variant: 2

## Variant Features

- Structs / Records
- Nested Functions
- Static Scoping

## Compiler Components

- Hand-written DFA Lexer
- Recursive Descent Parser
- Abstract Syntax Tree
- Symbol Table
- Semantic Analysis
- Three Address Code
- Constant Folding
- Dead Code Elimination
- Stack Machine Backend
- Interpreter

## Project Structure

See the src, tests and examples directories.

## Running

```bash
python src/main.py examples/struct_example.ml
