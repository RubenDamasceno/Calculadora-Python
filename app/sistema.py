from time import sleep
from app.operacoes import *
from app.utilidades import leiaInt, menu



def iniciar():
    while True:
        resp = menu(['Somar', 'Subtrair', 'Multiplicar', 'Dividir', 'Sair'])
        if resp == 1:
            while True:
                numeros = input('Digite os números para somar separados por espaços: ')
                try:
                    lista = [float(n) for n in numeros.split()]
                    if len(lista) == 0:
                        print('ERRO! Você precisa digitar ao menos um número!')
                    else:
                        print(f'O resultado da Soma vale: {soma(*lista)}')
                        break
                except ValueError:
                    print('ERRO! Por favor, digite apenas números separados por espaços!')

        elif resp == 2:
            while True:
                numeros = input('Digite os números para subtrair separados por espaços: ')
                try:
                    lista = [float(n) for n in numeros.split()]
                    if len(lista) == 0:
                        print('ERRO! Você precisa digitar ao menos um número!')
                    else:
                        print(f'O resultado da Subtração vale: {subtracao(*lista)}')
                        break
                except ValueError:
                    print('ERRO! por favor, digite apenas números separados por espaços!')

        elif resp == 3:
            while True:
                numeros = input('Digite os números para multiplicar separados por espaços: ')
                try:
                    lista = [float(n) for n in numeros.split()]
                    if len(lista) == 0:
                        print('ERRO! Você precisa digitar ao menos um número!')
                    else:
                        print(f'O resultado da Multiplicação vale: {multiplicar(*lista)}')
                        break
                except ValueError:
                    print('ERRO! Por favor, digite apenas números separados por espaços!')

        elif resp == 4:
            while True:
                numeros = input('Digite os numeros para dividir separados por espaços:')
                try:
                    lista = [float(n) for n in numeros.split()]
                    if len(lista) == 0:
                        print('ERRO! Você precisa digitar ao menos um número!')
                    else:
                        resultado = dividir(*lista)
                        if isinstance(resultado, str):
                            print(f'{resultado}')
                        else:
                            print(f'O resultado da Divisão vale: {resultado:.2}')
                            break
                except ValueError:
                    print('ERRO! Por favor, digite apenas números separados por espaços!')

        if resp == 5:
            print('Finalizando', end='',flush=True)
            for _ in range(3):
                sleep(0.5)
                print('.', end='',flush=True)
            print()
            print('>>> Volte sempre! <<<')
            break




