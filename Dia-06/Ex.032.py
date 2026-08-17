    # Exercício 032 — Desafio de Lógica
'''Sistema de Reservas de Hotel. Cadastrar hóspedes: Nome - Dias hospedado - valor da diaria. Ao final mostrar:
- valor total de cada hospedagem;
- hospede que mais gastou;
- hospede que menos gastou;
- média dos gastos;
- hóspedes acima da média.'''
from statistics import mean

hotel = []

print('='*7, 'Check-in do Hóspede', '='*7)
while True:
    hospede = {}
# Cadastro e validação do hospede
    while True:
        hospede['Nome'] = input('Nome: ').capitalize().strip()

        if hospede['Nome'] == '':
            print('O nome não pode estar em branco.')
        elif not hospede['Nome'].replace(' ', '').isalpha():
            print('O nome não pode conter caracteres especiais.')
        else:
            break

    while True:
        try:
            hospede['Dias'] = int(input('Dias hospedados: '))

            if hospede['Dias'] <= 0:
                print('O número de dias deve ser maior que zero.')
            else:
                break
        except ValueError:
            print('Digite apenas um número inteiro válido.')

    while True:
        try:
            hospede['Valor'] = float(input('Valor da diária: '))

            if hospede['Valor'] <= 0:
                print('O valor da diária deve ser maior que zero.')
            else:
                break
        except ValueError:
            print('Digite apenas um valor numérico válido.')

    # Gasto total do hóspede = dias hospedados * valor da diária
    gasto_total = hospede['Dias'] * hospede['Valor']
    hospede['Total'] = gasto_total

    hotel.append(hospede)

    # Repitir
    while True:
        checkin = input('Gostaria de realizar check-in de outro hóspede? [S/N] ').upper()
        if checkin in ('S', 'N'):
            break
        print('Opção inválida. Digite S para sim ou N para não.')
    if checkin == 'N':
        break

# Quantitativos
mais_gastou = max(hotel, key=lambda hospede: hospede['Total'])
menos_gastou = min(hotel, key=lambda hospede: hospede['Total'])
media = mean(hospede['Total'] for hospede in hotel)
faturamento = sum(hospede['Total'] for hospede in hotel)

print()
print('='*7, 'Dados do Hóspede', '='*7)
for i, hospede in enumerate(hotel):
    print(f"{i+1}º. Nome: {hospede['Nome']} - Dias Hospedado: {hospede['Dias']} - Valor pago por diária: R$ {hospede['Valor']:.2f} - Valor total gasto: R$ {hospede['Total']:.2f}")

print(f"\nO hóspede que mais gastou foi {mais_gastou['Nome']} com total de R$ {mais_gastou['Total']:.2f}")
print(f"O hóspede que menos gastou foi {menos_gastou['Nome']} com total de R$ {menos_gastou['Total']:.2f}")
print(f"A média de valores gasto pelos hóspedes foi de: R$ {media:.2f}")
print(f"O faturamento total do hotel foi: {faturamento:.2f}\n")

print('='*7, 'Hóspedes acima da média', '='*7)
for i, hospede in enumerate(hotel):
    if hospede['Total'] > media:
        print(f"Nome: {hospede['Nome']} - Valor total gasto: R$ {hospede['Total']:.2f}")