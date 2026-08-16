    # Exercício 023 — Documentação
'''Utilize datetime e descubra: Dia, Mes e Ano. 
Depois calcule a idade aproximada do usuário.'''
from datetime import date

hoje = date.today()

while True:
    nome = input('Digite seu nome: ').strip().capitalize()
    if nome != '' and nome.isalpha():
        break
    print('Nome inválido! Digite apenas letras.')

while True:
    try:
        dia = int(input('Dia de nascimento: '))
        mes = int(input('Mês de nascimento: '))
        ano = int(input('Ano de nascimento: '))

        nascimento = date(ano, mes, dia)
        break
    except ValueError:
        print('Data inválida! Digite uma data válida.')
        
idade = hoje.year - nascimento.year
if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
    idade -= 1

print(f'{nome}, você tem {idade} anos.')