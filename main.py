from lexer import Lexer
from llparser import LLParser
from pathlib import Path
from myToken import Token_Type, Token


def lexing(p: Path):
    lexer = Lexer(p)
    lexer.next_token()
    lexer.add_token()

    while lexer.token.type != Token_Type.T_EOF:
        lexer.next_token()
        lexer.add_token()

    print(f'\nTokens: {lexer.tokens}\n')
    return lexer.tokens


def ll1_parsing(tokens: list[Token]):
    parser = LLParser(tokens)
    return parser.parse()


def main(p: Path):
    tokens = lexing(p)
    ast = ll1_parsing(tokens)
    print('\nParsed AST: \n')
    ast.print()
    print(f'\nResult: {ast.calc()}\n')


if __name__ == '__main__':
    p = Path('input.txt')
    main(p)
