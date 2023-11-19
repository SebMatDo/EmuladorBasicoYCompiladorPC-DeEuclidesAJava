###### SE INICIALIZA UN ALGORITMO muy simple para pruebas (fibonacci)#####

fun
    var a : entero;
    var b : entero;
    var c : entero;
    a = 1; 
    b = 1;
    c = 5;
    mientras (c > 0) hacer
	escribir(a);
	escribir(b);
	a = a+b;
	b = b+a;
	c = c - 1;
    fmientras;
ffun


### fin algoritmo


fun
   var a : entero;
   var b : entero;
   a = 1;
   b = 3;
   a = a + b;
ffun


fun
var a : entero;
var b : entero;
a = 255;
b = 75;
mientras (a != b) hacer
	si (a > b) entonces
		a =  a - b;
	fsi;
	si  (a < b) entonces
		b = b - a;
	fsi;
fmientras;
escribir(a);
ffun


fun
var a : entero;
var b : entero;
var factorial : entero;
a = 5;
factorial = 1;
mientras (a > 0) hacer
	factorial = factorial * a;
	a = a - 1;
fmientras;
escribir(factorial);
ffun