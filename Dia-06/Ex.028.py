    # Exercício 028 — Revisão - Módulos e Bibliotecas
'''Objetivo: Aprender a ler documentação. Bibliotecas: 
- Laboratório Math + Statistics

- Cadastre 10 números reais. Pesquise na Biblioteca e mostre:
lista original; média; mediana; moda; maior valor; menor valor;
raiz quadrada do maior valor; arredondamento para cima de todos os números;
arredondamento para baixo de todos os números.
- Regras:
1 - não copiar exemplos prontos; 2- consultar a documentação;
3 - descobrir sozinho como usar cada função; 4 - anotar em comentário o que cada função faz.'''
import math
import statistics

numeros = []
raizq = []
cima = []
baixo = []

for i in range(10):
    numero = float(input(f'Digite o {i+1}º numero: '))
    numeros.append(numero)
    cima.append(math.ceil(numero)) # arredonda pra cima o valor = math.ceil()
    baixo.append(math.floor(numero)) # arredonda pra baixo o valor = math.floor()
    if numero >= 0:
        raizq.append(round(math.sqrt(numero), 2)) # math.sqrt() retorna a raiz quadrada de numeros inteiros positivos
    # usei o round tambem pra arrendondar pra 2 casas
    else:
        raizq.append('N/A')

media = statistics.mean(numeros) # mean mostra a média dos numeros - uso com statistics.mean()
mediana = statistics.median(numeros) # retorna o valor do meio dos dados numérios. uso com stastics.median()
# Se a quantidade de numero for par, calcula a média dos dois do meio
moda = statistics.mode(numeros) # retorna o valor mais frequente. uso com statistics.mode()
maior = max(numeros) # max mostra o maior valor
menor = min(numeros) # min o menor valor

print(f'Lista completa = {numeros}')
print(f'A média dos numeros = {media:.2f} e a mediana entre eles: {mediana}')
print(f'O numero que mais se repete {moda}')
print(f'O maior numero {maior} e o menor numero {menor}')
print(f'Lista da raiz quadrada dos numeros {raizq}')
print(f'O valor dos numeros arredondados pra cima {cima}')
print(f'O valor dos numeros arredondados pra baixo {baixo}')