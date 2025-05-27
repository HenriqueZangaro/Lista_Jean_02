base = int(input('Informe a base: '))
expo = int(input('Informe o expoente: '))
resultado = base
for i in range(expo - 1):
    resultado = resultado * base

print(f'{base} elevado à potência {expo} resulta em {resultado}')
