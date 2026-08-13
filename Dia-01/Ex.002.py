    # Exercício 002 (Revisão)
'''Crie um dicionário para armazenar (NOME - IDADE - CIDADE).
Os dados devem ser informados pelo usuário. Depois mostre todas as informações usando um for.'''
dados = {}

dados['Nome:'] = input('Nome: ').capitalize().strip()
dados['Idade:'] = int(input('Idade: '))
dados['Cidade:'] = input('Cidade: ').title()

for k, v in dados.items():
    print(k, v)