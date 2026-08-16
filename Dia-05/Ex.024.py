    # Exercício 024 — ( Desafio ) - Sistema de Login
'''Cadastrar: Usuário - Email - Senha.
Validações: email deve conter @ - Senha minimo 8 digitos - usuário não pode estar vazio
Depois: logar - solicitar Usuário e Senha.
Validar logim, mostrar login realizado com sucesso, ou mostrar senha ou usuário inválidos.'''
cadastro = []

# Cadastro + Validação Usuario - Email - Senha
while True:
    pessoa = {}
    while True:
        pessoa['Usuario'] = input('Digite seu usuário: ')
        if pessoa['Usuario'] == '':
            print('Usuário não pode estar vazio')
        elif any(p['Usuario'] == pessoa['Usuario'] for p in cadastro):
            print('Esse usuário já existe! Digite outro.')
        else:
            break       

    while True:
        pessoa['email'] = input('Digite seu email: ')
        if '@' not in pessoa['email'] or '.com' not in pessoa['email']:
            print('Digite um email válido.')
        else:
            break

    while True:
        pessoa['senha'] = input('Digite uma senha : ')
        if pessoa['senha'] == '':
            print('A senha não pode estar vazia.')
        elif ' ' in pessoa['senha']:
            print('A senha não pode conter espaços.')
        elif 8 <= len(pessoa['senha']) <= 12: 
            break
        else:
            print('Sua senha precisa ter entre 8 e 12 digitos')
    
    cadastro.append(pessoa)
    print('Usuário cadastrado com sucesso!\n')

# Cadastrar outro usúario + validar S/N
    while True:
        cadastrar = input('Gostaria de cadastrar outra pessoa? [S/N]: ').upper()
        if cadastrar in ('N', 'S', 'SIM', 'NÃO'):
            break
        else:
            print('Opção inválida. Digite S/N')
    if cadastrar == 'N':
        break


# Login - Tentativas
tentativa = 0

print('='*7, 'LOGIN', '='*7)
while tentativa < 3:
    login = input('Usuário: ')
    senha = input('Senha: ')

    if any(p['Usuario'] == login and p['senha'] == senha for p in cadastro):
        print('Login realizado com sucesso')
        break
    else:
        print('Usuário ou senha inválidos')
        tentativa += 1

if tentativa == 3:
    print('Tentativas excedidas.')