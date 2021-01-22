# função serve para simplificar processos de rotina em um programa
# função serve para criar comandos personalizados

# em Python, uma função é chamada com "def NomeDaFuncao():"

# EXEMPLO DE FUNÇÃO APLICADA:
'''
def linha():
    print('---' * 10)
linha()                         # ou seja, sempre que precisar utilizar o definidor de função - def linha(): -, basta fazer o chamado - linha()
print('         Olá, mundo!')
linha()

# saída:
# ------------------------------
#          Olá, mundo!
# ------------------------------
'''

# EXEMPLO DE FUNÇÃO COM PARÂMETRO:
'''
def mensagem(msg):          # define que existe um parâmetro para a def - msg
    print('-=-' * 10)       # apenas imprime um linha
    print(msg)              # imprime a mensagem definida para o parâmetro quando a def for chamada
    print('-=-' * 10)
mensagem('PYTHON TESTE')    # chama a def com o parâmetro da função preenchido - 'PYTHON TESTE'

# saída:
-=--=--=--=--=--=--=--=--=--=-
PYTHON TESTE
-=--=--=--=--=--=--=--=--=--=-
'''

# EXEMPLO DE FUNÇÃO COM DOIS PARÂMETROS DEFINIDOS:
'''
def soma(a, b):             # a def solicita a inclusão de dois parâmetros - a, b -- ATENÇÃO: é obrigatório que seja incluído exatamente a quantidade de valores solicitados (nem mais nem menos)
    s = a + b               # faz a soma dos dois parâmetros indicados na chamada da função
    print(s)                # imprime o valor da variável 's'
   
soma(1, 2)                  # ao chamar a def o resultado deve ser a soma dos parâmetros 1 e 2

# saída:
# 3
'''
'''
def soma (a, b):
    print(f'a = {a} e b = {b}')
    s = a + b
    print(f'A soma é: {s}')
soma(b=1, a=2)              # observar que a ordem dos parâmetros foi alterada: a = 2 e b = 1

# saída:
# a = 2 e b = 1
# A soma é: 3
'''

# EXEMPLO DE FUNÇÃO COM QUANTIDADE INDEFINIDA DE PARÂMETROS
'''
def contador(* num):    # indica que será passada uma quantidade indefinida de valores para o parâmetro
    for valor in num:   # nesse caso, o parâmetro - num - será tratado como uma TUPLA
        print(f'{valor}', end=' ')
    print('FIM')

contador(1, 2, 3)
contador(4, 5, 6, 7)
# saída:
# 1 2 3 FIM
# 4 5 6 7 FIM 
'''
# EXEMPLO DE FUNÇÃO COM USO DE LISTA
'''
def dobra(lista):                   # def com um parâmetro
    pos = 0                         # serve como contador
    while pos < len(lista):         # enquanto contador abaixo da qtde de itens da lista
        list[pos] *= 2              # lista na posição de 'pos' dobra o seu valor
        pos += 1                    # o contador tem um acréscimo de 1


valores = [1, 2, 3, 4, 10]          # lista formada fora da def
dobra(valores)                      # 'valores', que é uma lista, aplicada ao parâmetro da def 
print(valores)                      # imprime os números da lista dobrados

# saída:
# [2, 4, 6, 8, 20]
'''

# INTERACTIVE HELP
'''
# comando help() / função interna do Python
# a 'Ajuda Interativa' serve para explicar ao usuário as funcionalidades do Python

# Possibilidade 1:
# na parte inferior da tela, clicar em 'Python Console'
# dentro de 'Python Console', digitar 'help()'
# feito isso, abrirá o modo 'Interactive Help'
# dentro do modo de 'Ajuda Interativa', o usuário deve digitar aquilo que ele procura como dúvida a ser esclarecida
# exemplos: 'print', 'def', 'random', 'len', 'input', etc.
# o resultado da busca será o manual explicativo padronizado do próprio Python ao usuário
# para sair do modo de 'Ajuda Interativa', basta digitar 'quit'.

# Possibilidade 2:
# utilizar o comando help() na área de trabalho do Python
# exemplo: help(print) / resultado: manual explicativo do Python para o comando 'print'

# Possibilidade 3:
# utilizar o 'doc' interno de um comando
# exemplo: print(input.__doc__) / resultado: manual explicativo do Python para o comando 'input'
'''

# DOCSTRING
'''
# docstring é uma string de documentação
# quando criamos uma função, é interessante incluirmos uma docstring para o caso de outro usuário precisar trabalhar com nosso código
# EXEMPLO:
def contador(i, f, p):
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM')
# supondo que o usuário não saiba o que indicam os parâmetros da função (i, f, p), uma alternativa seria chamar o 'help(contador)'
# mas o resultado do help() será aquilo que o criador da função deixou como registro de anotação
# assim, é importanque que essas anotações sejam feitas
# para se fazer o registro das anotações, deve-se utilizar três aspas duplas para abrir e três para fechar, logo abaixo da linha inicial da def.
# VER EXEMPLO ABAIXO:

def teste(a=1, b=2, c=3):
    """
    -> faz uma soma e mostra na tela
    -> a função tem três parâmetros
    -> a inicia com 1
    -> b inicia com 2
    -> c inicia com 3
    """
    s = a + b + c
    print(s)

# ao chmara 'help(teste)' o resultado será o manual explicativo criado entre as três aspas duplas

help(contador)
teste()
help(teste)
'''

