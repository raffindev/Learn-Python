    # Exercício 36 — Tratamento de Erros
'''Você receberá os seguintes campos: Nome - CPF - Telefone - Idade - Email
Crie TODAS as validações que conseguir imaginar.'''

cadastro = []

# Tratamento do nome
while True:
    pessoa = {}

    while True:
        pessoa['Nome'] = input('Nome: ').title().strip()
        if pessoa['Nome'] == '':
            print('O nome não pode estar em branco.')
        elif not pessoa['Nome'].replace(' ', '').isalpha():
            print('O nome não pode conter números ou símbolos.')
        else:
            break

    # Tratamento da idade
    while True:
        try:
            pessoa['Idade'] = int(input('Idade: '))
            if pessoa['Idade'] <= 0 or pessoa['Idade'] > 120:
                print('A idade deve ser maior que 0 e menor ou igual a 120.')
            else:
                break
        except ValueError:
            print('A idade deve conter apenas números.')

    # Tratamento do e-mail
    while True:
        pessoa['Email'] = input('E-mail: ').lower().strip()
        if '@' in pessoa['Email']:
            apos_arroba = pessoa['Email'].split('@')[1]
            if '.' in apos_arroba:
                break

        print('E-mail inválido.')

    # Tratamento de telefone
    while True:
        try:
            pessoa['Telefone'] = input('Telefone: ').strip()
            if pessoa['Telefone'].isdigit() and 8 <= len(pessoa['Telefone']) <= 12:
                break
            else:
                print('Número de telefone inválido. Digite apenas números, entre 8 e 12 dígitos.')
        except ValueError:
            print('Precisa conter apenas números')
        
    # Tratamento do CPF
    while True:
        pessoa['Cpf'] = input('CPF: ').strip()
        if not pessoa['Cpf'].isdigit():
            print('O CPF deve conter apenas números.')
        elif len(pessoa['Cpf']) != 11:
            print('O CPF informado deve ter 11 dígitos.')
        else:
            break

    cadastro.append(pessoa)
    print('Cadastro realizado com sucesso!')
    break