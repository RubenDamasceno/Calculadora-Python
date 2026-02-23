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
            return "\033[31mERRO! Divisão por zero!\033[m"
        res /= n
    return res
