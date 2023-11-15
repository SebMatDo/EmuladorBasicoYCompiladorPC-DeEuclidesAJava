
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocMENORMAYORleftSUMARESTAleftMULTDIVASIGNAR BOOLEANO CADENA CASO COLON COMA DECIMAL DEV DIFERENTE DIV ENTERO ENTONCES FALSO FFUN FMIENTRAS FUN GEQ HACER ID IGUAL LCORCHETE LEQ LPAREN MAYOR MENOR MIENTRAS MOD MULT NEGAR NULO NUMERO O PARAMETROS PCOMA RCORCHETE RESTA RPAREN SI SINO SUMA VAR VERDADERO Y\n        algoritmo : fun_sentencias proposicion proposiciones\n        | proposicion proposiciones\n        fun_sentencias : fun_senten fun_sentencias\n        | fun_senten\n        \n        proposiciones : proposicion proposiciones\n        | empty\n        \n        proposicion : DEV expresion\n        | asignacion PCOMA\n        | inicializar_variable PCOMA\n        \n        sec_proposiciones : proposicion sec_proposiciones\n        | proposicion\n        \n        asignacion : ID ASIGNAR expresion\n        \n        suma_resta : SUMA\n        | RESTA\n        \n        operador_relacional : IGUAL\n        | DIFERENTE\n        | LEQ\n        | GEQ\n        | MENOR\n        | MAYOR\n        \n        tipos : ENTERO\n        | BOOLEANO\n        | DECIMAL\n        | CADENA\n        \n        operador_terminal : operaciones factor operador_terminal\n        | empty\n        operaciones : MULT\n        | DIV\n        | MOD\n        | Y\n        | O\n        \n        termino : LPAREN termino RPAREN\n        | factor\n        | NEGAR termino\n        | factor operador_terminal\n        \n        terminos : suma_resta termino terminos\n        | termino terminos\n        | empty\n        \n        exp_simple : LPAREN exp_simple RPAREN\n        | suma_resta termino terminos\n        | termino terminos\n        | termino\n        \n        expresion : LPAREN expresion RPAREN\n        | exp_simple operador_relacional exp_simple\n        | exp_simple\n        | NEGAR expresion\n        \n        expresiones : COMA expresion expresiones\n        | empty\n        \n        conjunto : expresion\n        | expresion expresiones\n        \n        factor : ENTERO\n        | CADENA\n        | NULO\n        | ID\n        | DIFERENTE factor\n        | VERDADERO\n        | FALSO\n        | LPAREN expresion RPAREN\n        | conjunto\n        \n        bloque : sec_proposiciones\n        | empty\n        \n        def_funcion : FUN ID LPAREN asignar_tipos RPAREN\n        | FUN ID LPAREN asignar_tipos RPAREN DEV LPAREN asignar_tipos RPAREN\n        \n        fun_senten : def_funcion bloque FFUN\n        \n        asignar_tipos : ID COLON tipos coma_asignar_tipos\n        coma_asignar_tipos : COMA ID COLON tipos coma_asignar_tipos\n        | empty\n        \n        inicializar_variable : VAR ID COLON tipos\n        \n        lista_ids : LPAREN ID coma_ids RPAREN\n        coma_ids : COMA ID coma_ids\n        | empty\n        empty :'
    
