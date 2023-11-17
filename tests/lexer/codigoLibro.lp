###### SE INICIALIZA UN ALGORITMO #####

fun
    ###### PRUEBAS INICIALIZAR VARIABLES #####
    var a : entero;
    var b : entero;
    var c : entero;
    var d : entero;
    c = 256;
    d = 125;
    a = b;
    ## a = 'Holamundo';
    ## b = "Hola mundo soy una cadena";

    ##### PRUEBAS ARITMETICAS ##########
    a = 2;
    a = 123+231;
    b = -123.45 - 1234.56677 - 234;
    a = 12*23;
    a = 12.23 * -23.345;
    b = 123 ^ 234 * 2345 + 234;
    a = (-12.33 / 2) + 2;
    a =((-12.3 /2) + 2);
    b = (2) + (3);
    a = ((123 ^ 23 - 23 * 94) / (1234 - 34)  + (23 * -233) * 2 ^ 2);
    a = 2 + 3 ^ 2 - (-52.5 - (52 - -2.4) + 54 * 2) + (52.5 - 5) / (2);
    b = 123+123+4124.2;
    c = a + 23 + b + 2;
    d = 12 - b + 3.4 - a + 3.3;


    ####### PRUEBAS BOOLEANAS ##########
    a = verdadero;
    b = falso;
    a = (verdadero);
    a = !verdadero;
    b = !!!!!!!!!!!!!verdadero;
    b = verdadero || verdadero;
    a = (verdadero && verdadero || falso || verdadero) || falso || verdadero;

    a = c != d;
    a = b==b;
    b = d || a;
    b = a || b;
    a = a || (b && d);
    a = falso || (123==123 && a==b);


    ######## PRUEBAS DE OPERACIONES RELACIONALES #######
    a = 123==233;
    b = 123>4325;
    a = (123 ^ 23 - 23 * 94) / (1234 - 34)  + (23 * -233) * 2 ^ 2 >= (1 ^ 23 - 23 * 94) / (1234 - 34)  + (23 * -233) * 2 ^ 2;

    ####### PRUEBAS DE BOOLEANOS CON OPERACIONES RELACIONALES ######
    a = !falso || !123==123 && !a>b;
    a = !a || !(123==123);
    b = !a || !b && c;
    a = a>b ;
    a = a>b && d<a;

    ######### PRUEBAS DE SENTENCIAS ########

    ## IF
    si verdadero entonces
        a = 2;
    fsi;

    si a == 23 entonces
        a = 4;
    sino
        b = 3;
    fsi;

    si (b == 3 && c == 5) entonces
        c = c * 2;
        si ( c < 1024 ) entonces
            c = c + 1;
        sino
            c = c + 2;
        fsi;
    sino
        d = d + c;
    fsi;

    ## WHILE
    mientras verdadero hacer
        a = 2;
    fmientras;

    mientras b > c hacer
        a = b;
        b = a / b;
    fmientras;

    mientras (a >= 3) hacer
        b = 2;
        si (23+a+b < 1000) entonces
            a = a+1;
        fsi;
    fmientras;




ffun

###### FIN ALGORITMO #######