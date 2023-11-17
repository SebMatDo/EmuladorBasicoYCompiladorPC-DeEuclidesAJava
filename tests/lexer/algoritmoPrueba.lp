###### SE INICIALIZA UN ALGORITMO muy simple para pruebas #####

fun
    var a : booleano;
    var b : booleano;
    var c : booleano;
    a = verdadero;
    b = falso && verdadero; ## falso
    a = a || b;  ## verdadero
    c = (a || b && b || (a && verdadero || verdadero || falso) || falso);
    ## c = (verdadero || falso && falso || verdadero || falso) finalmente da verdadero

ffun

### fin algoritmo