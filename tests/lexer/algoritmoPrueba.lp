###### SE INICIALIZA UN ALGORITMO muy simple para pruebas (fibonacci)#####

fun
    var a : entero;
    var b : entero;
    var c : entero;
    a = 1;
    b = 1;
    c = 5;
    mientras  (c > 0) hacer
        a = a + b;
        b = b + a;
        c = c - 1;
        escribir(a);
    fmientras;
ffun

### fin algoritmo