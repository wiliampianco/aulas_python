# LISTAS COMPOSTAS
# pessoas = list() / dados = ['Pedro', 25] / pessoas.append(dados[:]) / print (pessoas) / resultado = [['Pedro', 25]]
# CONT... ATENÇÃO: a lista 'pessoas', depois de receber os dados da lista 'dados' tem apenas um elemento, que são todas as infos de 'dados'.
# Ou seja, ['Pedro', 25] está em pessoas[0].
# EXEMPLO:
'''
pessoa1 = ['Pedro', 25]
pessoa2 = ['Ricardo', 37]
pessoa3 = ['Wiliam', 36]
pessoas = list()
pessoas.append(pessoa1[:])
pessoas.append(pessoa2[:])
pessoas.append(pessoa3[:])
print(pessoas)
Saída == [['Pedro', 25], ['Ricardo', 37], ['Wiliam', 36]]
print(pessoas[0][0]) # solicita a posição '0' da sub-lista (pessoa1) que ocupa a posição '0' da lista (pessoas)
Saída == Pedro'''
# EXEMPLO
'''galera = [['Wiliam', 36], ['Willy', 33], ['Sergio', 57], ['Graça', 56]]
for p in galera:
    print(p[0])
Saída == Wiliam / Willy, Sergio, Graça -- Ou seja, apenas os 'nomes' cadastrados no exemplo.'''
# EXEMPLO
'''
galera = list()
dado = list() # neste exemplo, tem a função de ser uma lista 'temporária'
for c in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # ATENÇÃO, se não for utilizada a estrutura '[:]', as listas estarão ligadas, e não copiadas. Neste exemplo, se apenas copiadas, as duas seriam apagadas depois do 'clear'
    dado.clear() # o 'clear' deve limpar os itens de 'dados'
print(galera)
Saída == todos os itens digitados para 'dado' 
'''

from random import randint
from time import sleep

principal = []
temporaria = []
apostas = int(input('Quantas apostas deseja fazer: '))
for a in range(0, apostas):
    for t in range(0, 6):
        numero = randint(0, 60)
        while numero in temporaria:
            numero = randint(0, 5)
        temporaria.append(numero)
    principal.append(temporaria[:])
    temporaria.clear()
for p in range(0, apostas): 
    print(f'Aposta n° {p+1:2}: {sorted(principal[p])}')
    sleep(2)
