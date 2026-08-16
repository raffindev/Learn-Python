    # Exercício 025 — ( Desafio ) - Caixa Eletrônico 2.0
'''O usuário informa: Saldo inicial. Depois o programa exibe:
1 - Depositar
2 - Sacar
3 - Consultar saldo
0 - Sair'''

menu = ('''===== Caixa Eletrônico =====
1 - Depositar
2 - Sacar
3 - Consultar saldo
4 - Ver menu
0 - Sair
=============================''')

# Validação de saldo inicial
while True:
    try:
        saldo = int(input('Informe seu Saldo: R$ '))
        if saldo <= 0:
            print('O valor informado tem que ser maior que 0.')
        else:
            break

    except ValueError:
        print('Precisa conter números')

print(menu)

while True:
    # Validação da opção
    try:
        opção = int(input('\nDigite a Operação Desejada: '))
        if opção not in [0, 1, 2, 3, 4]:
            print('Operação inválida.')
            continue

    except ValueError:
        print('Digite apenas números.')
        continue

    if opção == 1:
        while True:
                depositar = int(input('Valor que gostaria de Depositar: R$ '))

                if depositar < 0:
                    print('O valor não pode ser negativo.')
                    continue

                saldo += depositar
                print(f'Valor depositado. R$ {depositar:.2f}')
                break

    if opção == 2:
        while True:
            try:
                sacar = int(input('Valor que gostaria de Sacar: R$ '))

                if sacar < 0:
                    print('O valor deve ser maior que 0.')
                    continue

                if sacar > saldo:
                    print('Saldo insuficiente.')
                    continue

                saldo -= sacar
                print(f'Saque realizado com sucesso. Valor sacado: R$ {sacar:.2f}')
                break

            except ValueError:
                print('Digite apenas números.')

    if opção == 3:
        print(f'Consultar Saldo: R$ {saldo:.2f}')

    if opção == 4:
        print(menu)
        continue

    if opção == 0:
        print('Programa encerrado.')
        break