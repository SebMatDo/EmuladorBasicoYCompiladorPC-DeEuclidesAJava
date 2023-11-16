import ply.yacc as yacc
from src.models.Lexer import MyLexer


class MyParser:

    # CONSTRUCTOR
    def __init__(self, lexer):
        print("Parser constructor called")
        self.parser = yacc.yacc(module=self)
        self.lexer = lexer
        self.lookUpTable = {}
        self.resultAsm = ''
        self.countVar = 0

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
        p[0] = ''
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
        p[0] = p[1]
        self.resultAsm += p[1]

    def p_proposiciones(self,p):
        # proposiciones ::= proposicion*
        '''
        proposiciones : proposicion proposiciones
        | empty
        '''
        print('Parser: se identifica unas proposiciones', p[0:])


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
        pseudoAsm = ''
        if self.lookUpTable.get(p[1]) is None:
            print('ERROR: Variable no inicializada siendo asignada', p[1])
        else:
            # todo verificacion de tipos
            pseudoAsm += p[3]
            pseudoAsm += 'Almacenar A,' + str(self.lookUpTable[p[1]][1]) + '\n' #se almacena la variable en la ram. usando el lookup para obtener su numero especifico
            p[0] = pseudoAsm
            print('Parser: se identifica una asignacion\n', p[0])



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
        p[0] = ''
        # mientras haya menos de 10 variables
        if self.countVar <= 10:
            # Se guarda la variable en un diccionario haciendo referencia a su tipo y su numero de variable
            # si es una nueva var la cuenta, si no, la reemplaza
            if self.lookUpTable.get(p[2]) is None:
                self.lookUpTable[p[2]] = [p[4], self.countVar]
                self.countVar += 1
            else:
                self.lookUpTable[p[2]][0] = p[4]
        else:
            print('ERROR NO SE PUEDEN DEFINIR MÁS DE 10 VARIABLES')


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
        # devuelve el valor del factor, p[2] si es un exparitmetico entre parentesis y p[1] de resto
        if len(p) == 3:
            p[0] = p[2]
        else:
            p[0] = p[1]


    def p_operaciones_aritmeticas(self, p):
        # operaciones_aritmeticas ::= (operador_aritmetico factor_aritmetico)*
        '''
        operaciones_aritmeticas : operador_aritmetico factor_aritmetico operaciones_aritmeticas
        | empty
        '''

        # esto permite que p[0] mantenga la recursion
        pseudoAsm = ''
        if len(p) == 4:
            if p[3] != '':
                pseudoAsm += 'CargarValor B,' + p[2] + '\n'
                if p[1] == '+':
                    pseudoAsm += 'Sumar A,B\n'
                pseudoAsm += p[3]
                p[0] = pseudoAsm
            else:
                pseudoAsm += 'CargarValor B,' + p[2] + '\n'
                if p[1] == '+':
                    pseudoAsm += 'Sumar A,B\n'
                p[0] = pseudoAsm
        else:
            p[0] = ''
        print('ops aritmeticas: ', p[0:])


    def p_operaciones_aritmeticas_id(self, p):
        # operaciones_aritmeticas_id ::= ( operador_aritmetico factor_aritmetico_id )+
        '''
        operaciones_aritmeticas_id : operador_aritmetico factor_aritmetico_id operaciones_aritmeticas_id
        | operador_aritmetico factor_aritmetico_id
        '''
        # esto permite que p[0] mantenga la recursion
        # aca puede haber IDS o numeros normales.
        pseudoAsm = ''
        isVar = self.lookUpTable.get(p[2]) is not None
        if isVar:
            numVar = str(self.lookUpTable[p[2]][1])
        asmToAdd = ''
        if len(p) == 4:  # con recursion
            if p[3] != '':
                asmToAdd = p[3]
        if isVar:
            pseudoAsm += 'Cargar B,' + numVar + '\n'
        else:
            pseudoAsm += 'CargarValor B,' + p[2] + '\n'
        if p[1] == '+':
            pseudoAsm += 'Sumar A,B\n'
        pseudoAsm += asmToAdd
        p[0] = pseudoAsm

        print('ops aritmeticas con id: ', p[0:])

    def p_termino_aritmetico(self, p):
        # termino_aritmetico ::= factor_aritmetico ( operaciones_aritmeticas | operaciones_aritmeticas_id )
        # | ID operaciones_aritmeticas_id
        '''
        termino_aritmetico : factor_aritmetico operaciones_aritmeticas
        | ID operaciones_aritmeticas_id
        | factor_aritmetico operaciones_aritmeticas_id
        '''

        pseudoAsm = ''
        asmToAdd = ''
        if p[2] != '':
            asmToAdd = p[2]
        if self.lookUpTable.get(p[1]) is None:  #  si p[1] no es id entonces lo carga en A
            pseudoAsm += 'CargarValor A,' + p[1] + '\n'
            pseudoAsm += p[2]
        else: # si es ID lo carga desde la ram
            pseudoAsm += 'Cargar A,' + str(self.lookUpTable.get(p[1])[1]) + '\n'
            pseudoAsm += asmToAdd

        p[0] = pseudoAsm
        print('terminos aritmeticos: ', p[0:])

        # acá ya termina la recursión y por lo tanto puedo hacer pseudoasm



    def p_exp_arimetica(self, p):
        # exp_aritmetica ::= termino_aritmetico ( operador_aritmetico termino_aritmetico )*
        '''
        exp_aritmetica : termino_aritmetico
        | termino_aritmetico operador_aritmetico exp_aritmetica
        '''
        # si len = 2 entonces es un solo termino si no entonces son muchos terminos
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 4:
            p[0] = p[1] + p[2] + p[3]
        # todo creo que aca va la conversion a asm por parte de las ops aritmeticas
        # supongo yo, haciendo que cargue a registro el primero que encuentre, haga la operacion con el siguiente operador y asi sucesivamente

        print("Parser exp arit: ",p[0:])

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
        print(self.resultAsm)
