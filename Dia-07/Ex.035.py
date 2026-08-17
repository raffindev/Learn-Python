    # Exercício 35 — Biblioteca da Semana - Tema: datetime + calendar
'''Pesquise na documentação: - weekday() - monthrange() - isleap()
1 - Faça um programa que: - Receba um ano 
2 - Informe:
- se é bissexto
- quantos dias fevereiro possui
- dia da semana do primeiro dia do ano'''
import datetime
import calendar

ano = int(input('Informe um ano: '))

# Usando isleap pra retornar se o ano é bissexto.
bissexto = calendar.isleap(ano) 
if bissexto == True:
    print(f'O ano {ano} é um ano bissexto')
else:
    print(f'O ano {ano} não é um ano bissexto')

# Usando monthrange(ano, mes) pra retornar o mes que desejo ver quantos dias tem.
fevereiro = calendar.monthrange(ano, 2)[1]
print(f'Fevereiro tem {fevereiro} dias')

# datetime.date(ano, mes, dia).weekday() pra retornar o primeiro dia do ano
diaprimeiro = datetime.date(ano, 1, 1).weekday()
dias = [ # Criei uma lista por extenso pois datetime.date retorna em numeros de 0 a 6
    'segunda-feira',
    'terça-feira',
    'quarta-feira',
    'quinta-feira',
    'sexta-feira',
    'sábado',
    'domingo'
]

print(f'O primeiro dia do ano de {ano} foi {dias[diaprimeiro]}.')