# PARÂMETROS OPCIONAIS
'''
# na criação de uma função, os Parâmetros Opcionais servem para que o preenchimento dos parâmetros fique à escolha do usuário

# EXEMPLO 1:
def soma(a, b, c):              # dessa maneira, o usuário é obrigado a preencher os parâmetros com valores definidos
    s = a + b + c
    print(s)

soma(1, 2, 3)                   # se os parâmetros não forem preenchidos pelo usuário (1, 2, 3), haverá um erro

# EXEMPLO 2:
def opcional(a=1, b=2, c=3):    # dessa maneira, caso o usuário não preencha os valores dos parâmetros, eles serão iniciados com a=1, b=2 e c=3
    s = a + b + c
    print(s)

opcional()                      # a def funcionará mesmo que o usuário não preencha o campo com os parâmetros
'''

# ESCOPO DE VARIÁVEIS
# 'escopo' indica o local onde uma variável vai ou não existir

'''
# EXEMPLO de Escopo Global:

def total():
    print(f'Dentro da def, n vale {n}') # 4. dentro da def é informado o valor declarado para a variável n, que está fora da def

n = 2                                   # 1. começa o Programa Principal
print(f'Fora da def, n vale {n}')       # 2. é chamado o print da variável já declarada
total()                                 # 3. é chamada a def criada


# EXEMPLO de Escopo Local:
def local():
    x = 8
    print(f'Dentro da def, n vale {n}')
    print(f'Dentro da def x vale {x}')

n = 2
print(f'Fora da def, n vale {n}')
local()
#print(f'Fora da def, x vale {x}')       # vai dar erro porque 'x' SÓ FUNCIONA DENTRO DA DEF


# EXEMPLO de Escopo Local e Global

def teste(b):
    a = 8                           # 3. outra variável 'a', com escopo Local, pois só funciona dentro da def
    b += 4                          # 4. variável 'b' recebe o seu valor (indicado pela variável 'a' Global) + 4
    c = 2                           # 5. variável 'c', também com escopo Local, recebe o valor 2
    print(f'A dentro vale = {a}')   # 6. print da variável 'a' Local
    print(f'B dentro vale = {b}')   # 7. print da variável 'b' Local
    print(f'C dentro vale = {c}')   # 8. print da variável 'c' Local

a = 5                               # 1. variável 'a' recebe o valor 5
teste(a)                            # 2. a def 'teste' é chamada com o parâmetro da variável 'a', ou seja, valor 5; o escopo de 'a' é Global, pois vai funcionar dentro da def tbém
print(f'A fora vale = {a}')         # 9. print da variável 'a' Global (externa à def)

def teste(b):
    global a                        # 1. 'global' determina que o valor indicado para a variável a partir daqui será sempre o mesmo, ou seja, 'ok'
    a = 'ok'
    b += 4
    c = 2
    print(f'A dentro vale = {a}')
    print(f'B dentro vale = {b}')
    print(f'C dentro vale = {c}')

a = 5
teste(a)
print(f'A fora vale = {a}')         # 2. a variável 'a' dentro da def determina qual será o valor da variável 'a' externa ('ok') em razão do 'global'.
                                    # inclusive, é possível alterar parâmetros int para float ou mesmo str
'''

# RETORNO DE VALORES
'''
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s                    # 1. faz com que a def devolva um resultado; sendo assim, as variáveis externas (r1, r2 e r3) receberão o resultado de 's' como int

r1 = soma(1, 2, 3)
r2 = soma(4, 5)
r3 = soma(6) + 4                # observar a combinação: 'soma()' com parâmetro 6 no 'a' retorna 6 de 's'; essa saída está sendo somada a 4 em 'r3'; print de r3 = 10
print(r1, r2, r3)               # 2. o trabalho de print fica mais facilitado com o uso do 'return' interno à função
'''

# RETURN COMO TRUE ou FALSE
'''
def par(num):
    if num % 2 == 0:            # 3. 'par(num)' vai averiguar se o valor informado é par
        return True             # 4. se o valor for par, retorna 'True'
    else:                       # 5. se o valor não for par
        return False            # 6. retorna 'False'


num = int(input('Número: '))    # 1. solicita um valor int para a variável 'num'
if par(num):                    # 2. condição 'if' para a def 'par(num)'
    print('PAR')                # 7. se 'num' for par, a def é 'True', portanto, print 'PAR'
else:                           # 8. senão, se a def for 'False'
    print('ÍMPAR')              # 9. imprime 'ÍMPAR'
'''
