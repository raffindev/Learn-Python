    # Exercício 009 — ( Revisão ) - Sistema de login
'''Cadastre: (Usuario - Senha)
Depois o sistema deve solicitar login. O usuário terá no máximo 3 tentativas para acertar.
Se acertar - Login realizado com sucesso. Se errar 3 vezes - Conta bloqueada.'''

cadastro = {}
tentativa = 0

cadastro['Login'] = input('Digite seu login: ')
while True:
    cadastro['Senha'] = input('Escolha uma senha entre 8 e 12 caracteres: ')
    if 8 <= len(cadastro['Senha']) <= 12:
        break

    print('A senha deve ter entre 8 e 12 caracteres!')

print('Faça o login')
usuario = input('Usuário: ')
while True:
    senha = input('Informe sua senha: ')
    if senha != cadastro['Senha']:
        tentativa += 1

        if tentativa < 3:
            print('Senha inválida. Tente novamente')
        else:
            print('Conta bloqueada')
            break
    else:
        print('Bem-vindo')
        break