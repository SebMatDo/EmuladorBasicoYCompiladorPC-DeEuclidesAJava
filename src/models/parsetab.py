
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocMENORMAYORleftSUMARESTAleftMULTDIVleftPOTENCIAASIGNAR BOOLEANO CADENA CASO COLON DECIMAL DIFERENTE DIV ENTERO ENTONCES ESCRIBIR FALSO FFUN FMIENTRAS FSI FUN GEQ HACER ID IGUAL LEER LEQ LPAREN MAYOR MENOR MIENTRAS MOD MULT NEGAR NULO NUM_DECIMAL NUM_ENTERO O PCOMA POTENCIA RESTA RPAREN SI SINO SUMA VALOR_CADENA VAR VERDADERO Y\n        algoritmo : FUN proposicion proposiciones FFUN\n        empty :\n        proposicion : asignacion PCOMA\n        | inicializar_variable PCOMA\n        | sentencia_si PCOMA\n        | sentencia_mientras PCOMA\n        | sentencia_hacer_mientras PCOMA\n        | sentencia_leer PCOMA\n        | sentencia_escribir PCOMA\n\n        \n        proposiciones : proposicion proposiciones\n        | empty\n        \n        asignacion : ID ASIGNAR ID\n        | ID ASIGNAR exp_aritmetica\n        | ID ASIGNAR exp_booleana\n        | ID ASIGNAR NULO\n        | ID ASIGNAR VALOR_CADENA\n        \n        tipos : ENTERO\n        | BOOLEANO\n        | DECIMAL\n        | CADENA\n        \n        inicializar_variable : VAR ID COLON tipos\n        \n        operador_aritmetico : MULT\n        | DIV\n        | SUMA\n        | RESTA\n        | POTENCIA\n        \n        factor_aritmetico : LPAREN exp_aritmetica RPAREN\n        | NUM_ENTERO\n        | NUM_DECIMAL\n        factor_aritmetico_id : factor_aritmetico\n        | ID\n        \n        operaciones_aritmeticas : operador_aritmetico factor_aritmetico operaciones_aritmeticas\n        | empty\n        \n        operaciones_aritmeticas_id : operador_aritmetico factor_aritmetico_id operaciones_aritmeticas_id\n        | operador_aritmetico factor_aritmetico_id\n        \n        termino_aritmetico : factor_aritmetico operaciones_aritmeticas\n        | ID operaciones_aritmeticas_id\n        | factor_aritmetico operaciones_aritmeticas_id\n        \n        exp_aritmetica : termino_aritmetico\n        | termino_aritmetico operador_aritmetico exp_aritmetica\n        \n        operador_relacional : IGUAL\n        | DIFERENTE\n        | LEQ\n        | GEQ\n        | MENOR\n        | MAYOR\n        \n        factor_relacional : LPAREN factor_relacional RPAREN\n        | exp_aritmetica operador_relacional exp_aritmetica\n        | ID operador_relacional exp_aritmetica\n        | exp_aritmetica operador_relacional ID\n        | ID operador_relacional ID\n        \n        operador_booleano : IGUAL\n        | DIFERENTE\n        | Y\n        | O\n        \n        factor_booleano : LPAREN exp_booleana RPAREN\n        | VERDADERO\n        | FALSO\n        | factor_relacional\n        | NEGAR factor_booleano\n        factor_booleano_id : factor_booleano\n        | ID\n        | NEGAR ID\n        \n        operaciones_booleanas : operador_booleano factor_booleano operaciones_booleanas\n        | empty\n        operaciones_booleanas_id : operador_booleano factor_booleano_id operaciones_booleanas_id\n        | empty\n        \n        termino_booleano : factor_booleano operaciones_booleanas\n        | ID operador_booleano factor_booleano_id operaciones_booleanas_id\n        | NEGAR ID operaciones_booleanas_id\n        \n        exp_booleana : termino_booleano\n        | termino_booleano operador_booleano exp_booleana\n        \n        sentencia_si : SI exp_booleana ENTONCES proposicion proposiciones FSI\n        | SI exp_booleana ENTONCES proposicion proposiciones SINO proposicion proposiciones FSI\n        \n        sentencia_mientras : MIENTRAS exp_booleana HACER proposicion proposiciones FMIENTRAS\n        \n        sentencia_hacer_mientras : HACER proposicion proposiciones MIENTRAS exp_booleana\n        \n        sentencia_leer : LEER LPAREN ID RPAREN\n        \n        sentencia_escribir :  ESCRIBIR LPAREN ID RPAREN\n        '
    
