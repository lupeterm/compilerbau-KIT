from enum import Enum, auto


class Token_Type(Enum):
    T_PLUS = auto()
    T_MINUS = auto()
    T_STAR = auto()
    T_SLASH = auto()
    T_LPAREN = auto()
    T_RPAREN = auto()
    T_NUMBER = auto()
    T_EOF = auto()


class T_Position:
    def __init__(self) -> None:
        self.line = 1
        self.column = 1


class Token:
    def __init__(self) -> None:
        self.type: Token_Type
        self.position = T_Position()
        self.value: float

    def __repr__(self) -> str:
        return f'{self.type.name}'
