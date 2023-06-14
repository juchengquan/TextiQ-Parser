import sys
sys.path.insert(0, './')

from src.regex import preprocess
from src.lexer import TextiQLexer
from src.parser import TextiQParser

lexer = TextiQLexer()
parser = TextiQParser()

if __name__ == "__main__":
    text_pre = "-what & ( not is | 'not' the meaning ) or of and (word1 | word3) or (stonehenge) and (fox say)~3"
    text = preprocess(text_pre)
    
    token = lexer.tokenize(text)
    for e in token:
        print('type=%r, value=%r' % (e.type, e.value))
        
    res = parser.parse(lexer.tokenize(text))
    print(res)
