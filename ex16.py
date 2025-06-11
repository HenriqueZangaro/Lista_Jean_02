n1 = n2 = 1
soma = 2
print(f'{1} {1} ', end='')
while soma < 500:
    print(f'{soma}', end=' ')
    n1 = n2
    n2 = soma
    soma = n1 + n2
print(f'{soma}')