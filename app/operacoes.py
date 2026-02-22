def soma(*numeros):
    return sum(numeros)

def subtracao(*numeros):
    res = numeros[0]
    for n in numeros[1:]:
        res -= n
    return res

def multiplicar(*numeros):
    res = numeros[0]
    for n in numeros[1:]:
        res *= n
    return res

def dividir(*numeros):
    res = numeros[0]
    for n in numeros[1:]:
        if n == 0:
            return "ERRO! Divisão por zero!"
        res /= n
    return res
