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

