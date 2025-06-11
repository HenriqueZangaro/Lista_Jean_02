termo = int(input('Digite a quantidade de termos que deseja calculaar a Série de Fibonacci: '))
n1 = n2 = 1
soma = 2
print(f'{1} {1} ', end='')
for i in range(n1, termo - 1):
    print(f'{soma}', end=' ')
    n1 = n2
    n2 = soma
    soma = n1 + n2
