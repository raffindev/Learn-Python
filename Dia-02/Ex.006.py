    # Exercício 006 — ( Revisão )
'''Leia 8 números inteiros e armazene-os em uma lista. Ao final mostre:
- a lista completa;
- quantos números são pares;
- quantos números são ímpares;
- o maior valor e sua posição;
- o menor valor e sua posição.'''

numeros = []

for i in range(8):
    numero = int(input(f'Digite o {i + 1}º número: '))
    numeros.append(numero)

pares = sum(numero % 2 == 0 for numero in numeros)
impares = len(numeros) - pares

maior_valor = max(numeros)
menor_valor = min(numeros)

posicao_maior = numeros.index(maior_valor) + 1
posicao_menor = numeros.index(menor_valor) + 1

print(f'\nLista: {numeros}')
print(f'Pares: {pares} - Ímpares: {impares}')
print(f'O maior valor {maior_valor} está na posição {posicao_maior}')
print(f'O menor valor {menor_valor} está na posição {posicao_menor}')