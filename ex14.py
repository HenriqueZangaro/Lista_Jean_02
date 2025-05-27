lista_geral = []
lista_pares = []
lista_impares = []

for i in range(1, 11):
    num = int(input(f'Digite o {i}° número: '))
    lista_geral.append(num)

for i in lista_geral:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)

print(f'Entre os números digitados, há {len(lista_pares)} números pares, que são:')
for i in lista_pares:
    print(f'{i} ', end='')
print()
print(f'Além disso, foram digitados {len(lista_impares)} ímpares, que são:')
for i in lista_impares:
    print(f'{i} ', end='')
print()
