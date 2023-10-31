import ply.yacc as yacc
from src.models.Lexer import MyLexer


class MyParser:

    # CONSTRUCTOR
    def __init__(self, lexer):
        print("Parser constructor called")
        self.parser = yacc.yacc(module=self)
        self.lexer = lexer

    # DESTRUCTOR
    def __del__(self):
        print('Parser destructor called.')

    tokens = MyLexer.tokens

    # GRAMMAR START
    def p_type_assignment(self, p):
        'type_assignment : VAR ID COLON ENTERO SEMICOLON'
        print("PARSER: expression recognized", p)

    # def p_function_header(self,p):
    #     'function_header : FUN ID LPAREN RPAREN DEV LPAREN RPAREN'
    #
    #     print('PARSER: fun header recognized', p)

    def p_error(self,p):
        if p:
            print("Syntax error at token", p)

    def build(self,**kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)

    def test(self, data):
        result = self.parser.parse(data)
        print(result)
#TYPES = t_ENTERO + r'|' + t_BOOLEANO
#t_TYPE_ASSIGNMENT = t_VAR + ID + t_EQ + t_ENTERO + t_SEMICOLON
