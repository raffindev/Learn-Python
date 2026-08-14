    # Exercício 016 — ( Revisão ) + Documentação
'''Utilize a biblioteca random e use a função: shuffle(). Depois: Leia 8 nomes.
- Armazene-os em uma lista.
- Embaralhe a lista usando shuffle().
- Mostre a ordem original e a nova ordem.'''
from random import shuffle

nomes = []
for i in range(8):
    nomes.append(input(f'Digite o {i+1}º nome: '))

print(f'Lista original: {nomes}')
embaralhada = shuffle(nomes)
print(f'Lista embaralhada: {nomes}')