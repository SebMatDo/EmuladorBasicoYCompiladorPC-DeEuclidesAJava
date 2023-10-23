params a, b, c

var x1, x2, x3

maximize a * x1 + (b * x3) / 4 - 2 * a * x2

subject to

    x1 + x2 < 300;
    x3 = -10.87;
    x1 + 34.5 * x3  >= 4;
    x1 > 0; x2 > 0; x3 > 0;