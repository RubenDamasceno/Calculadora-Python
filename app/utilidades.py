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