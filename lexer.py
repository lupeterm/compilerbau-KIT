from pathlib import Path
from myToken import Token, Token_Type
import sys
from copy import copy


class Lexer:
    def __init__(self, file: Path) -> None:
        with file.open() as f:
            self.stream = f.readlines()
        print(f'Reading: {self.stream[0]}\n')
        self.token = Token()
        self.line = 1
        self.column = 0
        self.next_char()
        self.tokens: list[Token] = []

    def add_token(self):
        self.tokens.append(copy(self.token))

    def next_char(self):
        if self.column >= len(self.stream[self.line - 1]):
            if self.line >= len(self.stream):
                self.c = 'EOF'
                return
            self.c = '\n'
            return
        self.c = self.stream[self.line - 1][self.column]
        self.column += 1

    def error(self):
        if self.c == 'EOF':
            print(f'Unexpected end of input at {self.line}, {self.column}')
        else:
            print(f'"Unexpected character {self.c} at {self.line}, {self.column}')
        sys.exit()

    def lex_float(self):
        end = self.column - 1
        float_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
        while end != len(self.stream[self.line - 1]) and (self.stream[self.line - 1][end] in float_chars):
            end += 1
        try:
            num = float(''.join(self.stream[self.line - 1][self.column - 1:end]))
            self.column = end
            self.token.type = Token_Type.T_NUMBER
            self.token.value = num
            self.next_char()
        except ValueError as e:
            print(e)
            self.error()

    def next_token(self):
        self.token.position.line = self.line
        self.token.position.column = self.column

        if self.c == '+':
            self.next_char()
            self.token.type = Token_Type.T_PLUS
            return
        elif self.c == '-':
            self.next_char()
            self.token.type = Token_Type.T_MINUS
            return
        elif self.c == '*':
            self.next_char()
            self.token.type = Token_Type.T_STAR
            return
        elif self.c == '/':
            self.next_char()
            self.token.type = Token_Type.T_SLASH
            return
        elif self.c == '(':
            self.next_char()
            self.token.type = Token_Type.T_LPAREN
            return
        elif self.c == ')':
            self.next_char()
            self.token.type = Token_Type.T_RPAREN
            return
        elif self.c == 'EOF':
            self.token.type = Token_Type.T_EOF
            return
        elif self.c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
            self.lex_float()
            return
        elif self.c == '\n':
            self.line += 1
            self.column = 0
        elif self.c == ' ' or self.c == '\t' or self.c == '\r':
            self.next_char()
            self.next_token()
        else:
            self.error()
            self.next_token()
