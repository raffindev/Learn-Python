    # Exercício 029 — Laboratório de Tratamento de Erros
'''Objetivo: Não criar sistema. Somente tratar erros. Crie um cadastro contendo:
- nome - idade - emaill - senha - salario
Faça o máximo de validações possíveis.'''
cadastro = []

while True:
    pessoa = {}
    #Tratamento de nome
    while True:
        pessoa['Nome'] = input('Nome: ').title().strip()
        if pessoa['Nome'] == '':
            print('O nome não pode estar vazio.')
        elif not pessoa['Nome'].replace(' ', '').isalpha():
            print('O nome deve conter apenas letras.')
        else:
            break

    # Tratamento de Idade
    while True:
        try:
            pessoa['Idade'] = int(input('Idade: '))
            if pessoa['Idade'] <= 0:
                print('Idade deve ser maior que 0.')
            else:
                break
            
        except ValueError:
            print('Digite apenas números inteiros.')

    # Tratamento de Email
    while True:
        pessoa['email'] = input('Digite seu email: ').lower()
        if "@" in pessoa['email'] and pessoa['email'].index("@") < pessoa['email'].index("."):
            break
        else:
            print("E-mail inválido")

    # Tratamento de Senha
    while True:
        pessoa['Senha'] = input('Digite sua senha: ')
        if len(pessoa['Senha']) < 8:
            print('A senha precisa ter pelo menos 8 caracteres.')
        elif not any(c.isupper() for c in pessoa['Senha']):
            print('A senha precisa conter pelo menos uma letra maiúscula.')
        elif not any(c.isdigit() for c in pessoa['Senha']):
            print('A senha precisa conter pelo menos um número.')
        elif not any(not c.isalnum() for c in pessoa['Senha']):
            print('A senha precisa conter pelo menos um símbolo.')
        else:
            break

    # Tratamento de Salário
    while True:
        try:
            pessoa['Salario'] = float(input('Digite seu Salário: R$ '))
            if pessoa['Salario'] <= 0:
                print('O valor do salário deve ser positivo')
            else:
                break
        except ValueError:
            print('Digite um valor de salário válido.')

    print('Cadastro Concluido com Sucesso')
    break