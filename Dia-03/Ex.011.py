    # Exercício 011 — ( Revisão ) + Random
'''Vamos começar com o módulo random. Leia 10 nomes e armazene-os em uma lista.
Depois utilize o módulo random para:
- sortear um nome;
- mostrar a lista completa;
- mostrar o nome sorteado.'''

from random import choice
nomes = []

for i in range(10):
    nomes.append(input(f'Digite o {i+1}º Nome: '))

print(f'Lista de Nomes:\n{nomes}')
print(f'Nome sorteado: {choice(nomes)}')