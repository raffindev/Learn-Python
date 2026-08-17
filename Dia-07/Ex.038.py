    # Exercício 38 — Desafio de Lógica
'''Sistema de Votação. Cadastre candidatos. Depois permita votos. Ao final mostre:
- total de votos
- vencedor
- empate (se houver)
- percentual de cada candidato'''
candidatos = []

# Parte 1 - Cadastrar Candidatos
while True:
    candidato = {}
    while True:
        candidato['Nome'] = input('Nome: ').capitalize().strip()
        if candidato['Nome'] == ' ':
            print('Nome inválido! Não pode conter espaços.')
        elif not candidato['Nome'].replace(' ', '').isalpha():
            print('Nome inválido! Não pode conter números ou símbolos.')
        else:
            break

    candidato['Votos'] = 0

    candidatos.append(candidato)
    print('Candidato cadastrado com sucesso!')

    while True:
        cadastrar = input('Deseja cadastrar outro candidato? [S/N] ').upper()
        if cadastrar in ('S', 'N'):
            break
    if cadastrar == 'N':
        break

#Parte 2 - Sistema de votação
print('='*30)
print('Votação'.center(30))
print('='*30)
for i, candidato in enumerate(candidatos, start=1):
    print(f'{i}. {candidato['Nome']} - Votos: {candidato['Votos']}')
print('='*30)
while True:
    try:
        votação = int(input(
            'Escolha o candidato que gostaria de votar ou 999 para encerrar: '))
        if votação == 999:
            break

        if votação < 1 or votação > len(candidatos):
            print('Erro: escolha um candidato válido\n')
            continue

        candidatos[votação - 1]['Votos'] += 1
        print('Voto registrado!\n')
    except ValueError:
        print('Escolha um candidato válido\n')

# Quantitativo
vencedor = max(candidato['Votos'] for candidato in candidatos)
empatados = [candidato['Nome'] for candidato in candidatos if candidato['Votos'] == vencedor]
total_votos = sum(candidato['Votos'] for candidato in candidatos)

# Resultado
print('=' * 30)
print('Resultado da Votação'.center(30))
print('=' * 30)

for i, candidato in enumerate(candidatos, start=1):
    if total_votos > 0:
        percentual = candidato['Votos'] / total_votos * 100
    else:
        percentual = 0

    print(f"{i}. {candidato['Nome']} - Votos: {candidato['Votos']} - {percentual:.2f}%")

print('=' * 30)
if len(empatados) == 1:
    print(f"Vencedor: {empatados[0]}")
else:
    print("Empate entre:")
    for nome in empatados:
        print(f"- {nome}")