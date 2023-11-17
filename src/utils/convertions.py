def decimalToBinary(value):
    a = bin(value & (2 ** 10 - 1))
    a = a.replace('0b', '')
    addZeros = 10 - len(a)
    toRet = ''
    while addZeros > 0:
        toRet += '0'
        addZeros -= 1
    toRet += a
    return toRet

def binaryToDec(binary):
    minus = 0
    if binary[0] == '1':
        minus = 1024
    return int(binary, 2) - minus

def isNum(n):
    try:
        int(n)
        return True
    except ValueError:
        return False