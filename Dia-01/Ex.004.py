    # Exercício 004 (Revisão) - Caixa Eletrônico Simples.
'''O usuário informa um valor inteiro. O programa deve informar quantas notas de:
R$100 - R$50 - R$20 - R$10 - R$5 - R$2 - R$1'''

saque = int(input('Digite o valor que gostaria de Sacar: R$ '))
valor = saque
cem = cinquenta = vite = dez = cinco = dois = um = 0

cem = saque // 100
saque %= 100

cinquenta = saque // 50
saque %= 50

vinte = saque // 20
saque %= 20

dez = saque // 10
saque %= 10

cinco = saque // 5
saque %= 5

dois = saque // 2
saque %= 2

um = saque // 1
saque %= 1

print('='*5, 'CAIXA ELETRÔNICO', '='*5)
print(f'Valor Solicitado: R$ {valor:.2f}\n')
print('-'*7, 'Cédulas', '-'*7)
if cem > 0:
    print(f'{cem} notas de R$ 100')
if cinquenta > 0:
    print(f'{cinquenta} notas de R$ 50')
if vinte > 0:
    print(f'{vinte} notas de R$ 20')
if dez > 0:
    print(f'{dez} notas de R$ 10')
if cinco > 0:
    print(f'{cinco} notas de R$ 5')
if dois > 0:
    print(f'{dois} notas de R$ 2')
if um > 0:
    print(f'{um} notas de R$ 1')