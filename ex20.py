while True:
    num = int(input('Informe o número inteiro que deseja calcular o fatorial (entre 0 e 16): '))
    while num not in range(0, 17):
        num = int(input('Fora do intervalo! Informe o número inteiro que deseja calcular o fatorial (entre 0 e 16): '))
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

    qc = str(input('Deseja calcular novamente? [S/N]: ')).upper()[0]
    while qc not in 'SN':
        qc = str(input('Insira corretamente! Deseja calcular novamente? [S/N]: ')).upper()[0]
    if qc == 'N':
        break
