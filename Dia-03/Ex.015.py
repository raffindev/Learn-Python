    # Exercício 015 — ( Desafio ) - Sistema de Agenda
'''Crie uma agenda simples, cada contato deve possuir: (Nome - Telefone.)
O usuário poderá cadastrar vários contatos. Ao final o programa deverá:
- Mostrar todos os contatos.
- Permitir pesquisar um nome.
- Informar se o contato existe.
- Mostrar o telefone correspondente.'''

# Cadastro
agenda = []

while True:
    contato = {}
    contato['Nome'] = input('Nome: ').title().strip()
    contato['Telefone'] = input('Telefone: ')
    if len(contato['Telefone']) == 9 and contato['Telefone'].isdigit():
        agenda.append(contato)
    else:
        print('O telefone precisa ter 9 números.')
    
# Validação Cadastro
    while True:
        cadastrar = input('Gostaria de cadastrar outro contato? [S/N] ').upper()
        if cadastrar in ('S', 'N'):
            break
        else:
            print('Opção inválida. Digite [S/N]')
    if cadastrar == 'N':
        break

print()
print('='*10, 'AGENDA', '='*10)
for pos, contato in enumerate(agenda, start=1):
    print(f'{pos}. Nome: {contato['Nome']} - Tel: {contato['Telefone']:<15}')

# Pesquisar na Agenda
while True:
    nome = input('Nome do Contato que gostaria de pesquisar: ').title().strip()
    if nome in ('0', 'Fim'):
        break

    encontrado = False

    for contato in agenda:
        if nome == contato['Nome']:
            print(f"O Contato escolhido é: {contato['Nome']} com telefone: {contato['Telefone']}")
            encontrado = True
            break

    if encontrado == False:
        print('Contato Inexistente')