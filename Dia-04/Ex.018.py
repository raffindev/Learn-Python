    # Exercício 018 — ( Revisão ) + Lambda
'''Cadastre 6 filmes. Cada filme deve possuir: (titulo - ano) Depois mostre:
- lista original;
- lista ordenada por ano usando sorted(..., key=lambda ...);
- filme mais antigo;
- filme mais recente.'''
from datetime import date

filmes = []
ano_atual = date.today().year

# Cadastrando filme - Tratamento de erro
for i in range(6):
    filme = {}
    filme['Nome'] = input('Nome do Filme: ').title().strip()
    filme['Ano'] = int(input('Ano de Lançamento: '))

    while filme['Ano'] < 0 or filme['Ano'] > ano_atual:
        print(f'Erro! O ano deve estar entre 0 e {ano_atual}.')
        filme['Ano'] = int(input('Digite novamente o Ano de Lançamento: '))
    filmes.append(filme)

print()
print(f'='*5, 'Lista de Filmes', '='*5)
for i, filme in enumerate(filmes):
    print(f"{filme['Ano']} - {filme['Nome']}")

# Sorteando a Lista e Mostrando Mais antigo e Mais novo.
print()
print(f'='*5, 'Lista de Filmes por Lançamento', '='*5)
lançamento = sorted(filmes, key=lambda filme: filme['Ano'])
for pos, filme in enumerate(lançamento):
    print(f'{filme['Ano']} - {filme['Nome']}')
antigo = lançamento[0]
novo = lançamento[-1]

print(f"\nFilme mais antigo: {antigo['Ano']} - {antigo['Nome']}")
print(f"Filme mais novo: {novo['Ano']} - {novo['Nome']}")