pais_A = 80000
taxa_A = 1.03
pais_B = 200000
taxa_B = 1.015
cont_anos = 0
while pais_A < pais_B:
    pais_A = pais_A * taxa_A
    pais_B = pais_B * taxa_B
    cont_anos += 1

if pais_A > pais_B:
    print(f'O país A demorou {cont_anos} anos para alcançar uma população de {pais_A:.0f} habitantes, passando o país B, com {pais_B:.0f} habitantes.')
else:
    print(f'O país A demorou {cont_anos} anos para alcançar uma população de {pais_A:.0f} habitantes, igualando a população do país B.')