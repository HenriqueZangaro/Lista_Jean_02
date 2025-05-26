lista = []
for n in range(1, 6):
    num = int(input(f'Digite o {n}° número: '))
    lista.append(num)

soma = sum(lista)
print(f'A soma dos números digitados é {soma}')
