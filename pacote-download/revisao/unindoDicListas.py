todos = list()
pessoa = dict()
idade = 0
mulheres = []
while True:
    pessoa['nome'] = input('Nome da pessoa: ').strip().upper()
    pessoa['sexo'] = input('Sexo [M/F] ').strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F')
        pessoa['sexo'] = input('Sexo [M/F] ').strip().upper()[0]
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    idade += pessoa['idade']
    todos.append(pessoa.copy())
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    while resp not in 'SN':
        print('ERRO! Responda apenas S ou N')
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print('-=-' * 10)
print(f'A) Ao todo, temos {len(todos)} pessoas cadastradas')
print(f'B) A média de idade é de {idade / len(todos)}')
print('C) As mulheres cadastradas foram: ', end='')
for i in mulheres:
    print(i, end='.. ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for i in todos:
    if i["idade"] >= (idade / len(todos)):
        for k, v in i.items():
            print(f'    {k} = {v}', end=';')
        print()
print('==-- ENCERRADO --==')
