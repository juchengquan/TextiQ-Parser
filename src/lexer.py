from sly import Lexer

class TextiQLexer(Lexer):
    tokens = { NAME, NUMBER, OPERATOR, AND, OR, NOT, RANGE}
    ignore = ' \t'
    literals = {"(", ")"}

    # Keyword tokens (and identifiers)
    NAME = r"[\w\d][\w\d\s]*[\w\d]"
    NAME["or"]=OR
    
    OPERATOR = r"[\&\-\|\~]"
    OPERATOR['&'] = AND
    OPERATOR['-'] = NOT
    OPERATOR['|'] = OR
    OPERATOR['~'] = RANGE

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        raise ValueError(f'Illegal character {t.value[0]!r} at index {self.index}', t.value, self.index)
        self.index += 1