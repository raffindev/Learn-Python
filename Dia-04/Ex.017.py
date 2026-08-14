    # Exercício 017 — ( Revisão ) + Math
'''Leia 5 números decimais. Para cada número mostre:
valor original - floor - ceil'''
import math

numeros = []
for i in range(5):
    numeros.append(float(input(f'{i+1}º Numero: ')))

cima = [math.ceil(numero) for numero in numeros]
baixo = [math.floor(numero) for numero in numeros]

print(f'Valor original: {numeros}')
print(f'Valor com arredondamento pra cima {cima}')
print(f'Valor com arredondamento pra baixo {baixo}')