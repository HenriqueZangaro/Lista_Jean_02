soma = 0
n1 = int(input('Digite o início do intervalo: '))
n2 = int(input('Digite o fim do intervalo: '))

print('Os números compreendidos no intervalo são: ', end='')

for i in range(n1, n2 + 1):
    print(f'{i}...', end='')
    soma += i
print()
print(f'A soma dos números é {soma}')
