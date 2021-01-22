print(('\033[34m= ' * 3), 'SIMULAÇÃO DE EMPRÉSTIMO BANCÁRIO = = =\033[m')
salario = float(input('Salário: R$ '))
valorImovel = int(input('Valor do imóvel: R$ '))
valorEntrada = int(input('Valor de entrada: R$ '))
anosParcela = int(input('Quantos anos vai parcelar? '))
totalMeses = anosParcela * 12
valorParcela = (valorImovel - valorEntrada) / totalMeses
valorFim = 0
valorFimPrimeiro = valorEntrada
valorFimUltimo = valorFimPrimeiro
valorCorrigido = 0
percentual = valorParcela * 100 / salario
cont = 0
if percentual >= 30:
    print(f'Valor da Parcela: \033[34mR$ {valorParcela:.2f}\033[m. Percentual do salário: \033[34m{percentual:.2f}%\033[m')
    print('\033[31mValor NEGADO\033[m')
else:
    print(f'Valor da Parcela: \033[34mR$ {valorParcela:.2f}\033[m. Percentual do salário: \033[34m{percentual:.2f}%\033[m')
    print('\033[32mValor APROVADO\033[m')
    anoInicio = int(input('Ano de início do pagamento: '))
    mesInicio = int(input('Mês de início do pagamento: '))
    inicioQuest = 14 - mesInicio
    anoQuest = anoInicio + 1
    cont += 1
    valorFimPrimeiro += (13 - mesInicio) * valorParcela
    valorFimUltimo = valorFimPrimeiro
    print(f'\033[33mPago até Dezembro {anoInicio}: R$ {valorFimPrimeiro:.2f}\033[m')
    if cont == anosParcela:
        valorCorrigido = valorImovel
        print('..::..' * 8)
        print(f'PERÍODO TOTAL DE PARCELAMENTO: \033[34m{cont} ano / {(cont) * 12} meses\033[m')
    elif cont != anosParcela:
        for r in range(inicioQuest, totalMeses + 1, 12):
            salario += salario * 5 / 100
            cont += 1
            if anoQuest % 2 == 1:
                pergunta = input(f'Próximo ano:\033[36m{anoQuest}\033[m  Aumento de juros? S / N ').strip().upper()
                if pergunta == 'N':
                    valorParcela += valorParcela * 7 / 100
                elif pergunta == 'S':
                    valorParcela += valorParcela * 10 / 100
            elif anoQuest % 2 == 0:
                valorParcela += valorParcela * 7 / 100
            valorFim += valorParcela * 12
            valorFimUltimo += valorParcela * 12
            percentual = valorParcela * 100 / salario
            if percentual >= 30:
                print(f'{r // 12 + 1}° ano / {r}° mês. \033[37mJANEIRO de {anoQuest}:\033[m')
                print(f'Salário: \033[34mR$ {salario:.2f}\033[m')
                print(f'Valor da parcela: \033[34mR$ {valorParcela:.2f}.\033[m')
                print(f'\033[31m{percentual:.2f}% Valor NEGADO\033[m')
                print(f'\033[33mPago até Dezembro de {anoQuest}: R$ {valorFimUltimo:.2f}\033[m')
            else:
                print(f'{r // 12 + 1}° ano / {r}° mês. \033[37mJANEIRO de {anoQuest}:\033[m')
                print(f'Salário: \033[34mR$ {salario:.2f}\033[m')
                print(f'Valor da parcela: \033[34mR$ {valorParcela:.2f}\033[m.')
                print(f'\033[32m{percentual:.2f}% Valor APROVADO\033[m')
                print(f'\033[33mPago até Dezembro de {anoQuest}: R$ {valorFimUltimo:.2f}\033[m')
            anoQuest += 1
        if mesInicio == 1:
            valorCorrigido = valorFimUltimo
        elif mesInicio > 1:
            valorCorrigido = valorFimUltimo - (12 * valorParcela) + (valorParcela * (mesInicio - 1))
        print('..::..' * 8)
        print(f'PERÍODO TOTAL DE PARCELAMENTO: \033[34m{anosParcela} anos / {totalMeses} meses\033[m')
    print(f'VALOR FINAL CORRIGIDO: \033[34mR$ {valorCorrigido:.2f}\033[m')
    print(f'DIFERENÇA ENTRE VALOR INICIAL E VALOR FINAL: \033[34mR$ {valorCorrigido - valorImovel:.2f}\033[m / {(valorCorrigido * 100 / valorImovel) - 100:.2f}% a mais do valor inicial')
