from time import sleep
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor, Digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('ERRO! Interrupção feita pelo usuário.')
            return 0
        else:
            return n


def menu(opcoes):
    for i, opcao in enumerate(opcoes):
        print(f'{i+1} - {opcao}')
    opc = leiaInt('Escolha uma opção: ')
    return opc

def soma(*numeros):
    return sum(numeros)

def iniciar():
    while True:
        resp = menu(['Somar', 'Subtrair', 'Multiplicar', 'Dividir', 'Sair'])
        if resp == 1:
            numeros = input('Digite os números para somar separados por espaço: ')
            lista = [float(n) for n in numeros.split()]
            print(f'Resultado: {soma(*lista)}')
        if resp == 5:
            print('Finalizando', end='',flush=True)
            for _ in range(3):
                sleep(0.5)
                print('.', end='',flush=True)
            print()
            print('>>> Volte sempre! <<<')
            break




