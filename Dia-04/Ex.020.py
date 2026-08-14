    # Exercício 020 — ( Desafio ) - Ranking de Jogadores
'''Cadastre jogadores contendo: (NOME - PONTUAÇÃO). Depois:
- Mostrar todos os jogadores.
- Exibir ranking do maior para o menor usando sorted().
- Mostrar Top 3.
- Mostrar a média de pontuação.
- Mostrar quem ficou acima da média.'''
ranking = []
medalhas = ["🥇", "🥈", "🥉"]

# Cadastro
print("=" * 40 + "\n" + "RANKING DE JOGADORES".center(40) + "\n" + "=" * 40)
while True:
    jogador = {}
    jogador['Nome'] = input('Nome: ').capitalize().strip()
    jogador['Equipe'] = input('Equipe: ').title().strip()
    jogador['Pontuação'] = int(input('Pontuação: '))
    while jogador['Pontuação'] <= 0:
        print('Pontuação inválida!')
        jogador['Pontuação'] = int(input('Pontuação: '))
    ranking.append(jogador)
    print()
    
    while True:
        cadastrar = input('Gostaria de Cadastrar outro jogador? [S/N]: ').upper()[0]
        if cadastrar in ('S', 'N'):
            break
    if cadastrar == 'N':
        break

# Pontuação
rank_pontos = sorted(ranking, key=lambda jogador: jogador['Pontuação'], reverse=True)
media = sum(jogador['Pontuação'] for jogador in ranking) / len(ranking)

# Visualização
print("=" * 50 + "\n" + "TODOS OS JOGADORES".center(50) + "\n" + "=" * 50)
for jogador in enumerate(ranking):
    print(f"Equipe: {jogador['Equipe']:<15} - {jogador['Nome']:<7} - {jogador['Pontuação']} pontos")

print("=" * 50 + "\n" + "RANKING".center(50) + "\n" + "=" * 50)
for i, jogador in enumerate(rank_pontos):
    print(f"{i+1}º {jogador['Nome']:<7} - {jogador['Pontuação']} pontos")

print("=" * 50 + "\n" + "TOP 3".center(50) + "\n" + "=" * 50)
for i, jogador in enumerate(rank_pontos[:3]):
    print(f"{medalhas[i]} {jogador['Equipe']:<15} {jogador['Nome']:<7} - {jogador['Pontuação']} pontos")
print("=" * 50)
print(f"Media {media:.2f} pontos - JOGADORES ACIMA DA MÉDIA".center(50))
print("=" * 50)
for jogador in ranking:
    if jogador['Pontuação'] > media:
        print(f"{jogador['Equipe']} {jogador['Nome']:<7} - {jogador['Pontuação']} pontos")