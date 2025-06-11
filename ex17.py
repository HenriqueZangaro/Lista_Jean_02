num = int(input('Informe o número inteiro que deseja calcular o fatorial: '))
resultado = num
# For para mostrar como é calculado o fatorial
print(f'{num}! = ', end='')
for i in range(num, 1, -1):
    print(f'{i} x ', end='')
print(f'{1} = ', end='')
# For para calcular o valor do fatorial

for i in range(num - 1, 0, -1):
    resultado = resultado * i
print(f'\033[32m{resultado}\033[0m')
