import ply.yacc as yacc
from src.models.Lexer import MyLexer


class MyParser:

    # CONSTRUCTOR
    def __init__(self, lexer):
        print("Parser constructor called")
        self.parser = yacc.yacc(module=self)
        self.lexer = lexer
        self.lookUpTable = {}
        self.lexerLookUpTable = MyLexer.lookUpTable
        self.resultAsm = ''
        self.countVar = 1
        self.lookUpJumps = {}
        self.countJumps = 1

    # DESTRUCTOR
    def __del__(self):
        print('Parser destructor called.')

    tokens = MyLexer.tokens

    precedence = ( # Aca va la precedencia de tokens
        #('nonassoc', 'MENOR', 'MAYOR'),  # Nonassociative
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
        #print('Parser: se identifica unas proposiciones', p[0:])


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
            print('ERROR: Variable INICIAL no inicializada siendo asignada', p[1])
        else:
            # todo verificacion de tipos

            # si es de tipo a = b hace esto
            # if p[3] == id
            if self.lexerLookUpTable.get(p[3]) is not None:
                # Si es una variable de lexer pero no ha sido inicializada
                # Si no se hace esta comprobacion se agregaria un NONE Y rompe el programa
                if self.lookUpTable.get(p[3]) is None:
                    print('ERROR VARIABLE 2 NO INICIALIZADA')
                else:
                    pseudoAsm += 'Cargar A,' + str(self.lookUpTable.get(p[3])[1]) + '\n'

            else: # if p[3] != id
                # entonces esto es de tipo a = expresion
                # ahora toca mirar si lo que llega es un asm o un factor.
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

    def p_factor_aritmetico(self, p):
        # factor_aritmetico_id ::= factor_aritmetico | ID
        '''
        factor_aritmetico : NUM_ENTERO
        | NUM_DECIMAL
        | ID
        '''

        # Verificacion de decimales
        if type(p[1]) == float:
            print('ERROR EL ANALIZADOR SINTACTICO DETECTA UN DECIMAL, se tomará solo la parte entera')
            p[0] = str(int(p[1]))
        else:
            p[0] = str(p[1])
        #print('Factor aritmetico: ', p[0:])
    #
    # def p_factor_aritmetico_id(self, p):
    #     '''
    #     factor_aritmetico_id: factor_aritmetico
    #     | ID
    #     '''
    #
    # def p_operaciones_aritmeticas_id(self, p):
    #     # operaciones_aritmeticas_id ::= ( operador_aritmetico factor_aritmetico_id )+
    #     '''
    #     operaciones_aritmeticas_id : operador_aritmetico factor_aritmetico_id operaciones_aritmeticas_id
    #     | operador_aritmetico factor_aritmetico_id
    #     '''
    #     # esto permite que p[0] mantenga la recursion
    #     # aca puede haber IDS o numeros normales.
    #     pseudoAsm = ''
    #     asmToAdd = ''
    #     isVar = self.lookUpTable.get(p[2]) is not None
    #
    #     if isVar:
    #         numVar = str(self.lookUpTable[p[2]][1])
    #         pseudoAsm += 'Cargar B,' + numVar + '\n'
    #     else:
    #         pseudoAsm += 'CargarValor B,' + p[2] + '\n'
    #
    #     if len(p) == 4:  # con recursion
    #         asmToAdd = p[3]
    #
    #     # dependiendo de la operacion se escribe una instrucción
    #     match p[1]:
    #         case '+':
    #             pseudoAsm += 'Sumar A,B\n'
    #         case '-':
    #             pseudoAsm += 'Restar A,B\n'
    #         case '*':
    #             pseudoAsm += 'Mult A,B\n'
    #         case '/':
    #             pseudoAsm += 'Div A,B\n'
    #         case '^':  # Este es especial porque requiere un ciclo, x^y = y veces x
    #             # Se comienzan a manejar saltos (etiquetas)
    #             pseudoAsm += 'Copiar A,C\n'
    #             pseudoAsm += 'CargarValor D,1\n'
    #             pseudoAsm += 'Restar B,D\n'
    #             etiqueta = 'jmp' + str(self.countJumps)
    #             self.countJumps += 1
    #             pseudoAsm += etiqueta + ':\n'
    #             pseudoAsm += 'Mult A,C\n'
    #             pseudoAsm += 'Restar B,D\n'
    #             pseudoAsm += 'SaltarSiPos ' + etiqueta + '\n'
    #
    #     pseudoAsm += asmToAdd
    #     p[0] = pseudoAsm
    #
    #     print('ops aritmeticas con id: ', p[0:])

    def p_termino_aritmetico(self, p):
        # termino_aritmetico ::= factor_aritmetico ( operaciones_aritmeticas | operaciones_aritmeticas_id )
        # | ID operaciones_aritmeticas_id
        '''
        termino_aritmetico : LPAREN termino_aritmetico RPAREN
        | termino_aritmetico POTENCIA termino_aritmetico
        | termino_aritmetico MULT termino_aritmetico
        | termino_aritmetico DIV termino_aritmetico
        | termino_aritmetico SUMA termino_aritmetico
        | termino_aritmetico RESTA termino_aritmetico
        | factor_aritmetico
        '''

        # ahora la logica esta aca para poder manejar mejor las cargas
        pseudoAsm = ''

        if p[1] == '(': # si viene en parentesis
            if not str.isnumeric(p[2]): # y no es numerico
                pseudoAsm += p[2] # se copia lo que trae
                #todo verificar con variables
                p[0] = pseudoAsm
            else:
                p[0] = p[2] # si esnumerico se devuelve asi solito
            return p[0]

        if len(p) == 2:  # si se toma la ruta de factor solito
            p[0] = p[1]

        if len(p) == 4:  # si viene así hay cosas.

            # se añade lo que se traia de antes
            if not str.isnumeric(p[1]) and str.isnumeric(p[3]): # caso (var or asm) op_aritmetico num, o llevamos al otro caso
                #swap
                temp = p[1]
                temp2 = p[3]
                p[3] = temp
                p[1] = temp2

            # ya que las variables o el asm siempre quedaran en p[3]

            if not str.isnumeric(p[3]) and str.isnumeric(p[1]): # caso num op_aritmetico (var or asm)
                if self.lexerLookUpTable.get(p[3]) is None: # si el str no es variable
                    pseudoAsm += p[3]
                else: # si es una variable caso num op var
                    if self.lookUpTable.get(p[3]) is None:
                        raise Exception('ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[3])
                    pseudoAsm += 'Cargar A,' + str(self.lookUpTable.get(p[3])[1]) + '\n'
                pseudoAsm += 'Copiar A,B\n'  # si no es numerico es porque p[3] es una exp, copiamos su registro a B

            if not str.isnumeric(p[3]) and not str.isnumeric(p[1]): # ambos factores son ASM o variables o una combinacion de ambos
                if self.lexerLookUpTable.get(p[1]) is None and self.lexerLookUpTable.get(p[3]) is None: # ambas asm
                    pseudoAsm += p[1]
                    pseudoAsm += 'Copiar A,D\n'
                    pseudoAsm += p[3]
                    pseudoAsm += 'Copiar A,B\n'
                    pseudoAsm += 'Copiar D,A\n'

                if self.lexerLookUpTable.get(p[1]) is not None and self.lexerLookUpTable.get(p[3]) is not None: # ambas son variabes
                    if self.lookUpTable.get(p[3]) is None:
                        raise Exception('ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[3])
                    if self.lookUpTable.get(p[1]) is None:
                        raise Exception('ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[1])
                    pseudoAsm += 'Cargar A,' + str(self.lookUpTable.get(p[1])[1]) + '\n'
                    pseudoAsm += 'Cargar B,' + str(self.lookUpTable.get(p[3])[1]) + '\n'

                if self.lexerLookUpTable.get(p[3]) is not None and self.lexerLookUpTable.get(p[1]) is None:  # solo la p[3] es variable
                    # swap y pasa la variable a p[1]
                    temp = p[1]
                    temp2 = p[3]
                    p[3] = temp
                    p[1] = temp2

                if self.lexerLookUpTable.get(p[1]) is not None and self.lexerLookUpTable.get(p[3]) is None: # solo la p[1] es variable
                    if self.lookUpTable.get(p[1]) is None:
                        raise Exception('ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[1])
                    pseudoAsm += p[3]
                    pseudoAsm += 'Cargar B,' + str(self.lookUpTable.get(p[1])[1]) + '\n'


            if str.isnumeric(p[1]):  # verificar si el factor es numerico
                pseudoAsm += 'CargarValor A,' + p[1] + '\n'  # si es numerico carga su valor en A

            if str.isnumeric(p[3]):  # verificar si el factor es numerico
                pseudoAsm += 'CargarValor B,' + p[3] + '\n'  # si es numerico carga su valor en B

            # dependiendo de la operacion se escribe una instrucción
            match p[2]:
                case '+':
                    pseudoAsm += 'Sumar A,B\n'
                case '-':
                    pseudoAsm += 'Restar A,B\n'
                case '*':
                    pseudoAsm += 'Mult A,B\n'
                case '/':
                    pseudoAsm += 'Div A,B\n'
                case '^':  # Este es especial porque requiere un ciclo, x^y = y veces x
                    # se pasa el reg D (que puede contener info de otras operaciones con parentesis) a una variable protegida especial 0
                    pseudoAsm += 'Almacenar D, 0\n'
                    # Se comienzan a manejar saltos (etiquetas)
                    pseudoAsm += 'Copiar A,C\n'
                    pseudoAsm += 'CargarValor D,1\n'
                    pseudoAsm += 'Restar B,D\n'
                    etiqueta = 'jmp' + str(self.countJumps)
                    self.countJumps += 1
                    pseudoAsm += etiqueta + ':\n'
                    pseudoAsm += 'Mult A,C\n'
                    pseudoAsm += 'Restar B,D\n'
                    pseudoAsm += 'SaltarSiPos ' + etiqueta + '\n'
                    # al final vuelve a traer el antiguo registro D
                    pseudoAsm += 'Cargar D, 0\n'

            p[0] = pseudoAsm

        print('term aritm ', p[0:])


    def p_exp_arimetica(self, p):
        '''
        exp_aritmetica : termino_aritmetico
        '''
        # Verifica si lo que llega como exp aritmetica es un ASM o un numero
        if str.isnumeric(p[1]) or str.isdecimal(p[1]):
            p[0] = 'CargarValor A,' + p[1] + '\n'
        else:
            p[0] = p[1]
        print("Parser exp arit: ",p[0:])

    ####################### APARTADO PARA RECONOCER RELACIONES BOOLEANAS CON PARENTESIS Y CUALQUIER LONGITUD ####################

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
        print('FACTOR RELACIONAL')

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
        print('FACTOR BOOLEANO')

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
