# SIMULADOR DE CAIXA ELETRÔNICO COM DIFERENTES SAÍDAS DE CÉDULAS, CONFORME O VALOR SOLICITADO
valor = int(input('Valor desejado. R$ '))
while valor % 10 != 0:
    print('Notas disponíveis: 100, 50, 20 e 10.')
    valor = int(input('Valor desejado. R$ '))
    if valor % 10 == 0:
        break
cem = cinq = vint = dez = 0
ced = 50
if valor <= 400:
    cinq = int((valor / 2) // 50)
    valor -= cinq * 50
    ced = 20
if valor > 400 and valor <= 1200:
    cem = (valor - 400) // 100
    valor -= cem * 100
if valor > 1200:
    cem = int((valor / 2) // 100)
    valor -= cem * 100
    cinq = int((valor / 2) // 50)
    valor -= cinq * 50
    ced = 20
total = valor
while True:
    if ced <= total:
        if ced == 50:
            cinq += 1
        if ced == 20:
            vint += 1
        if ced == 10:
            dez += 1
        total -= ced
    else:
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
    if total == 0:
       break
if cem > 0:
    print(f'{cem} notas de R$ 100,00')
if cinq > 0:
    print(f'{cinq} notas de R$ 50,00')
if vint > 0:
    print(f'{vint} notas de R$ 20,00')
if dez > 0:
    print(f'{dez} notas de R$ 10,00')
print('Obrigado e até breve.')
