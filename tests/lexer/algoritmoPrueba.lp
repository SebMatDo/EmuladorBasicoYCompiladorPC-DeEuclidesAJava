###### SE INICIALIZA UN ALGORITMO muy simple para pruebas (fibonacci)#####

fun
    a = 1;
    b = 1;
    c = 10; ## EL C no puede ser muy alto o hay overflow en la suma lol
    mientras  (c > 0) hacer
        a = a + b;
        b = b + a;
        c = c - 1;
    fmientras;

ffun

### fin algoritmo