import ply.yacc as yacc
from src.models.Lexer import MyLexer
from src.utils.convertions import isNum


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
        ('left', 'NEGAR'),
        ('left', 'Y'),
        ('left', 'O'),

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
        | RESTA factor_aritmetico
        '''

        # ahora la logica esta aca para poder manejar mejor las cargas
        pseudoAsm = ''
        print(p[0:])

        if p[1] == '-':
            if isNum(p[2]):
                pseudoAsm += 'CargarValor B,' + p[2] + '\n'
                pseudoAsm += 'CargarValor A,0\n Restar A,B\n'
            else: # si es una var o asm
                if self.lexerLookUpTable.get(p[2]) is None:  # si el str no es var
                    pseudoAsm += p[2]
                    pseudoAsm += 'Copiar A,B\n CargarValor A,0\n Restar A,B\n'

                else: # si es var
                    if self.lookUpTable.get(p[2]) is None:
                        raise Exception('ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[2])

                    pseudoAsm += 'Cargar B,' + str(self.lookUpTable.get(p[2])[1]) + '\n'
                    pseudoAsm += 'CargarValor A,0\n Restar A,B\n'
            p[0] = pseudoAsm
            return p[0]

        if p[1] == '(': # si viene en parentesis
            if not isNum(p[2]): # y no es numerico
                pseudoAsm += p[2] # se copia lo que trae
                p[0] = pseudoAsm
            else:
                p[0] = p[2] # si esnumerico se devuelve asi solito
            return p[0]

        if len(p) == 2:  # si se toma la ruta de factor solito
            p[0] = p[1]

        if len(p) == 4:  # si viene así hay cosas.
            if not isNum(p[1]) and isNum(p[3]): # caso (var or asm) op_aritmetico num
                if self.lexerLookUpTable.get(p[1]) is None:  # si el str no es variable caso asm op num
                    pseudoAsm += p[1]
                else:  # si es una variable caso var op num
                    if self.lookUpTable.get(p[1]) is None:
                        raise Exception('ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[3])
                    pseudoAsm += 'Cargar A,' + str(self.lookUpTable.get(p[1])[1]) + '\n'
                pseudoAsm += 'Copiar A,B\n'  # si no es numerico es porque p[3] es una exp, copiamos su registro a B

            if not isNum(p[3]) and isNum(p[1]): # caso num op_aritmetico (var or asm)
                if self.lexerLookUpTable.get(p[3]) is None: # si el str no es variable caso num op asm
                    pseudoAsm += p[3]
                else: # si es una variable caso num op var
                    if self.lookUpTable.get(p[3]) is None:
                        raise Exception('ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[3])
                    pseudoAsm += 'Cargar A,' + str(self.lookUpTable.get(p[3])[1]) + '\n'
                pseudoAsm += 'Copiar A,B\n'  # si no es numerico es porque p[3] es una exp, copiamos su registro a B

            if not isNum(p[3]) and not isNum(p[1]): # ambos factores son ASM o variables o una combinacion de ambos
                if self.lexerLookUpTable.get(p[1]) is None and self.lexerLookUpTable.get(p[3]) is None: # asm op asm
                    pseudoAsm += p[1]
                    pseudoAsm += 'Copiar A,D\n'
                    pseudoAsm += p[3]
                    pseudoAsm += 'Copiar A,B\n'
                    pseudoAsm += 'Copiar D,A\n'

                if self.lexerLookUpTable.get(p[1]) is not None and self.lexerLookUpTable.get(p[3]) is not None: # ambas son variabes var op var
                    if self.lookUpTable.get(p[3]) is None:
                        raise Exception('ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[3])
                    if self.lookUpTable.get(p[1]) is None:
                        raise Exception('ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[1])
                    pseudoAsm += 'Cargar A,' + str(self.lookUpTable.get(p[1])[1]) + '\n'
                    pseudoAsm += 'Cargar B,' + str(self.lookUpTable.get(p[3])[1]) + '\n'

                if self.lexerLookUpTable.get(p[3]) is not None and self.lexerLookUpTable.get(p[1]) is None:  # solo la p[3] es variable caso asm op var
                    if self.lookUpTable.get(p[3]) is None:
                        raise Exception('ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[3])
                    pseudoAsm += p[1]
                    pseudoAsm += 'Cargar B,' + str(self.lookUpTable.get(p[1])[1]) + '\n'

                if self.lexerLookUpTable.get(p[1]) is not None and self.lexerLookUpTable.get(p[3]) is None: # solo la p[1] es variable caso var op asm
                    if self.lookUpTable.get(p[1]) is None:
                        raise Exception('ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[1])
                    pseudoAsm += p[3]
                    pseudoAsm += 'Cargar B,' + str(self.lookUpTable.get(p[1])[1]) + '\n'


            if isNum(p[1]):  # verificar si el factor es numerico
                pseudoAsm += 'CargarValor A,' + p[1] + '\n'  # si es numerico carga su valor en A

            if isNum(p[3]):  # verificar si el factor es numerico
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
                    pseudoAsm += 'Div A,B \n' # se hizo una operacion inversa
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
        if isNum(p[1]):
            p[0] = 'CargarValor A,' + p[1] + '\n'
        else: # si no es un numero es un asm y se pasa normal
            p[0] = p[1]
        print("Parser exp arit: ",p[0:])

    ####################### APARTADO PARA RECONOCER RELACIONES BOOLEANAS CON PARENTESIS Y CUALQUIER LONGITUD ####################
    #
    # def p_operador_relacional(self,p):
    #     # operador_relacional ::= IGUAL | DIFERENTE | LEQ | GEQ | MENOR | MAYOR
    #     '''
    #     operador_relacional : IGUAL
    #     | DIFERENTE
    #     | LEQ
    #     | GEQ
    #     | MENOR
    #     | MAYOR
    #     '''
    #     # print('Parser: se identifica un op relacional ', p)
    #
    # def p_factor_relacional(self, p):
    #     #factor_relacional ::= '(' factor_relacional ')' | ( exp_aritmetica | ID ) operador_relacional ( exp_aritmetica | ID )
    #     '''
    #     factor_relacional : LPAREN factor_relacional RPAREN
    #     | exp_aritmetica operador_relacional exp_aritmetica
    #     | ID operador_relacional exp_aritmetica
    #     | exp_aritmetica operador_relacional ID
    #     | ID operador_relacional ID
    #     '''
    #     print('FACTOR RELACIONAL')

    ####################### APARADO PARA RECONOCER EXPRESIONES BOOLEANAS CON PARENTESIS Y CUALQUIER LONGITUD ####################

    def p_factor_booleano(self, p):
        # factor_booleano ::= NEGAR* ( '(' exp_booleana ')' | VERDADERO | FALSO | factor_relacional )
        # factor_booleano_id ::= factor_booleano | NEGAR? ID
        '''
        factor_booleano : VERDADERO
        | FALSO
        | ID
        '''
        print('FACTOR BOOLEANO')
        if p[1] == 'verdadero':
            p[0] = '1'
        elif p[1] == 'falso':
            p[0] = '0'
        else: # devolver normal si es variable
            p[0] = p[1]

    # def p_operaciones_booleanas(self, p):
    #     # operaciones_boolenas ::= ( operador_booleano factor_booleano )*
    #     # operaciones_booleanas_id ::= ( operador_booleano factor_booleano_id )*
    #     '''
    #     operaciones_booleanas : operador_booleano factor_booleano operaciones_booleanas
    #     | empty
    #     '''

    def p_termino_booleano(self, p):
        # termino_booleano ::= factor_booleano operaciones_booleanas
        # | ( ID operador_booleano factor_booleano_id | NEGAR ID ) operaciones_booleanas_id
        '''
        termino_booleano : LPAREN termino_booleano RPAREN
        | NEGAR termino_booleano
        | termino_booleano Y termino_booleano
        | termino_booleano O termino_booleano
        | factor_booleano
        '''
        # ahora la logica esta aca para poder manejar mejor las cargas
        pseudoAsm = ''

        if p[1] == '!':
            if isNum(p[2]):# si viene como 0 o 1
                pseudoAsm += 'CargarValor A,' + p[2] + '\n'
            else: # si es una var o asm
                if self.lexerLookUpTable.get(p[2]) is None:  # si el str no es var
                    pseudoAsm += p[2]
                else: # si es var
                    if self.lookUpTable.get(p[2]) is None:
                        raise Exception('ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[2])
                    pseudoAsm += 'Cargar B,' + str(self.lookUpTable.get(p[2])[1]) + '\n'

            # luego de tener el valor en el registro A, hago la logica para
            # hacer un swap entre 0 y 1. !true =false. !false =true
            pseudoAsm += 'CargarValor B,1\n Restar A,B\n'
            etiqueta = 'jmp' + str(self.countJumps)
            self.countJumps += 1
            pseudoAsm += 'SaltarSiCero ' + etiqueta + '\n'
            pseudoAsm += 'CargarValor A,1'
            pseudoAsm += etiqueta + ':\n'
            p[0] = pseudoAsm
            return p[0]

        if p[1] == '(': # si viene en parentesis
            if not isNum(p[2]): # y no es numerico
                pseudoAsm += p[2] # se copia lo que trae
                p[0] = pseudoAsm
            else:
                p[0] = p[2] # si esnumerico se devuelve asi solito
            return p[0]

        if len(p) == 2:  # si se toma la ruta de factor solito
            p[0] = p[1]
            return p[0]

        if len(p) == 4:  # si viene así hay cosas.
            if not isNum(p[1]) and isNum(p[3]):  # caso (var or asm) op_bool num
                if self.lexerLookUpTable.get(p[1]) is None:  # si el str no es variable caso asm op num
                    pseudoAsm += p[1]
                else:  # si es una variable caso var op num
                    if self.lookUpTable.get(p[1]) is None:
                        raise Exception(
                            'ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[3])
                    pseudoAsm += 'Cargar A,' + str(self.lookUpTable.get(p[1])[1]) + '\n'
                pseudoAsm += 'Copiar A,B\n'  # si no es numerico es porque p[3] es una exp, copiamos su registro a B

            if not isNum(p[3]) and isNum(p[1]): # caso num op_aritmetico (var or asm)
                if self.lexerLookUpTable.get(p[3]) is None: # si el str no es variable caso num op asm
                    pseudoAsm += p[3]
                else: # si es una variable caso num op var
                    if self.lookUpTable.get(p[3]) is None:
                        raise Exception('ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[3])
                    pseudoAsm += 'Cargar A,' + str(self.lookUpTable.get(p[3])[1]) + '\n'
                pseudoAsm += 'Copiar A,B\n'  # si no es numerico es porque p[3] es una exp, copiamos su registro a B

            if not isNum(p[3]) and not isNum(p[1]): # ambos factores son ASM o variables o una combinacion de ambos
                if self.lexerLookUpTable.get(p[1]) is None and self.lexerLookUpTable.get(p[3]) is None: # asm op asm
                    pseudoAsm += p[1]
                    pseudoAsm += 'Copiar A,D\n'
                    pseudoAsm += p[3]
                    pseudoAsm += 'Copiar A,B\n'
                    pseudoAsm += 'Copiar D,A\n'

                if self.lexerLookUpTable.get(p[1]) is not None and self.lexerLookUpTable.get(p[3]) is not None: # ambas son variabes var op var
                    if self.lookUpTable.get(p[3]) is None:
                        raise Exception('ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[3])
                    if self.lookUpTable.get(p[1]) is None:
                        raise Exception('ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[1])
                    pseudoAsm += 'Cargar A,' + str(self.lookUpTable.get(p[1])[1]) + '\n'
                    pseudoAsm += 'Cargar B,' + str(self.lookUpTable.get(p[3])[1]) + '\n'

                if self.lexerLookUpTable.get(p[3]) is not None and self.lexerLookUpTable.get(p[1]) is None:  # solo la p[3] es variable caso asm op var
                    if self.lookUpTable.get(p[3]) is None:
                        raise Exception('ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[3])
                    pseudoAsm += p[1]
                    pseudoAsm += 'Cargar B,' + str(self.lookUpTable.get(p[1])[1]) + '\n'

                if self.lexerLookUpTable.get(p[1]) is not None and self.lexerLookUpTable.get(p[3]) is None: # solo la p[1] es variable caso var op asm
                    if self.lookUpTable.get(p[1]) is None:
                        raise Exception('ERROR: La variable no ha sido inicializada y por lo tanto no se puede proseguir', p[1])
                    pseudoAsm += p[3]
                    pseudoAsm += 'Cargar B,' + str(self.lookUpTable.get(p[1])[1]) + '\n'


            if isNum(p[1]):  # verificar si el factor es numerico
                pseudoAsm += 'CargarValor A,' + p[1] + '\n'  # si es numerico carga su valor en A

            if isNum(p[3]):  # verificar si el factor es numerico
                pseudoAsm += 'CargarValor B,' + p[3] + '\n'  # si es numerico carga su valor en B

            # dependiendo de la operacion se escribe una instrucción
            match p[2]:
                case '&&':
                    pseudoAsm += 'Mult A,B\n'
                case '||':

                    pseudoAsm += 'Sumar A,B\n' # en el or solo da cero si ambos son cero, entonces podemos sumar y verificar si da 2
                    pseudoAsm += 'CargarValor C,1\n Restar A,C\n'

                    etiquetaTrue = 'jmp' + str(self.countJumps)
                    self.countJumps += 1
                    etiquetaFalse = 'jmp' + str(self.countJumps)
                    self.countJumps += 1
                    etiquetaFin = 'jmp' + str(self.countJumps)
                    self.countJumps += 1

                    pseudoAsm += 'SaltarSiCero ' + etiquetaTrue + '\n'
                    pseudoAsm += 'SaltarSiNeg ' + etiquetaFalse + '\n'
                    pseudoAsm += 'Saltar ' + etiquetaFin + '\n'

                    pseudoAsm += etiquetaTrue + ':\n'
                    pseudoAsm += 'CargarValor A,1\n'
                    pseudoAsm += 'Saltar ' + etiquetaFin + '\n'

                    pseudoAsm += etiquetaFalse + ':\n'
                    pseudoAsm += 'CargarValor A,0\n'

                    pseudoAsm += etiquetaFin + ':\n'


            p[0] = pseudoAsm

        print('term bool ', p[0:])


    def p_exp_booleana(self, p):
        # exp_booleana ::= termino_booleano ( operador_booleano termino_booleano )*
        '''
        exp_booleana : termino_booleano
        '''
        # Verifica si lo que llega como exp booleana es un ASM o un bool
        if isNum(p[1]):
            p[0] = 'CargarValor A,' + p[1] + '\n'
        else:
            p[0] = p[1]
        print('Parser: exp booleana', p[0:])

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
