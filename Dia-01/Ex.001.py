    # Exercício 001 (Revisão)
'''Crie um programa que receba 5 números inteirosm, armazene os números em uma lista e Mostre:
- a lista completa;
- o maior valor;
- o menor valor;
- a soma de todos os números.'''
numeros = []

for i in range(5):
    numeros.append(int(input(f'Digite o {i+1}º numero: ')))

print(f'Numeros digitados: {numeros}')
print(f'Maior valor: {max(numeros)}')
print(f'Menor valor: {min(numeros)}')
print(f'Soma {sum(numeros)}')