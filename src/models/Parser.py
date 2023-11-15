import ply.yacc as yacc
from src.models.Lexer import MyLexer


class MyParser:

    # CONSTRUCTOR
    def __init__(self, lexer):
        print("Parser constructor called")
        self.parser = yacc.yacc(module=self)
        self.lexer = lexer
        self.lookUpTable = {}

    # DESTRUCTOR
    def __del__(self):
        print('Parser destructor called.')

    tokens = MyLexer.tokens

    precedence = ( # Aca va la precedencia de tokens
        ('nonassoc', 'MENOR', 'MAYOR'),  # Nonassociative
        ('left', 'SUMA', 'RESTA'),
        ('left', 'MULT', 'DIV'),
        ('left', 'POTENCIA'),
        #('right', 'UMINUS'),  # Unary minus operator
    )
    # GRAMMAR START

    def p_algoritmo(self,p):
        # algoritmo regex inicial que comienza la recursion para reconocer una cantidad arbitraria de proposiciones

        # algoritmo ::= FUN proposicion+ FFUN
        '''
        algoritmo : FUN proposicion proposiciones FFUN
        '''
        print('Parser: se identifica un algoritmo completo exitoso')

    def p_empty(self,p):
        # funcion para poder tener un lambda en el resto de producciones
        'empty :'
        pass

    def p_proposicion(self,p):
        # todo casos (match), hacer_mientras (funciona mal) para (for)
        '''
        proposicion : asignacion PCOMA
        | inicializar_variable PCOMA
        | sentencia_si PCOMA
        | sentencia_mientras PCOMA
        | sentencia_hacer_mientras PCOMA
        | sentencia_leer PCOMA
        | sentencia_escribir PCOMA

        '''
        # print('Parser: se identifica una proposicion', p)

    def p_proposiciones(self,p):
        # proposiciones ::= proposicion*
        '''
        proposiciones : proposicion proposiciones
        | empty
        '''
        # print('Parser: se identifica unas proposiciones', p)

    def p_asignacion(self,p):
        # asignacion ::= ID ASIGNAR ( ID | exp_aritmetica | exp_booleana | NULO | VALOR_CADENA )
        '''
        asignacion : ID ASIGNAR ID
        | ID ASIGNAR exp_aritmetica
        | ID ASIGNAR exp_booleana
        | ID ASIGNAR NULO
        | ID ASIGNAR VALOR_CADENA
        '''

        # Si intenta usar una variable no inicializada
        if self.lookUpTable.get(p[1]) is None:
            print('ERROR: Variable no inicializada siendo asignada', p[1])
        else:
            # todo verificacion de tipos
            print('Parser: se identifica una asignacion', p[1:])


    def p_tipos(self,p):
        # tipos ::= ENTERO | BOOLEANO | DECIMAL | CADENA
        '''
        tipos : ENTERO
        | BOOLEANO
        | DECIMAL
        | CADENA
        '''
        p[0] = p[1]

    def p_inicializar_variable(self,p):
        # inicializar_variable ::= VAR ID COLON tipos
        '''
        inicializar_variable : VAR ID COLON tipos
        '''
        print('PARSER: se inicializa variable ', p[2:])
        p[0] = 'inicializacion_variable'
        # Se guarda la variable en un diccionario haciendo referencia a su tipo
        self.lookUpTable[p[2]] = p[4]


