    # Exercício 027 — Revisão Geral (%, //, Condicionais e Laços)
'''Receba 10 números inteiros. Depois mostre:
- pares;
- ímpares;
- soma dos pares;
- soma dos ímpares;
- quantidade de múltiplos de 3;
- resultado da divisão inteira por 2 (//).'''
multiplos_tres = []
pares = []
impares = []
par = impar = soma = 0

for i in range(10):
    numero = int(input(f'Digite o {i+1}º numero: '))
    soma += numero
    if numero % 2 == 0:
        pares.append(numero)
        par += numero
    else:
        impares.append(numero)
        impar += numero

    if numero % 3 == 0:
        multiplos_tres.append(numero)

diviint = soma // 2

print(f'Os numeros pares são: {pares}, a soma deles da: {par}')
print(f'Os numeros impares são: {impares}, a soma deles da: {impar}')
print(f'Os numeros que são multiplos de 3 são {multiplos_tres}')
print(f'A divisão inteira da soma de todos os numeros é: {diviint}')