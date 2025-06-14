from time import sleep
cont = 1
lista = []
print('Olá, vamos calcular uma soma de números!')
sleep(0.5)
print('Insira apenas números entre 0 e 1000.')
sleep(1)
while True:
    num = int(input(f'Informe o {cont}° número: '))
    while num not in range(0, 1001):
        num = int(input('Digite apenas números entre 0 e 1000! Informe o {cont}° número: '))
    lista.append(num)
    cont += 1
    qc = str(input('Deseja informar mais um número? [S/N]: ')).upper()[0]
    if qc not in 'SN':
        qc = str(input('Informe corretamente! Deseja informar mais um número? [S/N]: ')).upper()[0]
    if qc == 'N':
        break
print('Calculando...')
sleep(2)
print(f'O maior valor digitado foi o número {max(lista)}')
sleep(1)
print(f'O menor valor digitado foi o número {min(lista)}')
sleep(1)
print(f'A soma de todos os valores digitados é {sum(lista)}')
