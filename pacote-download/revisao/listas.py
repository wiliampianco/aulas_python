# listas ficam entre []
# listas podem ser MUTÁVEIS
# lista.append(x) -- inclui o elemento 'x' ao final da lista previamente preenchida
# lista.insert(0, x) -- o elemento 'x' é incluído na posição indicada '0' (e não ao final da lista), empurrando os demais elementos para frente. Sempre recebe DOIS VALORES.
# del lista[x] -- elimina o item da lista na posição indicada 'x'
# lista.pop(x) -- elimina o item da lista na posição indicada 'x' -- se nada for indicado no índice '()', o último elemento é eliminado
# lista.remove('x') -- elimina a primeira ocorrência do item indicado no índice, 'x'
# lista[x] = y -- o elemento 'x' da lista é substituído pelo elemento 'y'
# if item in lista: -- condiciona uma operação à certeza do item na lista. p. ex: if item in lista: / lista.remove[item]
# lista = list(range(1, 11)) -- o comando 'list' cria uma lista com o uso do 'range'
# lista.sort() -- ordena os elementos de uma lista
# lista.sort(reverse=True) -- ordena os elementos de uma lista em ordem inversa
# len(lista) -- mostra quantos elementos existem na lista
# for item in lista: / print(item) -- executa a operação para cada item da lista
# for item in enumerate(lista): / print(item) -- mostra a posição do item na lista e o valor do item (em forma de tupla).
# CONT... 'for posição, item in enumerate(lista):' / print(posição, item) -- retorna a posição do item e o valor do item da lista.
# lista = list() / for c in range(0, 5): / lista.append(int(input('Digite um valor: '))) -- a lista é formada com 'range' via teclado
# listaA = [1, 2, 3, 4] / listaB = listaA -- listaB == [1, 2, 3, 4]
# CONT... listaB[0] = 9 / print(listaA, listaB) / resultado = [9, 2, 3, 4] / [9, 2, 3, 4] -- OU SEJA, as duas listas mudam juntas, pois estão 'LIGADAS'!
# CONT... listaB = listaA[:] -- todos os elementos de listaA são COPIADOS para listaB
# CONT... listaB[0] = 9 / print(listA, listaB) / resultado = [1, 2, 3, 4] / [9, 2, 3, 4]

expre = input('Digite a expressão: ')
abre = 0
fecha = 0
while True:
    if expre[0] == ')':
        print('ERRADO')
        break
    else:
        for simb in expre:
            if simb == '(':
                abre += 1
            elif simb == ')':
                fecha += 1
        if abre == fecha:
            print('CORRETO')
        else:
            print('INCORRETO')
        break
