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
        'type_assignment : VAR ID COLON type SEMICOLON'
        print("PARSER: se encontró una asignacion de tipo", p)

    def p_type(self,p):
        '''
        type : ENTERO
        | BOOLEANO
        | DECIMAL
        | CADENA
        | ARREGLO
        '''
        print('PARSER: Se encontró un tipo', p)

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
