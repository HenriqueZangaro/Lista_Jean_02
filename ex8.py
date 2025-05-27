media = 0
soma = 0
for n in range(1, 6):
    num = int(input(f'Digite o {n}° número: '))
    soma += num

media = soma / 5

print(f'A soma dos números digitados é {soma}. A média é {media:.1f}')
