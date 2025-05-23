from time import sleep


usuario = str(input('Digite o usuário: '))
senha = str(input('Digite a senha: '))
print('VERIFICANDO...')
sleep(1)
while usuario == senha:
    print('\033[31mO usuário não pode ser igual a senha!\033[0m')
    sleep(1)
    usuario = str(input('Digite o usuário: '))
    senha = str(input('Digite a senha: '))
    print('VERIFICANDO...')
    sleep(1)

print('\033[32mLogin feito!\033[0m')
