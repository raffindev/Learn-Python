    # Exercício 5 (Desafio) - Cadastro de Pessoas
'''Crie um sistema que permita cadastrar pessoas. Para cada pessoa (Nome - Idade).+
O usuário decide se deseja continuar cadastrando. Ao final mostre:

Quantas pessoas foram cadastradas.
Média de idade.
Nome da pessoa mais velha.
Nome da pessoa mais nova.'''
cadastro = []
soma = 0

while True:
    pessoa = []
    pessoa.append(input('Digite o nome: ').capitalize().strip())
    pessoa.append(int(input('Digite a idade: ')))
    cadastro.append(pessoa)
    soma += pessoa[1]

    while True:
        continuar = input('Deseja cadastrar outra pessoa? [S/N]: ').upper()
        if continuar in ('S', 'N'):
            break
        else:
            print('Opção invalidade, por favor digite S ou N')
    if continuar == 'N':
        break

media = soma / len(cadastro)
mais_velha = pessoa
mais_nova = pessoa    

for pessoa in cadastro:
    if pessoa[1] > mais_velha[1]:
        mais_velha = pessoa

    if pessoa[1] < mais_nova[1]:
        mais_nova = pessoa
        
print(f'\nTem {len(cadastro)} pessoas Cadastradas\n')
print('-'*5, 'LISTA PESSOAS CADASTRADAS', '-'*5)
for indice, (pes, idade) in enumerate(cadastro):
    print(f'{pes} - {idade} anos')
print(f'A média de idade das pessoas é {media:.0f} anos')
print(f'A pessoa mais velha é {mais_velha[0]} com {mais_velha[1]} anos')
print(f'A pessoa mais nova é {mais_nova[0]} com {mais_nova[1]} anos')