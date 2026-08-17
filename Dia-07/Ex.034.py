    # Exercício 34 — Revisão Geral 2
'''Cadastre 8 produtos. Cada produto deve ter: nome - preço. Ao final:
- produto mais caro
- produto mais barato
- média dos preços
- produtos acima da média
- produtos abaixo da média'''
from statistics import mean

produtos = []

for i in range(8):
    produto = {}
    produto['Nome'] = input('Produto: ')
    produto['Preço'] = float(input('Preço: R$ '))
    produtos.append(produto)

mais_caro = max(produtos, key=lambda produto: produto['Preço'])
mais_barato = min(produtos, key=lambda produto: produto['Preço'])
media = mean(produto['Preço'] for produto in produtos)

print('=' * 5, 'Produtos', '=' * 5)
for i, produto in enumerate(produtos):
    print(f"{i + 1}. {produto['Nome']} - R$ {produto['Preço']:.2f}")

print(f"\nO produto mais barato é {mais_barato['Nome']} custando R$ {mais_barato['Preço']:.2f}")
print(f"O produto mais caro é {mais_caro['Nome']} custando R$ {mais_caro['Preço']:.2f}")
print(f"A média do valor dos produtos foi: R$ {media:.2f}\n")

print('=' * 5, 'Valor Acima da Média', '=' * 5)
for produto in produtos:
    if produto['Preço'] > media:
        print(f"{produto['Nome']} - R$ {produto['Preço']:.2f}")

print('=' * 5, 'Valor Abaixo da Média', '=' * 5)
for produto in produtos:
    if produto['Preço'] < media:
        print(f"{produto['Nome']} - R$ {produto['Preço']:.2f}")