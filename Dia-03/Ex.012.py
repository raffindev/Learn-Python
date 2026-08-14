    # Exercício 012 — ( Revisão ) + Math
'''Vamos usar math. Leia 5 números. Para cada número mostre:
- valor digitado;
- quadrado;
- raiz quadrada.'''
from math import sqrt

numeros = []

for i in range(5):
    numero = int(input(f'Digite o {i+1}º número: '))
    numeros.append(numero)

for numero in numeros:
    print(f'Valor: {numero} | Quadrado: {numero**2} | Raiz: {sqrt(numero):.2f}')