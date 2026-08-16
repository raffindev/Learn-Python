    # Exercício 022 — ( Revisão ) Biblioteca
'''Utilize a biblioteca ramdom. Leia 20 nomes e sorteie 5 sem repitir.
Mostre os sorteados e quem ficou de fora'''
from random import sample

nomes = []

for i in range (20):
    while True:
        nome = input(f'Digite o {i+1}º nome: ').title().strip()

        if nome != '' and nome.isalpha():
            nomes.append(nome)
            break

        print('Nome inválido! Digite apenas letras.')

sorteados = sample(nomes, 5)

print('='*3, 'Lista de Sorteados', '='*3)
for i, nome in enumerate(sorteados):
    print(f'{i+1}º Sorteado - {nome}') 
print('='*3, 'Ficaram de fora', '='*3)
for nome in nomes:
    if nome not in sorteados:
        print(nome, end='. ')