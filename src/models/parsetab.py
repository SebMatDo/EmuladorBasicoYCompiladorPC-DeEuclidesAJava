
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARREGLO ASSIGN BOOLEANO CADENA CASO COLON COMMA DECIMAL DEV DIVIDE ENTERO ENTONCES EQUAL FALSO FFUN FMIENTRAS FUN GEQ GREATER HACER ID LEQ LESS LPAREN MIENTRAS MINUS MOD NOTEQ NUMBER O PARAMS PLUS RPAREN SEMICOLON SI SINO TIMES VAR VERDADERO Ytype_assignment : VAR ID COLON type SEMICOLON\n        type : ENTERO\n        | BOOLEANO\n        | DECIMAL\n        | CADENA\n        | ARREGLO\n        '
    
_lr_action_items = {'VAR':([0,],[2,]),'$end':([1,11,],[0,-1,]),'ID':([2,],[3,]),'COLON':([3,],[4,]),'ENTERO':([4,],[6,]),'BOOLEANO':([4,],[7,]),'DECIMAL':([4,],[8,]),'CADENA':([4,],[9,]),'ARREGLO':([4,],[10,]),'SEMICOLON':([5,6,7,8,9,10,],[11,-2,-3,-4,-5,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'type_assignment':([0,],[1,]),'type':([4,],[5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> type_assignment","S'",1,None,None,None),
  ('type_assignment -> VAR ID COLON type SEMICOLON','type_assignment',5,'p_type_assignment','Parser.py',21),
  ('type -> ENTERO','type',1,'p_type','Parser.py',26),
  ('type -> BOOLEANO','type',1,'p_type','Parser.py',27),
  ('type -> DECIMAL','type',1,'p_type','Parser.py',28),
  ('type -> CADENA','type',1,'p_type','Parser.py',29),
  ('type -> ARREGLO','type',1,'p_type','Parser.py',30),
]
