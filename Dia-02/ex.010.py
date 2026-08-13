    # Exercício 010 — ( Revisão ) - Sistema de Caixa de Mercado.
'''O mercado possui vários produtos. O usuário poderá cadastrar produtos informando (Produto - Preço)
Ao finalizar os cadastros, o programa deve mostrar:
- Quantos produtos foram cadastrados.
- Valor total da compra.
- Produto mais caro.
- Produto mais barato.
- Quantos produtos custam mais de R$100.'''
mercado = []
cont = maisde100 = 0

while True:
    produto = {}
    produto['Produto'] = input('Digite o Produto: ')
    produto['Preço'] = float(input('Preço: R$ '))
    cont += 1
    if produto['Preço'] > 100:
        maisde100 += 1
    mercado.append(produto)

    while True:
        cadastrar = input('Gostaria de cadastrar outro produto? [S/N] ').upper()
        if cadastrar in ('S', 'N'):
            break
    if cadastrar == 'N':
        break

soma = sum(produto['Preço'] for produto in mercado)
mais_caro = max(mercado, key=lambda produto: produto['Preço'])
mais_barato = min(mercado, key=lambda produto: produto['Preço'])

print(f'='*5, 'Compra', '='*5)
for i, produto in enumerate(mercado, start=1):
    print(f"{i}. {produto['Produto']:<10} Preço R$: {produto['Preço']:.2f}")

print(f'\nTem {cont} produtos cadastrados.')
print(f'O valor total da compra foi de: {soma:.2f}')
print(f"Mais caro: {mais_caro['Produto']} - R$ {mais_caro['Preço']}")
print(f"Mais barato: {mais_barato['Produto']} - R$ {mais_barato['Preço']}")
print(f'Tem {maisde100} produtos que custam mais de R$ 100')