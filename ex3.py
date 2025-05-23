nome = str(input('Digite seu nome: ')).strip()
while len(nome) <= 3:
    nome = str(input('Muito curto! Informe corretamente: '))
idade = int(input('Digite sua idade: '))


while idade not in range(0, 151):
    if idade < 0:
        idade = int(input('Idade negativa? SÉRIO?\nInforme a idade corretamente: '))
    else:
        idade = int(input('COMO VOCÊ AINDA ESTÁ VIVO?\nInforme a idade corretamente: '))


salario = float(input('Informe seu salário: R$'))
while salario <= 0:
    if salario < 0:
        salario = float(input('PAGANDO PARA TRABALHAR KKKK\nInforme o salário verdadeiro: R$'))
    else:
        salario = float(input('ESTAGIÁRIO KKKK\nInforme o salário verdadeiro: '))


sexo = str(input('Informe seu sexo: [M/F] ')).strip().lower()[0]
while sexo not in 'mf':
    sexo = str(input('NÃO BINÁRIE? KKKKK\nInforme o sexo corretamente: '))
if sexo == 'm':
    sexo = 'masculino'
else:
    sexo = 'feminino'

estado_civil = str(input('Informe seu estado civil:\nS (Solteiro(a))\nC (Casado(a))\nV (Viúvo(a))\nD (Divorciado)\n')).upper().strip()[0]
while estado_civil not in 'SCVD':
    estado_civil = str(input('Digita direito caraio:\nS (Solteiro(a))\nC (Casado(a))\nV (Viúvo(a))\nD (Divorciado)\n')).upper().strip()[0]
if sexo == 'masculino':
    if estado_civil == 'S':
        estado_civil = 'solteiro'
    elif estado_civil == 'C':
        estado_civil = 'casado'
    elif estado_civil == 'V':
        estado_civil = 'viúvo'
    elif estado_civil == 'D':
        estado_civil = 'divorciado'
else:
    if estado_civil == 'S':
        estado_civil = 'solteira'
    elif estado_civil == 'C':
        estado_civil = 'casada'
    elif estado_civil == 'V':
        estado_civil = 'viúva'
    elif estado_civil == 'D':
        estado_civil = 'divorciada'

print(f'Então, seu nome é {nome}, sua idade é {idade}, salário de R${salario}, sexo {sexo} e {estado_civil}. Que massa!')
