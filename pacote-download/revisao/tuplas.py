# tuplas são IMUTÁVEIS
# tuplas ficam entre () - embora o Python aceite sem () tbém
# for c in tupla: - no lugar de for c in range(x, x):
# sorted() - serve para mostrar os itens das tuplas de forma ordenada
# tupla.count(x) - conta quantas vezes o elemento x aparece na tupla
# é possível somar duas tuplas - a = (1, 2, 3) / b = (4, 5, 6) -- c = a + b
# print(nome da tupla.index(valor) - mostra qual a posição da primeira ocorrência do valor solicitado
# print(nome da tupla.index(valor, x) - mostra qual a posição da primeira ocorrência do valor solicitado a partir de uma posição definida
# em Python, tuplas aceitam dados de diferentes tipos - p.ex: pessoa = ('Wiliam', 36, 'M', 76.5)
# del(nome da tupla) - apaga a tupla inteira -- o del serve para qualquer outro elemento dentro de Python
# max(tupla) = mostra o maior valor dentro da tupla
# min(tupla) = mostra o menor valor dentro da tupla
palavras = ('agua', 'mel', 'acucar', 'cafe', 'doce', 'sal', 'cerveja', 'amendoim', 'pimenta')
t1 = t2 = t3 = ' '
cont = 0
for item in palavras:
    print(f'\nA palavra {item.upper()} tem ', end=' ')
    if item in palavras[0]:
        for p in item:
            if p in 'aeiou':
                cont += 1
                print(f'{p.lower():}', end=' ')
                if cont == 1:
                    t1 = p
                if cont == 2:
                    t2 = p
                if cont == 3:
                    t3 = p
teste = (t1, t2, t3)
for v in teste:
    print(v)

