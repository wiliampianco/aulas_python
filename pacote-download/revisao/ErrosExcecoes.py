# existem erros de Sintaxe e erros de Semântica
# erros de Sintaxe indicam que a escrita de um comando, por exemplo, foi mal feita
# erros de Semântica indicam que a lógica de um programa não está bem feita
# EXEMPLOS:
#   primt(x) == erro de Sintaxe, pois o correto seria 'print(x)'
#   print(x) == erro de Semântica, caso a variável 'x' não tenha sido declarada previamente

# problemas Sintáticos são ERROS
# problemas Semânticos são EXCEÇÕES

# para evitar mensagens de erro, o Python conta com a estrutura 'try: ... except: ... else: ... finally: '
# EXEMPLO:
'''
try:                                                # o 'try' pede para que o programa tente executar um comando
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:                                             # o 'except' apresenta qual deve ser o comportamento do programa caso a tentativa inicial falhe
    print('Infelizmente tivemos um problema!')
else:                                               # se o programa não cair no 'except', o programa executa o 'else', ou seja, o resultado esperado
    print(f'O resultado do cálculo é: {r:.1f}')
finally:                                            # funcionando bem ou não, o 'finally' será acionado na saída da estrutura
    print('FIM')
'''
# EXEMPLO:
'''
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:                                   # a classe principal 'Exception' é passada para a variável 'erro'
    print(f'O problema encontrado foi {erro.__class__}')    # '__class__' demonstra qual foi a classe do erro encontrado
else:                                                       # [não é indicado demonstrar a classe do erro para o usuário final]
    print(f'O resultado do cálculo é: {r:.1f}')
finally:
    print('FIM')
'''
# EXEMPLO COM VÁRIOS TIPOS DE EXCEÇÕES:
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dado digitado')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero')
else:
    print(f'O resultado do cálculo é: {r:.1f}')
finally:
    print('FIM')