_lr_action_items = {'DEV':([0,2,3,4,8,12,13,16,17,19,22,25,26,27,28,29,31,32,33,34,35,39,45,47,58,59,61,64,65,66,68,69,71,77,79,84,85,86,87,88,90,94,95,96,104,106,107,108,110,120,],[5,5,5,-4,5,5,5,-3,-7,-45,-42,-33,-51,-52,-53,-54,-56,-57,-59,-8,-9,5,-50,-48,-46,-34,-42,-49,-42,-41,-38,-35,-26,-33,-64,-49,-43,-39,-32,-44,-40,-37,-42,-33,-47,-43,-36,-25,112,-63,]),'ID':([0,2,3,4,5,8,10,11,12,13,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,39,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,104,105,106,107,108,110,114,116,120,],[9,9,9,-4,29,9,41,42,9,9,-3,-7,29,-45,29,29,29,-13,-14,-33,-51,-52,-53,-54,29,-56,-57,-59,-8,-9,9,29,-50,29,-48,-49,-45,29,29,-15,-16,-17,-18,-19,-20,-46,29,29,29,29,29,-49,29,-41,29,-38,-35,29,-26,-27,-28,-29,-30,-31,-33,29,-64,-49,102,-49,-43,-39,-32,-44,29,-40,29,-49,29,-37,29,-33,-47,29,-43,-36,-25,-62,117,102,-63,]),'VAR':([0,2,3,4,8,12,13,16,17,19,22,25,26,27,28,29,31,32,33,34,35,39,45,47,58,59,61,64,65,66,68,69,71,77,79,84,85,86,87,88,90,94,95,96,104,106,107,108,110,120,],[10,10,10,-4,10,10,10,-3,-7,-45,-42,-33,-51,-52,-53,-54,-56,-57,-59,-8,-9,10,-50,-48,-46,-34,-42,-49,-42,-41,-38,-35,-26,-33,-64,-49,-43,-39,-32,-44,-40,-37,-42,-33,-47,-43,-36,-25,-62,-63,]),'FUN':([0,4,79,],[11,11,-64,]),'$end':([1,3,12,13,14,15,17,19,22,25,26,27,28,29,31,32,33,34,35,43,44,45,47,58,59,61,64,65,66,68,69,71,77,84,85,86,87,88,90,94,95,96,104,106,107,108,],[0,-72,-72,-72,-2,-6,-7,-45,-42,-33,-51,-52,-53,-54,-56,-57,-59,-8,-9,-1,-5,-50,-48,-46,-34,-42,-49,-42,-41,-38,-35,-26,-33,-49,-43,-39,-32,-44,-40,-37,-42,-33,-47,-43,-36,-25,]),'LPAREN':([5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,40,42,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,84,85,86,87,88,89,90,91,92,93,94,95,96,104,105,106,107,108,112,],[18,-49,18,-45,60,62,62,-13,-14,-33,-51,-52,-53,-54,78,-56,-57,-59,18,83,-50,18,-48,-49,-45,62,89,-15,-16,-17,-18,-19,-20,-46,62,60,62,91,93,-49,62,-41,62,-38,-35,78,-26,-27,-28,-29,-30,-31,-33,18,-49,-49,-43,-39,-32,-44,105,-40,91,-49,91,-37,62,-33,-47,105,-43,-36,-25,116,]),'NEGAR':([5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,84,85,86,87,88,89,90,91,92,93,94,95,96,104,105,106,107,108,],[20,-49,20,-45,20,63,63,-13,-14,-33,-51,-52,-53,-54,20,-56,-57,-59,20,-50,20,-48,-49,-45,63,63,-15,-16,-17,-18,-19,-20,-46,63,20,63,63,63,-49,63,-41,63,-38,-35,20,-26,-27,-28,-29,-30,-31,-33,20,-49,-49,-43,-39,-32,-44,63,-40,63,-49,63,-37,63,-33,-47,63,-43,-36,-25,]),'SUMA':([5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,84,85,86,87,88,89,90,91,92,93,94,95,96,104,105,106,107,108,],[23,-49,23,-45,23,23,23,-13,-14,-33,-51,-52,-53,-54,23,-56,-57,-59,23,-50,23,-48,-49,-45,23,23,-15,-16,-17,-18,-19,-20,-46,23,23,23,23,23,-49,23,-41,23,-38,-35,23,-26,-27,-28,-29,-30,-31,-33,23,-49,-49,-43,-39,-32,-44,23,-40,23,-49,23,-37,23,-33,-47,23,-43,-36,-25,]),'RESTA':([5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,84,85,86,87,88,89,90,91,92,93,94,95,96,104,105,106,107,108,],[24,-49,24,-45,24,24,24,-13,-14,-33,-51,-52,-53,-54,24,-56,-57,-59,24,-50,24,-48,-49,-45,24,24,-15,-16,-17,-18,-19,-20,-46,24,24,24,24,24,-49,24,-41,24,-38,-35,24,-26,-27,-28,-29,-30,-31,-33,24,-49,-49,-43,-39,-32,-44,24,-40,24,-49,24,-37,24,-33,-47,24,-43,-36,-25,]),'ENTERO':([5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,104,105,106,107,108,109,119,],[26,-49,26,-45,26,26,26,-13,-14,-33,-51,-52,-53,-54,26,-56,-57,-59,26,-50,26,-48,-49,-45,26,26,-15,-16,-17,-18,-19,-20,-46,26,26,26,26,26,-49,26,-41,26,-38,-35,26,-26,-27,-28,-29,-30,-31,-33,26,-49,98,-49,-43,-39,-32,-44,26,-40,26,-49,26,-37,26,-33,-47,26,-43,-36,-25,98,98,]),'CADENA':([5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,104,105,106,107,108,109,119,],[27,-49,27,-45,27,27,27,-13,-14,-33,-51,-52,-53,-54,27,-56,-57,-59,27,-50,27,-48,-49,-45,27,27,-15,-16,-17,-18,-19,-20,-46,27,27,27,27,27,-49,27,-41,27,-38,-35,27,-26,-27,-28,-29,-30,-31,-33,27,-49,101,-49,-43,-39,-32,-44,27,-40,27,-49,27,-37,27,-33,-47,27,-43,-36,-25,101,101,]),'NULO':([5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,84,85,86,87,88,89,90,91,92,93,94,95,96,104,105,106,107,108,],[28,-49,28,-45,28,28,28,-13,-14,-33,-51,-52,-53,-54,28,-56,-57,-59,28,-50,28,-48,-49,-45,28,28,-15,-16,-17,-18,-19,-20,-46,28,28,28,28,28,-49,28,-41,28,-38,-35,28,-26,-27,-28,-29,-30,-31,-33,28,-49,-49,-43,-39,-32,-44,28,-40,28,-49,28,-37,28,-33,-47,28,-43,-36,-25,]),'DIFERENTE':([5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,84,85,86,87,88,89,90,91,92,93,94,95,96,104,105,106,107,108,],[30,-49,30,53,30,30,30,-13,-14,-33,-51,-52,-53,-54,30,-56,-57,-59,30,-50,30,-48,-49,53,30,30,-15,-16,-17,-18,-19,-20,-46,30,30,30,30,30,-49,30,-41,30,-38,-35,30,-26,-27,-28,-29,-30,-31,-33,30,-49,-49,-43,-39,-32,53,30,-40,30,-49,30,-37,30,-33,-47,30,-43,-36,-25,]),'VERDADERO':([5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,84,85,86,87,88,89,90,91,92,93,94,95,96,104,105,106,107,108,],[31,-49,31,-45,31,31,31,-13,-14,-33,-51,-52,-53,-54,31,-56,-57,-59,31,-50,31,-48,-49,-45,31,31,-15,-16,-17,-18,-19,-20,-46,31,31,31,31,31,-49,31,-41,31,-38,-35,31,-26,-27,-28,-29,-30,-31,-33,31,-49,-49,-43,-39,-32,-44,31,-40,31,-49,31,-37,31,-33,-47,31,-43,-36,-25,]),'FALSO':([5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,84,85,86,87,88,89,90,91,92,93,94,95,96,104,105,106,107,108,],[32,-49,32,-45,32,32,32,-13,-14,-33,-51,-52,-53,-54,32,-56,-57,-59,32,-50,32,-48,-49,-45,32,32,-15,-16,-17,-18,-19,-20,-46,32,32,32,32,32,-49,32,-41,32,-38,-35,32,-26,-27,-28,-29,-30,-31,-33,32,-49,-49,-43,-39,-32,-44,32,-40,32,-49,32,-37,32,-33,-47,32,-43,-36,-25,]),'PCOMA':([6,7,19,22,25,26,27,28,29,31,32,33,45,47,58,59,61,64,65,66,68,69,71,77,81,84,85,86,87,88,90,94,95,96,97,98,99,100,101,104,106,107,108,],[34,35,-45,-42,-33,-51,-52,-53,-54,-56,-57,-59,-50,-48,-46,-34,-42,-49,-42,-41,-38,-35,-26,-33,-12,-49,-43,-39,-32,-44,-40,-37,-42,-33,-68,-21,-22,-23,-24,-47,-43,-36,-25,]),'FFUN':([8,17,19,22,25,26,27,28,29,31,32,33,34,35,36,37,38,39,45,47,58,59,61,64,65,66,68,69,71,77,80,84,85,86,87,88,90,94,95,96,104,106,107,108,110,120,],[-72,-7,-45,-42,-33,-51,-52,-53,-54,-56,-57,-59,-8,-9,79,-60,-61,-11,-50,-48,-46,-34,-42,-49,-42,-41,-38,-35,-26,-33,-10,-49,-43,-39,-32,-44,-40,-37,-42,-33,-47,-43,-36,-25,-62,-63,]),'ASIGNAR':([9,],[40,]),'COMA':([17,19,22,25,26,27,28,29,31,32,33,45,47,48,49,50,58,59,61,64,65,66,68,69,71,77,81,84,85,86,87,88,90,92,94,95,96,98,99,100,101,104,106,107,108,111,121,],[46,-45,-42,-33,-51,-52,-53,-54,-56,-57,-59,-50,-48,46,-45,-42,46,-34,-42,46,-42,-41,-38,-35,-26,-33,46,46,-43,-39,-32,-44,-40,46,-37,-42,-33,-21,-22,-23,-24,-47,-43,-36,-25,114,114,]),'MULT':([17,19,22,25,26,27,28,29,31,32,33,45,47,48,49,50,58,59,61,64,65,66,68,69,71,77,81,84,85,86,87,88,90,92,94,95,96,104,106,107,108,],[-49,-45,-42,72,-51,-52,-53,-54,-56,-57,-59,-50,-48,-49,-45,-42,-46,-34,-42,-49,-42,-41,-38,-35,-26,72,-49,-49,-43,-39,-32,-44,-40,-49,-37,-42,72,-47,-43,-36,-25,]),'DIV':([17,19,22,25,26,27,28,29,31,32,33,45,47,48,49,50,58,59,61,64,65,66,68,69,71,77,81,84,85,86,87,88,90,92,94,95,96,104,106,107,108,],[-49,-45,-42,73,-51,-52,-53,-54,-56,-57,-59,-50,-48,-49,-45,-42,-46,-34,-42,-49,-42,-41,-38,-35,-26,73,-49,-49,-43,-39,-32,-44,-40,-49,-37,-42,73,-47,-43,-36,-25,]),'MOD':([17,19,22,25,26,27,28,29,31,32,33,45,47,48,49,50,58,59,61,64,65,66,68,69,71,77,81,84,85,86,87,88,90,92,94,95,96,104,106,107,108,],[-49,-45,-42,74,-51,-52,-53,-54,-56,-57,-59,-50,-48,-49,-45,-42,-46,-34,-42,-49,-42,-41,-38,-35,-26,74,-49,-49,-43,-39,-32,-44,-40,-49,-37,-42,74,-47,-43,-36,-25,]),'Y':([17,19,22,25,26,27,28,29,31,32,33,45,47,48,49,50,58,59,61,64,65,66,68,69,71,77,81,84,85,86,87,88,90,92,94,95,96,104,106,107,108,],[-49,-45,-42,75,-51,-52,-53,-54,-56,-57,-59,-50,-48,-49,-45,-42,-46,-34,-42,-49,-42,-41,-38,-35,-26,75,-49,-49,-43,-39,-32,-44,-40,-49,-37,-42,75,-47,-43,-36,-25,]),'O':([17,19,22,25,26,27,28,29,31,32,33,45,47,48,49,50,58,59,61,64,65,66,68,69,71,77,81,84,85,86,87,88,90,92,94,95,96,104,106,107,108,],[-49,-45,-42,76,-51,-52,-53,-54,-56,-57,-59,-50,-48,-49,-45,-42,-46,-34,-42,-49,-42,-41,-38,-35,-26,76,-49,-49,-43,-39,-32,-44,-40,-49,-37,-42,76,-47,-43,-36,-25,]),'IGUAL':([17,19,22,25,26,27,28,29,31,32,33,45,47,48,49,50,58,59,61,64,65,66,68,69,71,77,81,84,85,86,87,88,90,92,94,95,96,104,106,107,108,],[-49,52,-42,-33,-51,-52,-53,-54,-56,-57,-59,-50,-48,-49,52,-42,-46,-34,-42,-49,-42,-41,-38,-35,-26,-33,-49,-49,-43,-39,-32,52,-40,-49,-37,-42,-33,-47,-43,-36,-25,]),'LEQ':([17,19,22,25,26,27,28,29,31,32,33,45,47,48,49,50,58,59,61,64,65,66,68,69,71,77,81,84,85,86,87,88,90,92,94,95,96,104,106,107,108,],[-49,54,-42,-33,-51,-52,-53,-54,-56,-57,-59,-50,-48,-49,54,-42,-46,-34,-42,-49,-42,-41,-38,-35,-26,-33,-49,-49,-43,-39,-32,54,-40,-49,-37,-42,-33,-47,-43,-36,-25,]),'GEQ':([17,19,22,25,26,27,28,29,31,32,33,45,47,48,49,50,58,59,61,64,65,66,68,69,71,77,81,84,85,86,87,88,90,92,94,95,96,104,106,107,108,],[-49,55,-42,-33,-51,-52,-53,-54,-56,-57,-59,-50,-48,-49,55,-42,-46,-34,-42,-49,-42,-41,-38,-35,-26,-33,-49,-49,-43,-39,-32,55,-40,-49,-37,-42,-33,-47,-43,-36,-25,]),'MENOR':([17,19,22,25,26,27,28,29,31,32,33,45,47,48,49,50,58,59,61,64,65,66,68,69,71,77,81,84,85,86,87,88,90,92,94,95,96,104,106,107,108,],[-49,56,-42,-33,-51,-52,-53,-54,-56,-57,-59,-50,-48,-49,56,-42,-46,-34,-42,-49,-42,-41,-38,-35,-26,-33,-49,-49,-43,-39,-32,56,-40,-49,-37,-42,-33,-47,-43,-36,-25,]),'MAYOR':([17,19,22,25,26,27,28,29,31,32,33,45,47,48,49,50,58,59,61,64,65,66,68,69,71,77,81,84,85,86,87,88,90,92,94,95,96,104,106,107,108,],[-49,57,-42,-33,-51,-52,-53,-54,-56,-57,-59,-50,-48,-49,57,-42,-46,-34,-42,-49,-42,-41,-38,-35,-26,-33,-49,-49,-43,-39,-32,57,-40,-49,-37,-42,-33,-47,-43,-36,-25,]),'RPAREN':([19,22,25,26,27,28,29,31,32,33,45,47,48,49,50,58,59,61,64,65,66,68,69,71,77,84,85,86,87,88,90,92,94,95,96,98,99,100,101,103,104,106,107,108,111,113,115,118,121,122,],[-45,-42,-33,-51,-52,-53,-54,-56,-57,-59,-50,-48,85,86,87,-46,-34,-42,-49,-42,-41,-38,-35,-26,-33,-49,-43,-39,-32,-44,-40,106,-37,-42,-33,-21,-22,-23,-24,110,-47,-43,-36,-25,-72,-65,-67,120,-72,-66,]),'COLON':([41,102,117,],[82,109,119,]),'BOOLEANO':([82,109,119,],[99,99,99,]),'DECIMAL':([82,109,119,],[100,100,100,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'algoritmo':([0,],[1,]),'fun_sentencias':([0,4,],[2,16,]),'proposicion':([0,2,3,8,12,13,39,],[3,12,13,39,13,13,39,]),'fun_senten':([0,4,],[4,4,]),'asignacion':([0,2,3,8,12,13,39,],[6,6,6,6,6,6,6,]),'inicializar_variable':([0,2,3,8,12,13,39,],[7,7,7,7,7,7,7,]),'def_funcion':([0,4,],[8,8,]),'proposiciones':([3,12,13,],[14,43,44,]),'empty':([3,8,12,13,17,22,25,48,50,58,59,61,64,65,77,81,84,92,95,96,111,121,],[15,38,15,15,47,68,71,47,68,47,68,68,47,68,71,47,47,47,68,71,115,115,]),'expresion':([5,18,20,21,22,30,40,46,50,51,59,60,61,62,63,65,67,70,78,89,91,93,95,105,],[17,48,58,64,64,64,81,84,64,64,64,48,64,92,58,64,64,64,92,92,48,48,64,48,]),'exp_simple':([5,18,20,21,22,30,40,46,50,51,59,60,61,62,63,65,67,70,78,89,91,93,95,105,],[19,49,19,19,19,19,19,19,19,88,19,49,19,49,19,19,19,19,49,49,49,49,19,49,]),'suma_resta':([5,18,20,21,22,30,40,46,50,51,59,60,61,62,63,65,67,70,78,89,91,93,95,105,],[21,21,21,21,67,21,21,21,67,21,67,21,67,21,21,67,21,21,21,21,21,21,67,21,]),'termino':([5,18,20,21,22,30,40,46,50,51,59,60,61,62,63,65,67,70,78,89,91,93,95,105,],[22,50,59,61,65,22,22,22,65,22,65,50,65,50,59,65,95,22,50,50,50,50,65,50,]),'factor':([5,18,20,21,22,30,40,46,50,51,59,60,61,62,63,65,67,70,78,89,91,93,95,105,],[25,25,25,25,25,77,25,25,25,25,25,25,25,25,25,25,25,96,25,25,25,25,25,25,]),'conjunto':([5,18,20,21,22,30,40,46,50,51,59,60,61,62,63,65,67,70,78,89,91,93,95,105,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'bloque':([8,],[36,]),'sec_proposiciones':([8,39,],[37,80,]),'expresiones':([17,48,58,64,81,84,92,],[45,45,45,45,45,104,45,]),'operador_relacional':([19,49,88,],[51,51,51,]),'terminos':([22,50,59,61,65,95,],[66,66,66,90,94,107,]),'operador_terminal':([25,77,96,],[69,69,108,]),'operaciones':([25,77,96,],[70,70,70,]),'tipos':([82,109,119,],[97,111,121,]),'asignar_tipos':([83,116,],[103,118,]),'coma_asignar_tipos':([111,121,],[113,122,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> algoritmo","S'",1,None,None,None),
  ('algoritmo -> fun_sentencias proposicion proposiciones','algoritmo',3,'p_algoritmo','Parser.py',29),
  ('algoritmo -> proposicion proposiciones','algoritmo',2,'p_algoritmo','Parser.py',30),
  ('fun_sentencias -> fun_senten fun_sentencias','fun_sentencias',2,'p_algoritmo','Parser.py',31),
  ('fun_sentencias -> fun_senten','fun_sentencias',1,'p_algoritmo','Parser.py',32),
  ('proposiciones -> proposicion proposiciones','proposiciones',2,'p_proposiciones','Parser.py',40),
  ('proposiciones -> empty','proposiciones',1,'p_proposiciones','Parser.py',41),
  ('proposicion -> DEV expresion','proposicion',2,'p_proposicion','Parser.py',47),
  ('proposicion -> asignacion PCOMA','proposicion',2,'p_proposicion','Parser.py',48),
  ('proposicion -> inicializar_variable PCOMA','proposicion',2,'p_proposicion','Parser.py',49),
  ('sec_proposiciones -> proposicion sec_proposiciones','sec_proposiciones',2,'p_sec_proposiciones','Parser.py',55),
  ('sec_proposiciones -> proposicion','sec_proposiciones',1,'p_sec_proposiciones','Parser.py',56),
  ('asignacion -> ID ASIGNAR expresion','asignacion',3,'p_asignacion','Parser.py',62),
  ('suma_resta -> SUMA','suma_resta',1,'p_suma_resta','Parser.py',69),
  ('suma_resta -> RESTA','suma_resta',1,'p_suma_resta','Parser.py',70),
  ('operador_relacional -> IGUAL','operador_relacional',1,'p_operador_relacional','Parser.py',76),
  ('operador_relacional -> DIFERENTE','operador_relacional',1,'p_operador_relacional','Parser.py',77),
  ('operador_relacional -> LEQ','operador_relacional',1,'p_operador_relacional','Parser.py',78),
  ('operador_relacional -> GEQ','operador_relacional',1,'p_operador_relacional','Parser.py',79),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_operador_relacional','Parser.py',80),
  ('operador_relacional -> MAYOR','operador_relacional',1,'p_operador_relacional','Parser.py',81),
  ('tipos -> ENTERO','tipos',1,'p_tipos','Parser.py',87),
  ('tipos -> BOOLEANO','tipos',1,'p_tipos','Parser.py',88),
  ('tipos -> DECIMAL','tipos',1,'p_tipos','Parser.py',89),
  ('tipos -> CADENA','tipos',1,'p_tipos','Parser.py',90),
  ('operador_terminal -> operaciones factor operador_terminal','operador_terminal',3,'p_operador_terminal','Parser.py',97),
  ('operador_terminal -> empty','operador_terminal',1,'p_operador_terminal','Parser.py',98),
  ('operaciones -> MULT','operaciones',1,'p_operador_terminal','Parser.py',99),
  ('operaciones -> DIV','operaciones',1,'p_operador_terminal','Parser.py',100),
  ('operaciones -> MOD','operaciones',1,'p_operador_terminal','Parser.py',101),
  ('operaciones -> Y','operaciones',1,'p_operador_terminal','Parser.py',102),
  ('operaciones -> O','operaciones',1,'p_operador_terminal','Parser.py',103),
  ('termino -> LPAREN termino RPAREN','termino',3,'p_termino','Parser.py',111),
  ('termino -> factor','termino',1,'p_termino','Parser.py',112),
  ('termino -> NEGAR termino','termino',2,'p_termino','Parser.py',113),
  ('termino -> factor operador_terminal','termino',2,'p_termino','Parser.py',114),
  ('terminos -> suma_resta termino terminos','terminos',3,'p_terminos','Parser.py',121),
  ('terminos -> termino terminos','terminos',2,'p_terminos','Parser.py',122),
  ('terminos -> empty','terminos',1,'p_terminos','Parser.py',123),
  ('exp_simple -> LPAREN exp_simple RPAREN','exp_simple',3,'p_exp_simple','Parser.py',129),
  ('exp_simple -> suma_resta termino terminos','exp_simple',3,'p_exp_simple','Parser.py',130),
  ('exp_simple -> termino terminos','exp_simple',2,'p_exp_simple','Parser.py',131),
  ('exp_simple -> termino','exp_simple',1,'p_exp_simple','Parser.py',132),
  ('expresion -> LPAREN expresion RPAREN','expresion',3,'p_expresion','Parser.py',138),
  ('expresion -> exp_simple operador_relacional exp_simple','expresion',3,'p_expresion','Parser.py',139),
  ('expresion -> exp_simple','expresion',1,'p_expresion','Parser.py',140),
  ('expresion -> NEGAR expresion','expresion',2,'p_expresion','Parser.py',141),
  ('expresiones -> COMA expresion expresiones','expresiones',3,'p_expresiones','Parser.py',148),
  ('expresiones -> empty','expresiones',1,'p_expresiones','Parser.py',149),
  ('conjunto -> expresion','conjunto',1,'p_conjunto','Parser.py',155),
  ('conjunto -> expresion expresiones','conjunto',2,'p_conjunto','Parser.py',156),
  ('factor -> ENTERO','factor',1,'p_factor','Parser.py',162),
  ('factor -> CADENA','factor',1,'p_factor','Parser.py',163),
  ('factor -> NULO','factor',1,'p_factor','Parser.py',164),
  ('factor -> ID','factor',1,'p_factor','Parser.py',165),
  ('factor -> DIFERENTE factor','factor',2,'p_factor','Parser.py',166),
  ('factor -> VERDADERO','factor',1,'p_factor','Parser.py',167),
  ('factor -> FALSO','factor',1,'p_factor','Parser.py',168),
  ('factor -> LPAREN expresion RPAREN','factor',3,'p_factor','Parser.py',169),
  ('factor -> conjunto','factor',1,'p_factor','Parser.py',170),
  ('bloque -> sec_proposiciones','bloque',1,'p_bloque','Parser.py',178),
  ('bloque -> empty','bloque',1,'p_bloque','Parser.py',179),
  ('def_funcion -> FUN ID LPAREN asignar_tipos RPAREN','def_funcion',5,'p_def_funcion','Parser.py',185),
  ('def_funcion -> FUN ID LPAREN asignar_tipos RPAREN DEV LPAREN asignar_tipos RPAREN','def_funcion',9,'p_def_funcion','Parser.py',186),
  ('fun_senten -> def_funcion bloque FFUN','fun_senten',3,'p_fun_senten','Parser.py',193),
  ('asignar_tipos -> ID COLON tipos coma_asignar_tipos','asignar_tipos',4,'p_asignar_tipos','Parser.py',199),
  ('coma_asignar_tipos -> COMA ID COLON tipos coma_asignar_tipos','coma_asignar_tipos',5,'p_asignar_tipos','Parser.py',200),
  ('coma_asignar_tipos -> empty','coma_asignar_tipos',1,'p_asignar_tipos','Parser.py',201),
  ('inicializar_variable -> VAR ID COLON tipos','inicializar_variable',4,'p_inicializar_variable','Parser.py',209),
  ('lista_ids -> LPAREN ID coma_ids RPAREN','lista_ids',4,'p_lista_ids','Parser.py',216),
  ('coma_ids -> COMA ID coma_ids','coma_ids',3,'p_lista_ids','Parser.py',217),
  ('coma_ids -> empty','coma_ids',1,'p_lista_ids','Parser.py',218),
  ('empty -> <empty>','empty',0,'p_empty','Parser.py',225),
]
