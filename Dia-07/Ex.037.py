    # Exercício 37 — Funcionários da Empresa — Lambda + Any + List Comprehension
'''Cadastre funcionários: Nome - Cargo - Salário - Ano de Empresa
- Any - verificar se ja tem usuário cadastrado com o mesmo nome
- Lambda - funcionario mais antigo - funcionario mais novo - maior salário - menor salário
- Lambda - Criar um ranking por salário - Do maior pro menor
- List Comprehension - Crie listas contendo:
salários acima da média;
funcionários com mais de 5 anos;
funcionários com menos de 2 anos;
cargos que contenham a palavra "Analista".
Depois Mostre - Média - diferença entre maior e menor'''
from statistics import mean

funcionarios = []

while True:
    funcionario = {}
    while True:
        funcionario['Nome'] = input('Nome: ').title().strip()
        if any(f['Nome'] == funcionario['Nome'] for f in funcionarios):
            print('Funcionário já cadastrado!')
            continue

        if funcionario['Nome'] == '':
            print('Nome inválido! Não pode conter espaços.')
        elif not funcionario['Nome'].replace(' ','').isalpha():
            print('Nome inválido! Não pode conter números ou símbolos.')
        else:
            break

    while True:
        funcionario['Cargo'] = input('Cargo: ').title().strip()
        if not funcionario['Cargo'].replace(' ','').isalnum():
            print('Cargo inválido.')
        else:
            break
    
    while True:
        try:
            funcionario['Salario'] = float(input('Salário: R$ '))
            if funcionario['Salario'] <= 0:
                print('Digite um salário válido.')
            else:
                break
        except ValueError:
            print('Somente números são aceitos.')
    
    while True:
        try:
            funcionario['Ano'] = int(input('Anos de Empresa: '))
            if funcionario['Ano'] <= 0:
                print('Tempo de empresa inválido.')
            else:
                break
        except ValueError:
            print('Somente números inteiros são aceitos.')

    funcionarios.append(funcionario)
    print('Funcionário cadastrado com sucesso!\n')

    while True:
        cadastrar = input('Deseja cadastrar outro funcionário? [S/N] ').upper()
        if cadastrar in ('S', 'N'):
            break
    if cadastrar == 'N':
        break

# Quantitativos - Lambda
antigo = max(funcionarios, key=lambda funcionario: funcionario['Ano'])
novo = min(funcionarios, key=lambda funcionario: funcionario['Ano'])
menor_salario = min(funcionarios, key=lambda funcionario: funcionario['Salario'])
maior_salario = max(funcionarios, key=lambda funcionario: funcionario['Salario'])
salarios = sorted(funcionarios, key=lambda funcionario: funcionario['Salario'], reverse=True)
diferença = maior_salario['Salario'] - menor_salario['Salario']

# List Comprehension
media = mean(funcionario['Salario'] for funcionario in funcionarios)
acima_media = [funcionario for funcionario in funcionarios if funcionario['Salario'] > media]
acima_5anos = [funcionario for funcionario in funcionarios if funcionario['Ano'] > 5]
abaixo_2anos = [funcionario for funcionario in funcionarios if funcionario['Ano'] < 2]
cargo_analista = [funcionario for funcionario in funcionarios if "Analista" in funcionario['Cargo']]

# Visualização
print('\n' + '=' * 50)
print('LISTA DE FUNCIONÁRIOS'.center(50))
print('=' * 50)

for i, funcionario in enumerate(funcionarios, 1):
    print(f'{i}º Funcionário')
    print(f"Nome: {funcionario['Nome']}")
    print(f"Cargo: {funcionario['Cargo']}")
    print(f"Salário: R$ {funcionario['Salario']:.2f}")
    print(f"Anos de Empresa: {funcionario['Ano']}")
    print('-' * 50)

print(f'\nQuantidade de funcionários cadastrados: {len(funcionarios)}')

print('\nQUANTITATIVOS')
print(f"Funcionário mais antigo: {antigo['Nome']} - {antigo['Ano']} anos")
print(f"Funcionário mais novo: {novo['Nome']} - {novo['Ano']} anos")
print(f"Menor salário: {menor_salario['Nome']} - R$ {menor_salario['Salario']:.2f}")
print(f"Maior salário: {maior_salario['Nome']} - R$ {maior_salario['Salario']:.2f}")
print(f"A média salarial da empresa é: {media:.2f}")
print(f"A diferença entre o maior e menor salário são: {diferença:.2f}")

print('\nFUNCIONÁRIOS POR SALÁRIO (MAIOR → MENOR)')
for funcionario in salarios:
    print(f"{funcionario['Nome']} - R$ {funcionario['Salario']:.2f}")

print('\n' + '=' * 50)
print('FUNCIONÁRIOS ACIMA DA MÉDIA SALARIAL'.center(50))
print('=' * 50)

for i, funcionario in enumerate(acima_media, start=1):
    print(f'{i}º Funcionário')
    print(f"Nome: {funcionario['Nome']}")
    print(f"Cargo: {funcionario['Cargo']}")
    print(f"Salário: R$ {funcionario['Salario']:.2f}")
    print(f"Anos de Empresa: {funcionario['Ano']}")
    print('-' * 50)

print(f'Quantidade: {len(acima_media)}')

# Mais tempo de empresa
print('\n' + '=' * 50)
print('FUNCIONÁRIOS COM MAIS DE 5 ANOS DE EMPRESA'.center(50))
print('=' * 50)

for i, funcionario in enumerate(acima_5anos, start=1):
    print(f'{i}º Funcionário')
    print(f"Nome: {funcionario['Nome']}")
    print(f"Cargo: {funcionario['Cargo']}")
    print(f"Salário: R$ {funcionario['Salario']:.2f}")
    print(f"Anos de Empresa: {funcionario['Ano']}")
    print('-' * 50)

print(f'Quantidade: {len(acima_5anos)}')

# Menos tempo de empresa
print('\n' + '=' * 50)
print('FUNCIONÁRIOS COM MENOS DE 2 ANOS DE EMPRESA'.center(50))
print('=' * 50)

for i, funcionario in enumerate(abaixo_2anos, start=1):
    print(f'{i}º Funcionário')
    print(f"Nome: {funcionario['Nome']}")
    print(f"Cargo: {funcionario['Cargo']}")
    print(f"Salário: R$ {funcionario['Salario']:.2f}")
    print(f"Anos de Empresa: {funcionario['Ano']}")
    print('-' * 50)

print(f'Quantidade: {len(abaixo_2anos)}')

# Cargo Analista
print('\n' + '=' * 50)
print('FUNCIONÁRIOS DO CARGO DE ANALISTA'.center(50))
print('=' * 50)

for i, funcionario in enumerate(cargo_analista, start=1):
    print(f'{i}º Funcionário')
    print(f"Nome: {funcionario['Nome']}")
    print(f"Cargo: {funcionario['Cargo']}")
    print(f"Salário: R$ {funcionario['Salario']:.2f}")
    print(f"Anos de Empresa: {funcionario['Ano']}")
    print('-' * 50)

print(f'Quantidade: {len(cargo_analista)}')