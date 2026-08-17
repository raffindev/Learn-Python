    # Exercício 026 — Revisão Geral (Operadores, Slice, Listas e Dicionários)
'''Crie um sistema que receba 8 nomes. Depois mostre:
 - lista completa;
 - os 3 primeiros nomes;
 - os 3 últimos nomes;
 - quantidade de nomes cadastrados;
 - nome com mais letras;
 - nome com menos letras.'''
nomes = []

for i in range(8):
    nomes.append(input(f'Digite o {i+1} nome: ').title().strip())

print(f'Os nomes digitados foram: \n{nomes}\n')
print(f'Os 3 primeiros nomes são: {nomes[:3]}')
print(f'Os 3 ultimos nomes são: {nomes[-3:]}')
print(f'Tem {len(nomes)} nomes cadastrados')

maior = max(nomes, key=len)
menor = min(nomes, key=len)

print(f'O maior nome é {maior} com {len(maior)} letras')
print(f'O menor nome é {menor} com {len(menor)} letras')