####################### APARADO PARA RECONOCER EXPRESIONES ARITMETICAS CON PARENTESIS Y CUALQUIER LONGITUD ####################

    def p_operador_aritmetico(self, p):
        # operador_aritmetico ::= MULT | DIV | SUMA | RESTA | POTENCIA
        '''
        operador_aritmetico : MULT
        | DIV
        | SUMA
        | RESTA
        | POTENCIA
        '''

        # devuelve el tipo de operacion
        p[0] = p[1]

    def p_factor_aritmetico(self, p):
        # factor_aritmetico ::=  '(' exp_aritmetica ')' | NUM_ENTERO | NUM_DECIMAL
        # factor_aritmetico_id ::= factor_aritmetico | ID
        '''
        factor_aritmetico : LPAREN exp_aritmetica RPAREN
        | NUM_ENTERO
        | NUM_DECIMAL
        factor_aritmetico_id : factor_aritmetico
        | ID
        '''


    def p_operaciones_aritmeticas(self, p):
        # operaciones_aritmeticas ::= (operador_aritmetico factor_aritmetico)*
        # operaciones_aritmeticas_id ::= ( operador_aritmetico factor_aritmetico_id )+
        '''
        operaciones_aritmeticas : operador_aritmetico factor_aritmetico operaciones_aritmeticas
        | empty
        operaciones_aritmeticas_id : operador_aritmetico factor_aritmetico_id operaciones_aritmeticas_id
        | operador_aritmetico factor_aritmetico_id
        '''

    def p_termino_aritmetico(self, p):
        # termino_aritmetico ::= factor_aritmetico ( operaciones_aritmeticas | operaciones_aritmeticas_id )
        # | ID operaciones_aritmeticas_id
        '''
        termino_aritmetico : factor_aritmetico operaciones_aritmeticas
        | ID operaciones_aritmeticas_id
        | factor_aritmetico operaciones_aritmeticas_id
        '''


    def p_exp_arimetica(self, p):
        # exp_aritmetica ::= termino_aritmetico ( operador_aritmetico termino_aritmetico )*
        '''
        exp_aritmetica : termino_aritmetico
        | termino_aritmetico operador_aritmetico exp_aritmetica
        '''
        #print("Parser exp arit: ",p[0-4])


    ####################### APARADO PARA RECONOCER RELACIONES BOOLEANAS CON PARENTESIS Y CUALQUIER LONGITUD ####################

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
        # print('Parser: se identifica un op relacional ', p)

    def p_factor_relacional(self, p):
        #factor_relacional ::= '(' factor_relacional ')' | ( exp_aritmetica | ID ) operador_relacional ( exp_aritmetica | ID )
        '''
        factor_relacional : LPAREN factor_relacional RPAREN
        | exp_aritmetica operador_relacional exp_aritmetica
        | ID operador_relacional exp_aritmetica
        | exp_aritmetica operador_relacional ID
        | ID operador_relacional ID
        '''


    ####################### APARADO PARA RECONOCER EXPRESIONES BOOLEANAS CON PARENTESIS Y CUALQUIER LONGITUD ####################

    def p_operador_booleano(self, p):
        # operador_booleano ::= IGUAL | DIFERENTE | Y | O
        '''
        operador_booleano : IGUAL
        | DIFERENTE
        | Y
        | O
        '''

    def p_factor_booleano(self, p):
        # factor_booleano ::= NEGAR* ( '(' exp_booleana ')' | VERDADERO | FALSO | factor_relacional )
        # factor_booleano_id ::= factor_booleano | NEGAR? ID
        '''
        factor_booleano : LPAREN exp_booleana RPAREN
        | VERDADERO
        | FALSO
        | factor_relacional
        | NEGAR factor_booleano
        factor_booleano_id : factor_booleano
        | ID
        | NEGAR ID
        '''

    def p_operaciones_booleanas(self, p):
        # operaciones_boolenas ::= ( operador_booleano factor_booleano )*
        # operaciones_booleanas_id ::= ( operador_booleano factor_booleano_id )*
        '''
        operaciones_booleanas : operador_booleano factor_booleano operaciones_booleanas
        | empty
        operaciones_booleanas_id : operador_booleano factor_booleano_id operaciones_booleanas_id
        | empty
        '''

    def p_termino_booleano(self, p):
        # termino_booleano ::= factor_booleano operaciones_booleanas
        # | ( ID operador_booleano factor_booleano_id | NEGAR ID ) operaciones_booleanas_id
        '''
        termino_booleano : factor_booleano operaciones_booleanas
        | ID operador_booleano factor_booleano_id operaciones_booleanas_id
        | NEGAR ID operaciones_booleanas_id
        '''

    def p_exp_booleana(self, p):
        # exp_booleana ::= termino_booleano ( operador_booleano termino_booleano )*
        '''
        exp_booleana : termino_booleano
        | termino_booleano operador_booleano exp_booleana
        '''
        #print('Parser: exp booleana', p)

    ###################### SENTENCIAS ###########################

    def p_sentencia_si(self, p):
        # sentencia_si ::= SI exp_booleana ENTONCES proposicion proposiciones ( SINO proposicion proposiciones )?
        '''
        sentencia_si : SI exp_booleana ENTONCES proposicion proposiciones FSI
        | SI exp_booleana ENTONCES proposicion proposiciones SINO proposicion proposiciones FSI
        '''

    def p_sentencia_mientras(self, p):
        # sentencia_mientras ::= MIENTRAS exp_booleana HACER proposicion proposiciones FMIENTRAS
        '''
        sentencia_mientras : MIENTRAS exp_booleana HACER proposicion proposiciones FMIENTRAS
        '''

    def p_sentencia_hacer_mientras(self, p):
        # sentencia_hacer_mientras ::= HACER proposicion proposiciones MIENTRAS exp_booleana
        '''
        sentencia_hacer_mientras : HACER proposicion proposiciones MIENTRAS exp_booleana
        '''

    def p_sentencia_leer(self, p):
        # sentencia_leer ::= LEER '(' ID ')'
        '''
        sentencia_leer : LEER LPAREN ID RPAREN
        '''

    def p_sentencia_escribir(self, p):
        # sentencia_escribir ::= ESCRIBIR '(' ID ')'
        '''
        sentencia_escribir :  ESCRIBIR LPAREN ID RPAREN
        '''


    def p_error(self,p):
        if p:
            print("Syntax error at token", p.type, ' y ', p)
            # Just discard the token and tell the parser it's okay.
            self.parser.errok()
        else:
            print("Syntax error at EOF")

    def build(self,**kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)

    def test(self, data):
        self.parser.parse(data)
        print(self.lookUpTable)