_lr_action_items = {'FUN':([0,],[2,]),'$end':([1,49,],[0,-1,]),'ID':([2,3,12,13,14,15,18,21,22,23,24,25,26,27,28,34,35,45,46,47,55,57,58,59,60,61,62,64,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,84,89,90,91,92,95,97,101,108,115,118,123,125,126,135,136,151,155,],[11,11,29,33,33,11,11,-3,-4,-5,-6,-7,-8,-9,50,82,88,11,99,100,102,11,33,-52,-53,-54,-55,111,112,116,-41,-42,-43,-44,-45,-46,121,-22,-23,-24,-25,-26,111,88,131,-41,-42,133,121,11,102,11,142,133,112,-41,-42,11,33,11,11,]),'VAR':([2,3,15,18,21,22,23,24,25,26,27,45,57,97,108,135,151,155,],[12,12,12,12,-3,-4,-5,-6,-7,-8,-9,12,12,12,12,12,12,12,]),'SI':([2,3,15,18,21,22,23,24,25,26,27,45,57,97,108,135,151,155,],[13,13,13,13,-3,-4,-5,-6,-7,-8,-9,13,13,13,13,13,13,13,]),'MIENTRAS':([2,3,15,18,20,21,22,23,24,25,26,27,45,48,57,97,98,108,135,151,155,],[14,14,14,14,-11,-3,-4,-5,-6,-7,-8,-9,14,-10,14,14,136,14,14,14,14,]),'HACER':([2,3,15,18,21,22,23,24,25,26,27,31,32,36,37,38,40,41,42,43,44,45,57,63,65,68,82,83,93,94,96,97,108,109,110,112,113,114,116,117,119,120,121,122,124,127,128,129,130,131,132,134,135,140,141,142,144,145,147,151,152,153,155,],[15,15,15,15,-3,-4,-5,-6,-7,-8,-9,-71,-2,-57,-58,-59,-39,-2,-28,-29,97,15,15,-68,-65,-37,-2,-60,-36,-38,-33,15,15,-72,-2,-62,-2,-61,-51,-49,-35,-30,-31,-70,-67,-56,-47,-27,-48,-50,-40,-2,15,-64,-69,-63,-34,-2,-32,15,-66,-2,15,]),'LEER':([2,3,15,18,21,22,23,24,25,26,27,45,57,97,108,135,151,155,],[16,16,16,16,-3,-4,-5,-6,-7,-8,-9,16,16,16,16,16,16,16,]),'ESCRIBIR':([2,3,15,18,21,22,23,24,25,26,27,45,57,97,108,135,151,155,],[17,17,17,17,-3,-4,-5,-6,-7,-8,-9,17,17,17,17,17,17,17,]),'FFUN':([3,18,19,20,21,22,23,24,25,26,27,48,],[-2,-2,49,-11,-3,-4,-5,-6,-7,-8,-9,-10,]),'PCOMA':([4,5,6,7,8,9,10,31,32,36,37,38,40,41,42,43,50,51,52,53,54,63,65,68,82,83,93,94,96,103,104,105,106,107,109,110,112,113,114,116,117,119,120,121,122,124,127,128,129,130,131,132,134,137,138,140,141,142,144,145,147,149,150,152,153,154,157,],[21,22,23,24,25,26,27,-71,-2,-57,-58,-59,-39,-2,-28,-29,-12,-13,-14,-15,-16,-68,-65,-37,-2,-60,-36,-38,-33,-21,-17,-18,-19,-20,-72,-2,-62,-2,-61,-51,-49,-35,-30,-31,-70,-67,-56,-47,-27,-48,-50,-40,-2,-77,-78,-64,-69,-63,-34,-2,-32,-76,-73,-66,-2,-75,-74,]),'ASIGNAR':([11,],[28,]),'NEGAR':([13,14,28,34,35,55,58,59,60,61,62,64,66,69,70,81,84,101,115,123,125,126,136,],[34,34,34,81,34,34,34,-52,-53,-54,-55,81,115,-52,-53,81,34,34,81,115,-52,-53,34,]),'LPAREN':([13,14,16,17,28,34,35,55,58,59,60,61,62,64,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,84,89,90,91,92,95,101,115,118,123,125,126,136,146,],[35,35,46,47,55,35,84,101,35,-52,-53,-54,-55,35,35,118,-41,-42,-43,-44,-45,-46,118,-22,-23,-24,-25,-26,35,84,118,-41,-42,118,118,101,35,118,35,-41,-42,35,118,]),'VERDADERO':([13,14,28,34,35,55,58,59,60,61,62,64,66,69,70,81,84,101,115,123,125,126,136,],[36,36,36,36,36,36,36,-52,-53,-54,-55,36,36,-52,-53,36,36,36,36,36,-52,-53,36,]),'FALSO':([13,14,28,34,35,55,58,59,60,61,62,64,66,69,70,81,84,101,115,123,125,126,136,],[37,37,37,37,37,37,37,-52,-53,-54,-55,37,37,-52,-53,37,37,37,37,37,-52,-53,37,]),'NUM_ENTERO':([13,14,28,34,35,55,58,59,60,61,62,64,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,84,89,90,91,92,95,101,115,118,123,125,126,136,146,],[42,42,42,42,42,42,42,-52,-53,-54,-55,42,42,42,-41,-42,-43,-44,-45,-46,42,-22,-23,-24,-25,-26,42,42,42,-41,-42,42,42,42,42,42,42,-41,-42,42,42,]),'NUM_DECIMAL':([13,14,28,34,35,55,58,59,60,61,62,64,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,84,89,90,91,92,95,101,115,118,123,125,126,136,146,],[43,43,43,43,43,43,43,-52,-53,-54,-55,43,43,43,-41,-42,-43,-44,-45,-46,43,-22,-23,-24,-25,-26,43,43,43,-41,-42,43,43,43,43,43,43,-41,-42,43,43,]),'FSI':([18,20,21,22,23,24,25,26,27,48,108,139,155,156,],[-2,-11,-3,-4,-5,-6,-7,-8,-9,-10,-2,150,-2,157,]),'SINO':([18,20,21,22,23,24,25,26,27,48,108,139,],[-2,-11,-3,-4,-5,-6,-7,-8,-9,-10,-2,151,]),'FMIENTRAS':([18,20,21,22,23,24,25,26,27,48,135,148,],[-2,-11,-3,-4,-5,-6,-7,-8,-9,-10,-2,154,]),'NULO':([28,],[53,]),'VALOR_CADENA':([28,],[54,]),'COLON':([29,],[56,]),'ENTONCES':([30,31,32,36,37,38,40,41,42,43,63,65,68,82,83,93,94,96,109,110,112,113,114,116,117,119,120,121,122,124,127,128,129,130,131,132,134,140,141,142,144,145,147,152,153,],[57,-71,-2,-57,-58,-59,-39,-2,-28,-29,-68,-65,-37,-2,-60,-36,-38,-33,-72,-2,-62,-2,-61,-51,-49,-35,-30,-31,-70,-67,-56,-47,-27,-48,-50,-40,-2,-64,-69,-63,-34,-2,-32,-66,-2,]),'RPAREN':([31,32,36,37,38,40,41,42,43,63,65,68,82,83,85,86,87,93,94,96,99,100,109,110,112,113,114,116,117,119,120,121,122,124,127,128,129,130,131,132,134,140,141,142,143,144,145,147,152,153,],[-71,-2,-57,-58,-59,-39,-2,-28,-29,-68,-65,-37,-2,-60,127,128,129,-36,-38,-33,137,138,-72,-2,-62,-2,-61,-51,-49,-35,-30,-31,-70,-67,-56,-47,-27,-48,-50,-40,-2,-64,-69,-63,129,-34,-2,-32,-66,-2,]),'IGUAL':([31,32,33,36,37,38,39,40,41,42,43,50,51,63,65,68,82,83,86,87,88,93,94,96,102,110,111,112,113,114,116,117,119,120,121,122,124,127,128,129,130,131,132,134,140,141,142,144,145,147,152,153,],[59,59,69,-57,-58,-59,90,-39,-2,-28,-29,69,90,-68,-65,-37,125,-60,-59,90,125,-36,-38,-33,125,59,90,90,59,-61,-51,-49,-35,-30,-31,-70,-67,-56,-47,-27,-48,-50,-40,-2,-64,-69,90,-34,59,-32,-66,-2,]),'DIFERENTE':([31,32,33,36,37,38,39,40,41,42,43,50,51,63,65,68,82,83,86,87,88,93,94,96,102,110,111,112,113,114,116,117,119,120,121,122,124,127,128,129,130,131,132,134,140,141,142,144,145,147,152,153,],[60,60,70,-57,-58,-59,91,-39,-2,-28,-29,70,91,-68,-65,-37,126,-60,-59,91,126,-36,-38,-33,126,60,91,91,60,-61,-51,-49,-35,-30,-31,-70,-67,-56,-47,-27,-48,-50,-40,-2,-64,-69,91,-34,60,-32,-66,-2,]),'Y':([31,32,33,36,37,38,40,41,42,43,50,63,65,68,82,83,86,88,93,94,96,102,110,112,113,114,116,117,119,120,121,122,124,127,128,129,130,131,132,134,140,141,142,144,145,147,152,153,],[61,61,61,-57,-58,-59,-39,-2,-28,-29,61,-68,-65,-37,61,-60,-59,61,-36,-38,-33,61,61,-62,61,-61,-51,-49,-35,-30,-31,-70,-67,-56,-47,-27,-48,-50,-40,-2,-64,-69,-63,-34,61,-32,-66,-2,]),'O':([31,32,33,36,37,38,40,41,42,43,50,63,65,68,82,83,86,88,93,94,96,102,110,112,113,114,116,117,119,120,121,122,124,127,128,129,130,131,132,134,140,141,142,144,145,147,152,153,],[62,62,62,-57,-58,-59,-39,-2,-28,-29,62,-68,-65,-37,62,-60,-59,62,-36,-38,-33,62,62,-62,62,-61,-51,-49,-35,-30,-31,-70,-67,-56,-47,-27,-48,-50,-40,-2,-64,-69,-63,-34,62,-32,-66,-2,]),'LEQ':([33,39,40,41,42,43,50,51,68,82,87,88,93,94,96,102,111,112,119,120,121,129,132,134,142,144,147,153,],[71,71,-39,-2,-28,-29,71,71,-37,71,71,71,-36,-38,-33,71,71,71,-35,-30,-31,-27,-40,-2,71,-34,-32,-2,]),'GEQ':([33,39,40,41,42,43,50,51,68,82,87,88,93,94,96,102,111,112,119,120,121,129,132,134,142,144,147,153,],[72,72,-39,-2,-28,-29,72,72,-37,72,72,72,-36,-38,-33,72,72,72,-35,-30,-31,-27,-40,-2,72,-34,-32,-2,]),'MENOR':([33,39,40,41,42,43,50,51,68,82,87,88,93,94,96,102,111,112,119,120,121,129,132,134,142,144,147,153,],[73,73,-39,-2,-28,-29,73,73,-37,73,73,73,-36,-38,-33,73,73,73,-35,-30,-31,-27,-40,-2,73,-34,-32,-2,]),'MAYOR':([33,39,40,41,42,43,50,51,68,82,87,88,93,94,96,102,111,112,119,120,121,129,132,134,142,144,147,153,],[74,74,-39,-2,-28,-29,74,74,-37,74,74,74,-36,-38,-33,74,74,74,-35,-30,-31,-27,-40,-2,74,-34,-32,-2,]),'MULT':([33,40,41,42,43,50,68,82,88,93,94,96,102,111,112,116,119,120,121,129,131,133,134,142,144,147,153,],[76,76,76,-28,-29,76,-37,76,76,-36,-38,-33,76,76,76,76,76,-30,-31,-27,76,76,76,76,-34,-32,76,]),'DIV':([33,40,41,42,43,50,68,82,88,93,94,96,102,111,112,116,119,120,121,129,131,133,134,142,144,147,153,],[77,77,77,-28,-29,77,-37,77,77,-36,-38,-33,77,77,77,77,77,-30,-31,-27,77,77,77,77,-34,-32,77,]),'SUMA':([33,40,41,42,43,50,68,82,88,93,94,96,102,111,112,116,119,120,121,129,131,133,134,142,144,147,153,],[78,78,78,-28,-29,78,-37,78,78,-36,-38,-33,78,78,78,78,78,-30,-31,-27,78,78,78,78,-34,-32,78,]),'RESTA':([33,40,41,42,43,50,68,82,88,93,94,96,102,111,112,116,119,120,121,129,131,133,134,142,144,147,153,],[79,79,79,-28,-29,79,-37,79,79,-36,-38,-33,79,79,79,79,79,-30,-31,-27,79,79,79,79,-34,-32,79,]),'POTENCIA':([33,40,41,42,43,50,68,82,88,93,94,96,102,111,112,116,119,120,121,129,131,133,134,142,144,147,153,],[80,80,80,-28,-29,80,-37,80,80,-36,-38,-33,80,80,80,80,80,-30,-31,-27,80,80,80,80,-34,-32,80,]),'ENTERO':([56,],[104,]),'BOOLEANO':([56,],[105,]),'DECIMAL':([56,],[106,]),'CADENA':([56,],[107,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'algoritmo':([0,],[1,]),'proposicion':([2,3,15,18,45,57,97,108,135,151,155,],[3,18,45,18,18,108,135,18,18,155,18,]),'asignacion':([2,3,15,18,45,57,97,108,135,151,155,],[4,4,4,4,4,4,4,4,4,4,4,]),'inicializar_variable':([2,3,15,18,45,57,97,108,135,151,155,],[5,5,5,5,5,5,5,5,5,5,5,]),'sentencia_si':([2,3,15,18,45,57,97,108,135,151,155,],[6,6,6,6,6,6,6,6,6,6,6,]),'sentencia_mientras':([2,3,15,18,45,57,97,108,135,151,155,],[7,7,7,7,7,7,7,7,7,7,7,]),'sentencia_hacer_mientras':([2,3,15,18,45,57,97,108,135,151,155,],[8,8,8,8,8,8,8,8,8,8,8,]),'sentencia_leer':([2,3,15,18,45,57,97,108,135,151,155,],[9,9,9,9,9,9,9,9,9,9,9,]),'sentencia_escribir':([2,3,15,18,45,57,97,108,135,151,155,],[10,10,10,10,10,10,10,10,10,10,10,]),'proposiciones':([3,18,45,108,135,155,],[19,48,98,139,148,156,]),'empty':([3,18,32,41,45,82,108,110,113,134,135,145,153,155,],[20,20,65,96,20,124,20,65,124,96,20,124,96,20,]),'exp_booleana':([13,14,28,35,55,58,84,101,136,],[30,44,52,85,85,109,85,85,149,]),'termino_booleano':([13,14,28,35,55,58,84,101,136,],[31,31,31,31,31,31,31,31,31,]),'factor_booleano':([13,14,28,34,35,55,58,64,66,81,84,101,115,123,136,],[32,32,32,83,32,32,32,110,114,83,32,32,83,114,32,]),'factor_relacional':([13,14,28,34,35,55,58,64,66,81,84,101,115,123,136,],[38,38,38,38,86,86,38,38,38,38,86,86,38,38,38,]),'exp_aritmetica':([13,14,28,34,35,55,58,64,66,67,81,84,89,92,101,115,118,123,136,],[39,39,51,39,87,87,39,39,39,117,39,87,130,132,87,39,143,39,39,]),'termino_aritmetico':([13,14,28,34,35,55,58,64,66,67,81,84,89,92,101,115,118,123,136,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'factor_aritmetico':([13,14,28,34,35,55,58,64,66,67,75,81,84,89,92,95,101,115,118,123,136,146,],[41,41,41,41,41,41,41,41,41,41,120,41,41,41,41,134,41,41,41,41,41,153,]),'operador_booleano':([31,32,33,50,82,88,102,110,113,145,],[58,64,66,66,123,66,66,64,123,123,]),'operaciones_booleanas':([32,110,],[63,140,]),'operador_relacional':([33,39,50,51,82,87,88,102,111,112,142,],[67,89,67,89,67,89,67,67,67,67,67,]),'operaciones_aritmeticas_id':([33,41,50,82,88,102,111,112,116,119,131,133,142,],[68,94,68,68,68,68,68,68,68,144,68,68,68,]),'operador_aritmetico':([33,40,41,50,82,88,102,111,112,116,119,131,133,134,142,153,],[75,92,95,75,75,75,75,75,75,75,75,75,75,146,75,146,]),'operaciones_aritmeticas':([41,134,153,],[93,147,147,]),'tipos':([56,],[103,]),'factor_booleano_id':([66,123,],[113,145,]),'factor_aritmetico_id':([75,95,],[119,119,]),'operaciones_booleanas_id':([82,113,145,],[122,141,152,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> algoritmo","S'",1,None,None,None),
  ('algoritmo -> FUN proposicion proposiciones FFUN','algoritmo',4,'p_algoritmo','Parser.py',33),
  ('empty -> <empty>','empty',0,'p_empty','Parser.py',41),
  ('proposicion -> asignacion PCOMA','proposicion',2,'p_proposicion','Parser.py',48),
  ('proposicion -> inicializar_variable PCOMA','proposicion',2,'p_proposicion','Parser.py',49),
  ('proposicion -> sentencia_si PCOMA','proposicion',2,'p_proposicion','Parser.py',50),
  ('proposicion -> sentencia_mientras PCOMA','proposicion',2,'p_proposicion','Parser.py',51),
  ('proposicion -> sentencia_hacer_mientras PCOMA','proposicion',2,'p_proposicion','Parser.py',52),
  ('proposicion -> sentencia_leer PCOMA','proposicion',2,'p_proposicion','Parser.py',53),
  ('proposicion -> sentencia_escribir PCOMA','proposicion',2,'p_proposicion','Parser.py',54),
  ('proposiciones -> proposicion proposiciones','proposiciones',2,'p_proposiciones','Parser.py',62),
  ('proposiciones -> empty','proposiciones',1,'p_proposiciones','Parser.py',63),
  ('asignacion -> ID ASIGNAR ID','asignacion',3,'p_asignacion','Parser.py',70),
  ('asignacion -> ID ASIGNAR exp_aritmetica','asignacion',3,'p_asignacion','Parser.py',71),
  ('asignacion -> ID ASIGNAR exp_booleana','asignacion',3,'p_asignacion','Parser.py',72),
  ('asignacion -> ID ASIGNAR NULO','asignacion',3,'p_asignacion','Parser.py',73),
  ('asignacion -> ID ASIGNAR VALOR_CADENA','asignacion',3,'p_asignacion','Parser.py',74),
  ('tipos -> ENTERO','tipos',1,'p_tipos','Parser.py',93),
  ('tipos -> BOOLEANO','tipos',1,'p_tipos','Parser.py',94),
  ('tipos -> DECIMAL','tipos',1,'p_tipos','Parser.py',95),
  ('tipos -> CADENA','tipos',1,'p_tipos','Parser.py',96),
  ('inicializar_variable -> VAR ID COLON tipos','inicializar_variable',4,'p_inicializar_variable','Parser.py',103),
  ('operador_aritmetico -> MULT','operador_aritmetico',1,'p_operador_aritmetico','Parser.py',125),
  ('operador_aritmetico -> DIV','operador_aritmetico',1,'p_operador_aritmetico','Parser.py',126),
  ('operador_aritmetico -> SUMA','operador_aritmetico',1,'p_operador_aritmetico','Parser.py',127),
  ('operador_aritmetico -> RESTA','operador_aritmetico',1,'p_operador_aritmetico','Parser.py',128),
  ('operador_aritmetico -> POTENCIA','operador_aritmetico',1,'p_operador_aritmetico','Parser.py',129),
  ('factor_aritmetico -> LPAREN exp_aritmetica RPAREN','factor_aritmetico',3,'p_factor_aritmetico','Parser.py',138),
  ('factor_aritmetico -> NUM_ENTERO','factor_aritmetico',1,'p_factor_aritmetico','Parser.py',139),
  ('factor_aritmetico -> NUM_DECIMAL','factor_aritmetico',1,'p_factor_aritmetico','Parser.py',140),
  ('factor_aritmetico_id -> factor_aritmetico','factor_aritmetico_id',1,'p_factor_aritmetico','Parser.py',141),
  ('factor_aritmetico_id -> ID','factor_aritmetico_id',1,'p_factor_aritmetico','Parser.py',142),
  ('operaciones_aritmeticas -> operador_aritmetico factor_aritmetico operaciones_aritmeticas','operaciones_aritmeticas',3,'p_operaciones_aritmeticas','Parser.py',155),
  ('operaciones_aritmeticas -> empty','operaciones_aritmeticas',1,'p_operaciones_aritmeticas','Parser.py',156),
  ('operaciones_aritmeticas_id -> operador_aritmetico factor_aritmetico_id operaciones_aritmeticas_id','operaciones_aritmeticas_id',3,'p_operaciones_aritmeticas_id','Parser.py',177),
  ('operaciones_aritmeticas_id -> operador_aritmetico factor_aritmetico_id','operaciones_aritmeticas_id',2,'p_operaciones_aritmeticas_id','Parser.py',178),
  ('termino_aritmetico -> factor_aritmetico operaciones_aritmeticas','termino_aritmetico',2,'p_termino_aritmetico','Parser.py',185),
  ('termino_aritmetico -> ID operaciones_aritmeticas_id','termino_aritmetico',2,'p_termino_aritmetico','Parser.py',186),
  ('termino_aritmetico -> factor_aritmetico operaciones_aritmeticas_id','termino_aritmetico',2,'p_termino_aritmetico','Parser.py',187),
  ('exp_aritmetica -> termino_aritmetico','exp_aritmetica',1,'p_exp_arimetica','Parser.py',209),
  ('exp_aritmetica -> termino_aritmetico operador_aritmetico exp_aritmetica','exp_aritmetica',3,'p_exp_arimetica','Parser.py',210),
  ('operador_relacional -> IGUAL','operador_relacional',1,'p_operador_relacional','Parser.py',227),
  ('operador_relacional -> DIFERENTE','operador_relacional',1,'p_operador_relacional','Parser.py',228),
  ('operador_relacional -> LEQ','operador_relacional',1,'p_operador_relacional','Parser.py',229),
  ('operador_relacional -> GEQ','operador_relacional',1,'p_operador_relacional','Parser.py',230),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_operador_relacional','Parser.py',231),
  ('operador_relacional -> MAYOR','operador_relacional',1,'p_operador_relacional','Parser.py',232),
  ('factor_relacional -> LPAREN factor_relacional RPAREN','factor_relacional',3,'p_factor_relacional','Parser.py',239),
  ('factor_relacional -> exp_aritmetica operador_relacional exp_aritmetica','factor_relacional',3,'p_factor_relacional','Parser.py',240),
  ('factor_relacional -> ID operador_relacional exp_aritmetica','factor_relacional',3,'p_factor_relacional','Parser.py',241),
  ('factor_relacional -> exp_aritmetica operador_relacional ID','factor_relacional',3,'p_factor_relacional','Parser.py',242),
  ('factor_relacional -> ID operador_relacional ID','factor_relacional',3,'p_factor_relacional','Parser.py',243),
  ('operador_booleano -> IGUAL','operador_booleano',1,'p_operador_booleano','Parser.py',252),
  ('operador_booleano -> DIFERENTE','operador_booleano',1,'p_operador_booleano','Parser.py',253),
  ('operador_booleano -> Y','operador_booleano',1,'p_operador_booleano','Parser.py',254),
  ('operador_booleano -> O','operador_booleano',1,'p_operador_booleano','Parser.py',255),
  ('factor_booleano -> LPAREN exp_booleana RPAREN','factor_booleano',3,'p_factor_booleano','Parser.py',261),
  ('factor_booleano -> VERDADERO','factor_booleano',1,'p_factor_booleano','Parser.py',262),
  ('factor_booleano -> FALSO','factor_booleano',1,'p_factor_booleano','Parser.py',263),
  ('factor_booleano -> factor_relacional','factor_booleano',1,'p_factor_booleano','Parser.py',264),
  ('factor_booleano -> NEGAR factor_booleano','factor_booleano',2,'p_factor_booleano','Parser.py',265),
  ('factor_booleano_id -> factor_booleano','factor_booleano_id',1,'p_factor_booleano','Parser.py',266),
  ('factor_booleano_id -> ID','factor_booleano_id',1,'p_factor_booleano','Parser.py',267),
  ('factor_booleano_id -> NEGAR ID','factor_booleano_id',2,'p_factor_booleano','Parser.py',268),
  ('operaciones_booleanas -> operador_booleano factor_booleano operaciones_booleanas','operaciones_booleanas',3,'p_operaciones_booleanas','Parser.py',275),
  ('operaciones_booleanas -> empty','operaciones_booleanas',1,'p_operaciones_booleanas','Parser.py',276),
  ('operaciones_booleanas_id -> operador_booleano factor_booleano_id operaciones_booleanas_id','operaciones_booleanas_id',3,'p_operaciones_booleanas','Parser.py',277),
  ('operaciones_booleanas_id -> empty','operaciones_booleanas_id',1,'p_operaciones_booleanas','Parser.py',278),
  ('termino_booleano -> factor_booleano operaciones_booleanas','termino_booleano',2,'p_termino_booleano','Parser.py',285),
  ('termino_booleano -> ID operador_booleano factor_booleano_id operaciones_booleanas_id','termino_booleano',4,'p_termino_booleano','Parser.py',286),
  ('termino_booleano -> NEGAR ID operaciones_booleanas_id','termino_booleano',3,'p_termino_booleano','Parser.py',287),
  ('exp_booleana -> termino_booleano','exp_booleana',1,'p_exp_booleana','Parser.py',294),
  ('exp_booleana -> termino_booleano operador_booleano exp_booleana','exp_booleana',3,'p_exp_booleana','Parser.py',295),
  ('sentencia_si -> SI exp_booleana ENTONCES proposicion proposiciones FSI','sentencia_si',6,'p_sentencia_si','Parser.py',304),
  ('sentencia_si -> SI exp_booleana ENTONCES proposicion proposiciones SINO proposicion proposiciones FSI','sentencia_si',9,'p_sentencia_si','Parser.py',305),
  ('sentencia_mientras -> MIENTRAS exp_booleana HACER proposicion proposiciones FMIENTRAS','sentencia_mientras',6,'p_sentencia_mientras','Parser.py',311),
  ('sentencia_hacer_mientras -> HACER proposicion proposiciones MIENTRAS exp_booleana','sentencia_hacer_mientras',5,'p_sentencia_hacer_mientras','Parser.py',317),
  ('sentencia_leer -> LEER LPAREN ID RPAREN','sentencia_leer',4,'p_sentencia_leer','Parser.py',323),
  ('sentencia_escribir -> ESCRIBIR LPAREN ID RPAREN','sentencia_escribir',4,'p_sentencia_escribir','Parser.py',329),
]
