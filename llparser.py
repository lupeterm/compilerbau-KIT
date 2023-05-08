from myToken import Token, Token_Type
from expression import Expression, MultOP, MinOP, AddOP, DivOP, NUM


def p(e):
    e.print()
    print('\n\n')


class LLParser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self._current = 0
        self.t = self.tokens[self._current]

    def parse(self):
        return self.parseE()

    def next_token(self):
        self._current += 1
        if self._current >= len(self.tokens):
            print('reached end of tokens')
            return self
        self.t = self.tokens[self._current]

    def parseE(self):
        expr = self.parseT()
        e = self.parseE_(expr)
        return e

    def parseT(self):
        expr = self.parseF()
        e = self.parseT_(expr)
        return e

    def parseT_(self, expr: Expression):
        if self.t.type == Token_Type.T_STAR:
            self.next_token()
            right = self.parseF()
            expr = MultOP(expr, right)
            return self.parseT_(expr)
        elif self.t.type == Token_Type.T_SLASH:
            self.next_token()
            right = self.parseF()
            expr = DivOP(expr, right)
            return self.parseT_(expr)
        else:
            return expr

    def parseE_(self, expr: Expression):
        if self.t.type == Token_Type.T_PLUS:
            self.next_token()
            right = self.parseT()
            expr = AddOP(expr, right)
            return self.parseE_(expr)
        elif self.t.type == Token_Type.T_MINUS:
            self.next_token()
            right = self.parseT()
            expr = MinOP(expr, right)
            return self.parseE_(expr)
        else:
            return expr

    def parseF(self):
        if self.t.type == Token_Type.T_LPAREN:
            self.next_token()
            expr = self.parseE()
            if self.t.type == Token_Type.T_RPAREN:
                self.next_token()
            else:
                print('missing RParen')
            return expr
        elif self.t.type == Token_Type.T_NUMBER:
            expr = NUM(self.t.value)
            self.next_token()
            return expr
        else:
            print(f'parser error in parseF for {self.t}')
            exit()
