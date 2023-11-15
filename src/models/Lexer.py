
import ply.lex as lex


class MyLexer():
    # CONSTRUCTOR
    def __init__(self):
        print('Lexer constructor called.')
        self.lexer = lex.lex(module=self)
        self.lexer.begin('INITIAL')

    # DESTRUCTOR
    def __del__(self):
        print('Lexer destructor called.')

    lookUpTable = {}

    # Step 1: Lexer rules

    # Terminales
    tokens = (
        'NUMERO',
        'SUMA', 'RESTA', 'MULT', 'DIV',
        'LPAREN', 'RPAREN',
        'LEQ', 'GEQ',  # Less than or equal, Greater than or equal
        'MAYOR', 'MENOR',  # Greater than, Less than
        'IGUAL',  # Equals
        'PARAMETROS',  # Params
        'ID',  # Identifiers
        'FUN',
        'VAR',  # Variables
        'MIENTRAS',
        'FMIENTRAS',
        'CASO',
        'HACER',
        'DEV',
        'FFUN',
        'MOD',
        'COMA',  # Comma
        'PCOMA',  # Semicolon
        'COLON',
        'ENTERO',
        'BOOLEANO',
        'DECIMAL',
        'CADENA',
        'O',
        'Y',
        'SI',
        'ENTONCES',
        'SINO',
        'ASIGNAR',
        'DIFERENTE',
        'VERDADERO',
        'FALSO',
        'NULO',
        'NEGAR',
        'LCORCHETE',
        'RCORCHETE',
    )

    # palabras reservadas
    reserved = {
        'fun': 'FUN',
        'var': 'VAR',
        'mientras': 'MIENTRAS',
        'fmientras': 'FMIENTRAS',
        'caso': 'CASO',
        'hacer': 'HACER',
        'dev': 'DEV',
        'ffun': 'FFUN',
        'mod': 'MOD',
        'var': 'VAR',
        'entero': 'ENTERO',
        'bool': 'BOOLEANO',
        'decimal': 'DECIMAL',
        'cadena' : 'CADENA',
        'si': 'SI',
        'entonces': 'ENTONCES',
        'sino': 'SINO',
        'verdadero': 'VERDADERO',
        'falso': 'FALSO',
        'nulo' : 'NULO',
        'negar' : 'NEGAR',
    }

    # Regular definition of tokens

    digit = r'[0-9]'
    letter = r'[a-zA-Z]'

    # Regular expression rules for simple tokens
    t_FUN = r'fun'
    t_VAR = r'var'
    t_MIENTRAS = r'mientras'
    t_FMIENTRAS = r'fmientras'
    t_CASO = r'caso'
    t_HACER = r'hacer'
    t_DEV = r'dev'
    t_FFUN = r'ffun'
    t_MOD = r'mod'
    t_SUMA = r'\+'
    t_RESTA = r'-'
    t_MULT = r'\*'
    t_DIV = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LEQ = r'<='
    t_GEQ = r'>='
    t_MAYOR = r'>'
    t_MENOR = r'<'
    t_IGUAL = r'=='
    t_DIFERENTE = r'!='
    t_ASIGNAR = r'='
    t_COLON = r':'
    t_COMA = r','
    t_PCOMA = r';'
    t_ignore = ' \t'
    ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
    NUMERO = r'\d+(\.\d+)?'
    t_ignore_COMMENT = r'\#\#.*'
    t_BOOLEANO = r'bool'
    t_ENTERO = r'entero'
    t_DECIMAL = r'decimal'
    t_CADENA = r'cadena'
    t_NULO = r'nulo'
    t_NEGAR = r'!'
    t_Y = r'&&'
    t_O = r'\|\|'
    t_LCORCHETE = r'{'
    r_RCORCHETE = r'}'

    # A regular expression rule with some action code

    @lex.TOKEN(NUMERO)
    def t_NUMERO(self, t):
        t.value = float(t.value)
        return t

    @lex.TOKEN(ID)
    def t_ID(self, t):
        if t.value in self.reserved:
            t.type = self.reserved[t.value]
            return t
        if t.value not in self.lookUpTable:
            self.lookUpTable[t.value] = {'currentValue': 0}
        t.value = (t.value, self.lookUpTable[t.value])
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
    # Error handling rule
    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        t.lexer.skip(1)

# Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)



# # Build the lexer
# lexer = lex.lex()
#
# Test it out

    def test(self, data):
        # Give the lexer some input
        self.lexer.input(data)

        # Tokenize
        while True:
            tok = self.lexer.token()
            if not tok:
                break      # No more input
            print(tok)
