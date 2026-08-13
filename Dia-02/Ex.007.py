    # Exercício 007 — ( Revisão )
'''Cadastre 5 alunos. Para cada aluno armazene: ( NOME, NOTA )
Utilize um dicionário para cada aluno. Ao final mostre:
- Aluno: João - Nota: 8.5
- Aluno: Maria - Nota: 7.0
Depois informe:
- média da turma;
- maior nota;
- nome do aluno com maior nota.'''
turma = []
soma = maior = 0

for i in range(5):
    aluno = {}
    aluno['Nome:'] = input('Nome: ').capitalize()
    aluno['Nota:'] = float(input('Nota: '))
    soma += aluno['Nota:']
    turma.append(aluno)
    print()

media = soma / len(turma)
for aluno in turma:
    if aluno['Nota:'] > maior:
        maior = aluno['Nota:']
        nome_maior = aluno['Nome:']

print(f'='*5, 'Alunos', '='*5)
for i, aluno in enumerate(turma, start=1):
    print(f"{i} - {aluno['Nome:']:<7} - Nota: {aluno['Nota:']:<5}")
print(f'\nA média da turma é {media:.2f}')
print(f'A melhor nota é {maior}')
print(f'O aluno com a melhor nota é {nome_maior}')