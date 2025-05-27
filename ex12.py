n = int(input('Informe qual número deseja saber a tabuada: '))

print(f"TABUADA DO {n}")
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
