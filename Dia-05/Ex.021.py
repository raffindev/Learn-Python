    # Exercício 021 — ( Revisão ) + Try/Except
'''Cadastre 5 pessoas, utilize ( Try, Except ) para impedir que o programa quebre 
caso o usuário digite uma idade invalida. Ao final mostre:
- todas as pessoas;
- média das idades;
- pessoa mais velha;
- pessoa mais nova.'''

pessoas = []
# Cadastro
for i in range(5):
    pessoa = {}
    pessoa['Nome'] = input('Nome: ').capitalize().strip()

    while True:
        try:
            pessoa['Idade'] = int(input('Idade: '))
            break
        except ValueError:
            print('Digite apenas números inteiros. ')
            
    pessoas.append(pessoa)

# Contadores
media = sum(pessoa['Idade'] for pessoa in pessoas) / len(pessoas)
maisvelha = max(pessoas, key=lambda pessoa: pessoa['Idade'])
maisnova = min(pessoas, key=lambda pessoa: pessoa['Idade'])

print('='*5, 'Pessoas', '='*5)
for i, pessoa in enumerate(pessoas):
    print(f"{i+1}. {pessoa['Nome']:<7} - {pessoa['Idade']} anos")
print(f'A média de idade das pessoas é de: {media:.2f} anos')
print(f"A pessoa mais velha é {maisvelha['Nome']} com {maisvelha['Idade']} anos")
print(f"A pessoa mais nova é {maisnova['Nome']} com {maisnova['Idade']} anos")