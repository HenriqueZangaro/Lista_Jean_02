from time import sleep
nota = int(input("Digite a nota do aluno (entre 0 e 10): "))
while nota not in range(0, 11):
    print('\033[31mDigite um valor válido!\033[0m')
    sleep(1)
    nota = int(input("Digite a nota do aluno entre 0 e 10: "))

print(f'A nota informada foi {nota}')
