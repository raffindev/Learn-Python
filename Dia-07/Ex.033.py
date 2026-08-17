    # Exercício 33 — Revisão Geral 1
'''Cadastre 10 números e mostre:
- lista completa - soma total - média - maior valor - menor valor - primeiros 3 números
- últimos 3 números - quantidade de pares - quantidade de ímpares'''

numeros = []
pares = []
impares = []

for i in range(10):
    numero = int(input(f'{i+1}º Numero: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

    numeros.append(numero)

# Quantitativos
soma = sum(numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)


print('='*5, 'Lista Numeros', '='*5)
print(f'Os numeros digitados foram: {numeros}')
print(f'A soma total foi: {soma}. Com uma média de {media:.2f}')
print(f'O maior valor é {maior}. Ja o menor é {menor}')
print(f'Os 3 primeiros numeros da lista são: {numeros[:3]}')
print(f'Os 3 ultimos numeros são {numeros[-3:]}')
print(f'Os numeros pares são: {pares}, com total de {len(pares)} numeros pares')
print(f'Os impares são {impares}, com total de {len(impares)} numeros impares')