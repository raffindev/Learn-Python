    # Exercício 003 (Revisão)
'''Crie uma lista com 10 números digitados pelo usuário.
Depois utilize enumerate() para mostrar:'''
numeros = []

# fiz assim em vez de for c < range(10): pra fixar outros modos de usar while
while len(numeros) < 10: # outro metodo usando while seria while contador < 10: mas ai criaria a variavel contador.
    numeros.append(int(input('Digite um número: ')))

print(f'\n{numeros}')
for i, (numeros) in enumerate(numeros):
    print(f'Posição {i} - numero {numeros}')