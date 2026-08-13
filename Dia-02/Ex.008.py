    # Exercício 008 — ( Revisão )
'''Crie uma lista com 10 números digitados pelo usuário. Mostre:
- números pares;
- números ímpares;
- soma dos pares;
- soma dos ímpares.
Tente fazer apenas percorrendo a lista uma vez.'''

numeros = []
par = []
impar = []
cont_par = cont_impar = 0

for i in range(10):
    numero = int(input(f'Digite o {i + 1}º número: '))
    numeros.append(numero)
    
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f'A lista de números: {numeros}')
print(f'Tem um total de {len(par)} números pares. Sendo eles: {par}')
print(f'A soma dos pares: {sum(par)}')
print(f'Tem um total de {len(impar)} números ímpares. Sendo eles: {impar}')
print(f'A soma dos impares: {sum(impar)}')