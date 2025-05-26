# Primeiro país
nome_pais_A = input('Digite o nome do primeiro país: ').strip()
pais_A = int(input("Insira o valor da sua população: "))
while pais_A <= 0:
    print('\033[31mEntrada inválida!\033[0m')
    pais_A = int(input("Insira o valor correto da sua população: "))
taxa_A = int(input('Informe a taxa de crescimento dessa população, em porcentagem e sem o símbolo(ex: 4, se for 4%): '))
while taxa_A <= 0:
    print('\033[31Entrada inválida!\033[0m')
    taxa_A = int(input('Informe a taxa de crescimento dessa população, em porcentagem e sem o símbolo(ex: 4, se for 4%): '))
taxa_A = 1 + (taxa_A / 100)
# Segundo país
nome_pais_B = input('Digite o nome do segundo país: ').strip()
pais_B = int(input("Insira o valor da sua população: "))
while pais_B <= 0:
    print('\033[31mEntrada inválida!\033[0m')
    pais_B = int(input("Insira o valor correto da sua população: "))
taxa_B = int(input('Informe a taxa de crescimento dessa população, em porcentagem e sem o símbolo(ex: 4, se for 4%): '))
while taxa_B <= 0:
    print('\033[31Entrada inválida!\033[0m')
    taxa_A = int(input('Informe a taxa de crescimento dessa população, em porcentagem e sem o símbolo(ex: 4, se for 4%): '))
taxa_B = 1 + (taxa_B / 100)
cont_anos = 0
# Lógica de crescimento populaiconal
if pais_A == pais_B:
    print('Populações iguais! Inválido!')
    print('Reinicie o programa!')
    exit()
if (pais_A > pais_B and taxa_A > taxa_B) or (pais_B > pais_A and taxa_B > taxa_A) or (pais_A > pais_B and taxa_A == taxa_B) or (pais_B > pais_A and taxa_B == taxa_A):
    print('Dados inválidos! A população nunca será alcançada!')
    exit()
if pais_A < pais_B:
    while pais_A < pais_B:
        pais_A = pais_A * taxa_A
        pais_B = pais_B * taxa_B
        cont_anos += 1
else:
    while pais_B < pais_A:
        pais_A = pais_A * taxa_A
        pais_B = pais_B * taxa_B
        cont_anos += 1

if pais_A > pais_B:
    print(f'O(a) {nome_pais_A} demorou {cont_anos} anos para alcançar uma população de {pais_A:.0f} habitantes, passando o(a) {nome_pais_B}, com {pais_B:.0f} habitantes.')
elif pais_B > pais_A:
    print(f'O(a) {nome_pais_B} demorou {cont_anos} anos para alcançar uma população de {pais_B:.0f} habitantes, passando o(a) {nome_pais_A}, com {pais_A:.0f} habitantes.')
else:
    print(f'Em {cont_anos} anos, ambos os países igualaram a população, com {pais_A} habitantes.')