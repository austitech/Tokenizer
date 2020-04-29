

tokentype = {
    'INT': 'INT',
    'FLOAT': 'FLOAT',
    'STRING': 'STRING',
    'CHAR': 'CHAR',

    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'MUL',
    '/': 'DIV',
    '=': 'ASSIGN',
    '%': 'MODULO',
    ':': 'COLON',
    ';': 'SEMICOLON',
    '<': 'LT',
    '>': 'GT',
    '[': 'O_BRACKET',
    ']': 'C_BRACKET',
    '(': 'O_PAREN',
    ')': 'C_PAREN',
    '{': 'O_BRACE',
    '}': 'C_BRACE',
    '&': 'AND',
    '|': 'OR',
    '!': 'NOT',
    '^': 'EXPO',

    'ID': 'ID',
    'EOF': 'EOF'
}


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'<{self.type}: {self.value}>'

    __repr__ = __str__
