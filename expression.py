class Expression:
    def __init__(self) -> None:
        self.left = None
        self.right = None

    def print(self, d=0):
        indent = "\t" * d
        if not isinstance(self, NUM):
            if self.left:
                self.left.print(d + 2)
        if isinstance(self, NUM):
            print(f'{indent}{self.value}')
        else:
            print(f'{indent}{self.__class__.__name__}({self.calc()})')
        if not isinstance(self, NUM):
            if self.right:
                self.right.print(d + 2)


class MultOP(Expression):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def calc(self):
        return self.left.calc() * self.right.calc()

class AddOP(Expression):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def calc(self):
        return self.left.calc() + self.right.calc()

class DivOP(Expression):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def calc(self):
        return self.left.calc() / self.right.calc()

class MinOP(Expression):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def calc(self):
        return self.left.calc() - self.right.calc()

class NUM(Expression):
    def __init__(self, value) -> None:
        self.value = value

    def calc(self):
        return self.value
