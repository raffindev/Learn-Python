    # Exercício 014 — ( Desafio ) - Sistema de Votação
'''Cadastre candidatos. Depois inicie a votação. O usuário poderá votar digitando o nome do candidato.
A votação termina quando for digitado: FIM - Ao final mostre:
- total de votos;
- votos de cada candidato;
- vencedor da eleição.'''

# Cadastro de Candidatos
candidatos = []

while True:
    candidato = {}
    candidato['Nome'] = input('Nome: ').title().strip()
    candidato['Votos'] = 0
    candidatos.append(candidato)

    while True:
        cadastrar = input('Gostaria de cadastrar outro candidato? [S/N] ').upper()
        if cadastrar in ('S', 'N'):
            break
        else:
            print('Opção inválida. Digite [S/N]')
    if cadastrar == 'N':
        break

print()
print('='*3, 'CANDIDATOS', '='*3)
for i, candidato in enumerate(candidatos):
    print(f'{i+1}. {candidato['Nome']} teve: {candidato['Votos']} votos')

# Votação
print()
print('='*3, 'VOTAÇÃO', '='*3)

votos = 0
while True:
    votação = input('Gostaria de votar em qual candidato? ').upper()

    if votação == 'FIM':
        break

    if not votação.isdigit():
        print('Digite um número válido ou FIM.')
        continue

    votação = int(votação)

    if 1 <= votação <= len(candidatos):
        candidato = candidatos[votação - 1]
        candidato['Votos'] += 1
        votos += 1
        print(f"Voto registrado para {candidato['Nome']}!")
    else:
        print('Não existe candidato com esse número.')
        
# Resultado
vencedor = max(candidatos, key=lambda candidato: candidato['Votos'])
print(f'\nTeve um total de {votos} votos')
print(f'E o vencedor foi {vencedor['Nome']} com {vencedor['Votos']}')