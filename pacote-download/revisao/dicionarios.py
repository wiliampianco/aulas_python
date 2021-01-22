# DICIONÁRIOS
# dicionários são identificados com chaves { }
# EXEMPLO: podemos declarar dicionários como: 'dados={}' ou 'dados = dict()'
# EXEMPLO: dados = {'nome': 'Pedro'} -- 'nome' == key / 'Pedro' = valor
# CONT... print(dados['nome']) / saída = 'Pedro' -- ATENÇÃO: quando informado a key dentro dos colchetes, a key deve estar entre aspas

# PARA ACRESCENTAR NOVOS ITENS:
'''
EXEMPLO:    dados = {'nome':'Wiliam', 'idade':37}
            dados=['sexo'] = 'M'
#   CONT... print(dados['sexo']) -- saída: 'M' -- Ou seja, item 'sexo': 'M' foi acrescentado ao dicionário
#   CONT... print(dados) -- saída: {'nome': 'Wiliam', 'idade': 37, 'sexo': 'M'}
'''

# PARA SUBSTITUIR VALORES:
'''
EXEMPLO: dados['nome'] = 'João'
    print(dados['nome']) / saída: 'João'
'''

# PARA DELETAR ELEMENTOS
'''EXEMPLO: del dados['idade'] 
    print(dados) -- saída: {'nome': 'João', 'sexo': 'M'}
'''

# VALORES, KEYS E ITENS:
'''
filmes = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
print(filmes.values()) -- saída: dict_values(['Star Wars', 1977, 'George Lucas'])
print(filmes.keys()) -- saída: dict_keys(['titulo', 'ano', 'diretor'])
print(filmes.items()) -- saída: dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])
'''

# ESTRUTURA DE REPETIÇÃO:
'''
for k, v in filmes.items():
    print(f'O {k} é {v}')
    saída:
        O titulo é Star Wars
        O ano é 1977
        O diretor é George Lucas
'''

# DICIONÁRIOS DENTRO DE LISTAS
# É possível mesclar tuplas, listas e dicionários
'''
locadora = [{'título': 'TÍTULO 0', 'ano': 'ANO 0', 'diretor': 'DIRETOR 0'},
            {'título': 'TÍTULO 1', 'ano': 'ANO 1', 'diretor': 'DIRETOR 1'},
            {'título': 'TÍTULO 2', 'ano': 'ANO 2', 'diretor': 'DIRETOR 2'}]
print(locadora)                 -- saída:   [{'título': 'TÍTULO 0', 'ano': 'ANO 0', 'diretor': 'DIRETOR 0'},
                                            {'título': 'TÍTULO 1', 'ano': 'ANO 1', 'diretor': 'DIRETOR 1'},
                                            {'título': 'TÍTULO 2', 'ano': 'ANO 2', 'diretor': 'DIRETOR 2'}]
print(locadora[0])              -- saída: {'título': 'TÍTULO 0', 'ano': 'ANO 0', 'diretor': 'DIRETOR 0'} 
print(locadora[1]['ano'])       -- saída: ANO 1
print(locadora[2]['diretor'])   -- saída: DIRETOR 2
for p, i in enumerate(locadora):
    print(p, i)                 -- saída: 0 {'título': 'TÍTULO 0', 'ano': 'ANO 0', 'diretor': 'DIRETOR 0'}
                                -- saída: 1 {'título': 'TÍTULO 1', 'ano': 'ANO 1', 'diretor': 'DIRETOR 1'}
                                -- saída: 2 {'título': 'TÍTULO 2', 'ano': 'ANO 2', 'diretor': 'DIRETOR 2'}

    print(i['diretor'])         -- saída: DIRETOR 0
                                -- saída: DIRETOR 1
                                -- saída: DIRETOR 2
'''

# CÓPIA DE CONTEÚDOS EM DICIONÁRIOS:
'''
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do estado: ')
    brasil.append(estado.copy())    # copy() copia todo o conteúdo do dicionário (estado) para a lista (brasil)
print(brasil)   # saída: [{'uf': 'sampa', 'sigla': 'sp'}, {'uf': 'rio', 'sigla': 'rj'}, {'uf': 'acre', 'sigla': 'ac'}] -- todos os valores digitados para estado
for i in brasil:
    print(i)    # saída: {'uf': 'sampa', 'sigla': 'sp'} -- observar que cada item (i) é um dicionário próprio
                # saída: {'uf': 'rio', 'sigla': 'rj'}
                # saída: {'uf': 'acre', 'sigla': 'ac'}
    for k, v in i.items():
        print(v, end=' ')
    print()     # saída: sampa sp
                # saída: rio rj
                # saída: acre ac
'''
# COLOCAR ITENS EM ORDEM NOS DICIONÁRIOS
'''
from operator import itemgetter                     # -- É preciso importar itemgetter para informar qual é a referência a ser ordenada
numeros = {'n1': 4,
           'n2': 3,
           'n3': 2}
                                                    # -- Para a ordenação, deve-se passar os itens do dicionário para uma lista (ordem)
ordem = sorted(numeros.items(), key=itemgetter(1))  # -- Aqui está indicado que a lista (ordem) colocará os itens do dicionário ordenados pelo item na posição 1 (key=itemgetter(1))
print(ordem)
            # saída: [('n3', 2), ('n2', 3), ('n1', 4)] 
                                                    # -- para inverter a ordem, deve-se incluir reverse=True depois de key=itemgetter(1) 
'''
