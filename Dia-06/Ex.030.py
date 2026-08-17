    # Exercício 030 — Lambda + Any + List Comprehension
'''Cadastre produtos: ( Nome - Preço - Estoque )
Use LAMBDA para Encontrar: mais caro - mais barato - maior estoque.
Use ANY para verificar se já existe produto com o mesmo nome.
Use LIST COMPREHENSION para criar listas de:
- produtos acima de R$100;
- produtos com estoque menor que 5;
- produtos com estoque maior que 10.'''
produtos = []

while True:
    # Cadastro
    produto = {}
    while True:
        produto['Nome'] = input('Nome: ').title().strip()
        duplicado = any(p['Nome'] == produto['Nome'] for p in produtos)
        if duplicado == True:
            print('Ja existe esse produto')
        else:
            break

    while True:
        produto['Preço'] = float(input('Preço: R$ '))
        if produto['Preço'] <= 0:
            print('O preço precisa ser maior que 0')
        else:
            break

    while True:
        produto['Estoque'] = int(input('Quantidade no Estoque: '))
        if produto['Estoque'] <= 0:
                print('A quantidade no estoque precisa ser maior que 0')
        else:
            break

    produtos.append(produto)

    while True:
        cadastrar = input('Gostaria de cadastrar outro produto? [S/N] ').upper()
        if cadastrar in ('S', 'N'):
            break
    if cadastrar == 'N':
        break

# Lambda
mais_caro = max(produtos, key=lambda produto: produto['Preço'])
mais_barato = min(produtos, key=lambda produto: produto['Preço'])
maior_estoque = max(produtos, key=lambda produto: produto['Estoque'])

# List comprehension
acima100 = [produto for produto in produtos if produto['Preço'] > 100]
estoquebaixo = [produto for produto in produtos if produto['Estoque'] < 5]
estoquealto = [produto for produto in produtos if produto['Estoque'] > 10]

print('='*10, 'MERCADO', '='*10)
for i, produto in enumerate(produtos):
    print(f"{i+1}. {produto['Nome']} - R$ {produto['Preço']:.2f} - Qntd. {produto['Estoque']}")
print('='*30)
print(f'\nO produto mais caro é {mais_caro['Nome']} custando R$ {mais_caro['Preço']:.2f}')
print(f'O produto mais barato é {mais_barato['Nome']} custando R$ {mais_barato['Preço']:.2f}')
print(f'O produto com maior quantidade no estoque: {maior_estoque['Nome']} com {maior_estoque['Estoque']}')

# Produtos acima de R$ 100
print('\nProdutos acima de R$ 100:')
if acima100:
    for produto in acima100:
        print(f"- {produto['Nome']} — R$ {produto['Preço']:.2f}")
else:
    print('Nenhum produto acima de R$ 100.')


# Estoque baixo
print('\nProdutos com estoque baixo:')
if estoquebaixo:
    for produto in estoquebaixo:
        print(f"- {produto['Nome']} — {produto['Estoque']} unidades")
else:
    print('Nenhum produto com estoque baixo.')


# Estoque alto
print('\nProdutos com estoque alto:')
if estoquealto:
    for produto in estoquealto:
        print(f"- {produto['Nome']} — {produto['Estoque']} unidades")
else:
    print('Nenhum produto com estoque alto.')