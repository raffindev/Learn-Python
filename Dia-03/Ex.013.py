    # Exercício 013 — ( Revisão ) + Lambda
'''Seu exercício, cadastre 5 produtos. Cada produto deve possuir (Produto, Preço). Ao final mostre:
- todos os produtos;
- produto mais caro utilizando max(..., key=lambda ...);
- produto mais barato utilizando min(..., key=lambda ...).'''
produtos = []

for i in range(5):
    produto = {}
    produto['Produto'] = input('Produto: ').capitalize()
    produto['Preço'] = float(input('Preço: R$ '))
    produtos.append(produto)

mais_caro = max(produtos, key=lambda produto: produto['Preço'])
mais_barato = min(produtos, key=lambda produto: produto['Preço'])

for produto in produtos:
    print(f"{produto['Produto']:.<10} R$ {produto['Preço']:.2f}")

print(f"O produto mais caro: {mais_caro['Produto']} R$ {mais_caro['Preço']:.2f}")
print(f"O produto mais barato: {mais_barato['Produto']} R$ {mais_barato['Preço']:.2f}")