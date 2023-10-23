import sys
from PyQt5.QtWidgets import QApplication
import ply.lex as lex
from pathlib import Path
import os
# import ply.yacc as yacc

lookUpTable = {}

# Step 1: Lexer rules

tokens = (
    'NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE',
    'LPAREN','RPAREN',
    'LEQ','GEQ', # Less than or equal, Greater than or equal
    'GREATER','LESS', # Greater than, Less than
    'EQ', # Equals
    'PARAMS', # Params
    'ID', # Identifiers
    'FUN',
    'VAR', # Variables
    'MIENTRAS',
    'FMIENTRAS',
    'CASO',
    'HACER',
    'DEV',
    'FFUN',
    'MOD',
    'COMMA', # Comma
    'SEMICOLON', # Semicolon
    'COLON'
)

# Regular definition of tokens

reserved = {
    'fun' : 'FUN',
    'var' : 'VAR',
    'mientras' : 'MIENTRAS',
    'fmientras' : 'FMIENTRAS',
    'caso' : 'CASO',
    'hacer' : 'HACER',
    'dev' : 'DEV',
    'ffun' : 'FFUN',
    'mod' : 'MOD'
}

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
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LEQ     = r'<='
t_GEQ     = r'>='
t_GREATER = r'>'
t_LESS    = r'<'
t_EQ      = r'='
t_COLON  = r':'
t_COMMA   = r','
t_SEMICOLON = r';'

t_ignore  = ' \t'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
        return t
    if t.value not in lookUpTable:
        lookUpTable[t.value] = {'currentValue': 0}
    t.value = (t.value, lookUpTable[t.value])
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

#def test_lexer():
# Test it out
data_folder = Path(os.getcwd())
file_path = data_folder.parent.parent / "tests/lexer/codigoLibro.lp"
print(file_path)
data = open(file_path,'r').read()


# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
