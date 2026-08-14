    # Exercício 019 — ( Desafio ) - Sistema de Estoque
'''Cadastre produtos contendo: (NOME - QUANTIDADE - PREÇO). Ao finalizar:
- Mostrar todos os produtos.
- Valor total do estoque.
- Produto com maior quantidade.
- Produto mais caro.
- Quantos produtos têm estoque menor que 5 unidades.'''
mercado = []

# Cadastro Produto + Validação
while True:
    produto = {}

    produto['Nome'] = input('Produto: ').title().strip()

    produto['Qntd'] = int(input('Quantidade: '))
    while produto['Qntd'] <= 0:
        print('Quantidade inválida!')
        produto['Qntd'] = int(input('Quantidade: '))

    produto['Preço'] = float(input('Preço: R$ '))
    while produto['Preço'] <= 0:
        print('Preço inválido!')
        produto['Preço'] = float(input('Preço: R$ '))

    mercado.append(produto)

    while True:
        cadastrar = input('Gostaria de Cadastrar outro produto? [S/N]: ').upper()[0]
        if cadastrar in ('S', 'N'):
            break
    if cadastrar == 'N':
        break

# Variaveis
valor_total = sum(produto['Qntd'] * produto['Preço'] for produto in mercado)
maior = max(mercado, key=lambda produto: produto['Qntd'])
caro = max(mercado, key=lambda produto: produto['Preço'])

# Visualização
print()
print('='*15, 'MERCADO', '='*15)
print('No. Produto - Qntd - Preço R$')
for i, produto in enumerate(mercado):
    print(f"{i+1}.  {produto['Nome']:<10} {produto['Qntd']:<5} R$ {produto['Preço']:.2f}")

print(f'\nValor total do Estoque: {valor_total:.2f}')
print(f"O produto com maior estoque é: {maior['Nome']} com {maior['Qntd']} de itens")
print(f"O produto mais caro é: {caro['Nome']} custando R$ {caro['Preço']:.2f}")

print('\nProdutos com menos de 5 items no estoque:')
for produto in mercado:
    if produto['Qntd'] < 5:
        print(f"Produto: {produto['Nome']} - Qntd: {produto['Qntd']}")