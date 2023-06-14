from sly import Parser
from .lexer import TextiQLexer

class TextiQParser(Parser):
    tokens = TextiQLexer.tokens

    precedence = (
        ('left', OR),
        ('left', AND),
        ('right', NOT),
        ('right', UMINUS),
        ('nonassoc', RANGE),
    )

    @_('expr')
    def statement(self, p):
        print(p.expr)

    @_('expr OR expr')
    @_('expr AND expr')
    def expr(self, p):
        return [p[1], p.expr0, p[2]]
    
    @_('expr RANGE NUMBER')
    def expr(self, p):
        # return [p[1], p.expr, p[2]]
        return [p[1], p.expr.split(" "), p[2]]
        # return [p[2], p.expr0, p.expr1, p[3]]

    @_('"-" expr %prec UMINUS')
    @_('NOT expr')
    def expr(self, p):
        return [p[0], p.expr]

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    @_('NAME')
    def expr(self, p):
        return p[0]