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

    precedence = ( # Aca va la precedencia de tokens
        ('nonassoc', 'MENOR', 'MAYOR'),  # Nonassociative
        ('left', 'SUMA', 'RESTA'),
        ('left', 'MULT', 'DIV'),
        #('right', 'UMINUS'),  # Unary minus operator
    )
    # GRAMMAR START

    def p_algoritmo(self,p):
        # algoritmo regex inicial para reconocer el resto puede ser cualquier cantidad de funciones o ninguna pero si o si una o mas proposiciones
        # la idea es poder llamar esa funcion por fuera para hacer un salto
        # algoritmo ::= fun_senten* proposicion+
        '''
        algoritmo : fun_sentencias proposicion proposiciones
        | proposicion proposiciones
        fun_sentencias : fun_senten fun_sentencias
        | fun_senten
        '''

    def p_proposiciones(self,p):
        # proposiciones ::= proposicion*
        '''
        proposiciones : proposicion proposiciones
        | empty
        '''

    def p_proposicion(self,p):
        # proposicion ::= DEV expresion | si_senten | mientras_senten | asignacion PCOMA
        '''
        proposicion : DEV expresion
        | asignacion PCOMA
        | inicializar_variable PCOMA
        '''

    def p_sec_proposiciones(self,p):
        # sec_proposiciones ::= proposicion+
        '''
        sec_proposiciones : proposicion sec_proposiciones
        | proposicion
        '''

    def p_asignacion(self,p):
        # asignacion ::= ID ASIGNAR expresion
        '''
        asignacion : ID ASIGNAR expresion
        '''


    def p_suma_resta(self,p):
        # suma_resta ::= SUMA | RESTA
        '''
        suma_resta : SUMA
        | RESTA
        '''

    def p_operador_relacional(self,p):
        # operador_relacional ::= IGUAL | DIFERENTE | LEQ | GEQ | MENOR | MAYOR
        '''
        operador_relacional : IGUAL
        | DIFERENTE
        | LEQ
        | GEQ
        | MENOR
        | MAYOR
        '''

    def p_tipos(self,p):
        # tipos ::= ENTERO | BOOLEANO | DECIMAL | CADENA
        '''
        tipos : ENTERO
        | BOOLEANO
        | DECIMAL
        | CADENA
        '''
        print('PARSER: Se encontró un tipo', p)

    def p_operador_terminal(self,p):
        # operador_terminal ::= (operaciones factor)*
        # operaciones ::= MULT | DIV | MOD | Y | O
        '''
        operador_terminal : operaciones factor operador_terminal
        | empty
        operaciones : MULT
        | DIV
        | MOD
        | Y
        | O
        '''


    def p_termino(self,p):
        # termino ::= '(' termino ')' | '!' termino | factor | factor operador_terminal
        '''
        termino : LPAREN termino RPAREN
        | factor
        | NEGAR termino
        | factor operador_terminal
        '''


    def p_terminos(self,p):
        # terminos ::= (('+' | '-')? termino) *
        '''
        terminos : suma_resta termino terminos
        | termino terminos
        | empty
        '''

    def p_exp_simple(self,p):
        # '(' exp_simple ')' | ('+' | '-') termino terminos | termino terminos | termino
        '''
        exp_simple : LPAREN exp_simple RPAREN
        | suma_resta termino terminos
        | termino terminos
        | termino
        '''

    def p_expresion(self, p):
        # ::= '(' expresion ')' | exp_simple ( operador_relacional exp_simple )?
        # | '!' expresion
        '''
        expresion : LPAREN expresion RPAREN
        | exp_simple operador_relacional exp_simple
        | exp_simple
        | NEGAR expresion
        '''

    def p_expresiones(self,p):
        # expresiones ::= ( COMA expresion )*
        '''
        expresiones : COMA expresion expresiones
        | empty
        '''

    def p_conjunto(self,p):
        # conjunto ::= expresion ( COMA expresion )*
        '''
        conjunto : expresion
        | expresion expresiones
        '''

    def p_factor(self,p):
        # ::= DIFERENTE* ( ENTERO | CADENA | NULO | ID | VERDADERO | FALSO | LPAREN expresion RPAREN | conjunto )
        # el diferente factor ahi da problemas de tipo !!!!!!!!entero
        '''
        factor : ENTERO
        | CADENA
        | NULO
        | ID
        | DIFERENTE factor
        | VERDADERO
        | FALSO
        | LPAREN expresion RPAREN
        | conjunto
        '''


    def p_bloque(self, p):
        # bloque   ::= LCORCHETE proposicion* RCORCHETE
        '''
        bloque : sec_proposiciones
        | empty
        '''

    def p_def_funcion(self,p):
        # def_funcion ::= FUN ID LPAREN asignar_tipos RPAREN ( DEV LPAREN asignar_tipos RPAREN )?
        '''
        def_funcion : FUN ID LPAREN asignar_tipos RPAREN
        | FUN ID LPAREN asignar_tipos RPAREN DEV LPAREN asignar_tipos RPAREN
        '''
        print('Parser: Se encontró una def_funcion', p)

    def p_fun_senten(self,p):
        # fun_senten ::= def_funcion bloque FFUN
        '''
        fun_senten : def_funcion bloque FFUN
        '''

    def p_asignar_tipos(self, p):
        # Asigna un tipo a una o mas variables
        # asignar_tipos ::= ID COLON tipos ( COMA ID COLON tipos )*
        '''
        asignar_tipos : ID COLON tipos coma_asignar_tipos
        coma_asignar_tipos : COMA ID COLON tipos coma_asignar_tipos
        | empty
        '''
        print("PARSER: se encontró una o más asignacion de tipo", p)

    def p_inicializar_variable(self,p):
        #
        '''
        inicializar_variable : VAR ID COLON tipos
        '''
        print('PARSER: se inicializa variable ',p)

    def p_lista_ids(self,p):
        # lista_ids ::= LPAREN ID ( COMA ID )* RPAREN
        '''
        lista_ids : LPAREN ID coma_ids RPAREN
        coma_ids : COMA ID coma_ids
        | empty
        '''
        print("PARSER: se encontró una asignacion de tipo list ids", p)


    def p_empty(self,p):
        # funcion para poder tener un lambda
        'empty :'
        pass

    def p_error(self,p):
        if p:
            print("Syntax error at token", p.type, ' y ',p)
            # Just discard the token and tell the parser it's okay.
            self.parser.errok()
        else:
            print("Syntax error at EOF")

    def build(self,**kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)

    def test(self, data):
        result = self.parser.parse(data)
        print(result)
