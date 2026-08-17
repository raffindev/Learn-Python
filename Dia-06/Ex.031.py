    # Exercício 031 — Desafio de Lógica
'''Sistema de Biblioteca. Cadastrar livros: Titulo - Autor - Ano - Quantidade. Ao final mostrar:
- livro mais antigo;
- livro mais novo;
- total de livros;
- quantidade total em estoque;
- livros publicados antes de 2000.'''
from datetime import date
ano_atual = date.today().year

biblioteca = []

while True:
    livro = {}
    # Cadastro e Tratamento Titulo
    while True:
        livro['Titulo'] = input('Titulo do livro: ').title().strip()
        duplicado = any(l['Titulo'] == livro['Titulo'] for l in biblioteca)
        if duplicado:
            print('Livro ja cadastrado.')
        elif livro['Titulo'] == '':
            print('O título não pode ficar em branco.')
        elif not livro['Titulo'].replace(' ', '').isalnum():
            print('O título não pode conter caracteres especiais.')
        else:
            break

    # Cadastro e Tratamento Autor
    while True:
        livro['Autor'] = input('Nome do Autor: ').title().strip()
        if livro['Autor'] == '':
            print('O nome do autor não pode ficar em branco.')
        elif not livro['Autor'].replace(' ', '').isalpha():
            print('Nome do autor inválido. Use apenas letras e espaços.')
        else:
            break

    # Cadastro e Tratamento Ano
    while True:
        try:
            livro['Ano'] = int(input('Digite o Ano: '))
            if livro['Ano'] <= 0 or livro['Ano'] > ano_atual:
                print('Ano inválido.')
            else:
                break
        except ValueError:
            print('O ano deve ser informado com números.')

    # Cadastro e Tratamento de Quantidade
    while True:
        try:
            livro['Qntd'] = int(input('Quantidade: '))
            if livro['Qntd'] <= 0:
                print('Quantidade inválida. Informe um valor maior que zero.')
            else:
                break
        except ValueError:
            print('A quantidade deve ser informada com números.')

    biblioteca.append(livro)

    # Cadastrar outro livro
    while True:
        cadastrar = input('Gostaria de cadastrar outro livro? [S/N] ').upper()
        if cadastrar in ('S', 'N'):
            break
        print('Opção inválida. Digite S para sim ou N para não.')
    if cadastrar == 'N':
        break

# Quantitativos
mais_novo = max(biblioteca, key=lambda livro: livro['Ano'])
mais_antigo = min(biblioteca, key=lambda livro: livro['Ano'])
total_estoque = sum(livro['Qntd'] for livro in biblioteca)
antes2000 = [livro for livro in biblioteca if livro['Ano'] < 2000]

# Visualização
print('=' * 15, 'BIBLIOTECA', '=' * 15)

for i, livro in enumerate(biblioteca):
    print(f"{i+1}º Titulo: {livro['Titulo']} - Ano: {livro['Ano']} - Autor: {livro['Autor']} - Qntd: {livro['Qntd']}")

print(f"\nO livro mais novo é {mais_novo['Titulo']} do ano {mais_novo['Ano']}")
print(f"O livro mais antigo é {mais_antigo['Titulo']} do ano {mais_antigo['Ano']}")
print(f"Tem {len(biblioteca)} livros registrados.")
print(f"Tem no total {total_estoque} livros no estoque.")

print('\n' + '=' * 5, 'LIVROS ANTES DE 2000', '=' * 5)

for livro in antes2000:
    print(f"Titulo: {livro['Titulo']} - Ano: {livro['Ano']}")