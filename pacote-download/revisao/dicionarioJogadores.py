atletas = []
jogador = {}
while True:
    jogador['nome'] = input('Nome do jogador: ').strip().upper()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = []
    total = []
    for g in range(0, partidas):
        gols.append(int(input(f'Quantos gols, {jogador["nome"]} fez na {g + 1}° partida? ')))
    jogador['gols'] = gols
    total.append(sum(gols))
    jogador['total'] = total
    atletas.append(jogador.copy())
    resp = input('Quer continuar? [S/N] ').upper()[0]
    while resp not in 'SN':
        print('Resposta inválida!')
        resp = input('Quer continuar? [S/N] ').upper()[0]
    if resp == 'N':
        break
print('-=-' * 15)
print('cod.', end='')
for i in jogador.keys():
    print(f'{str(i):<15}', end=' ')
print()
print('---' * 15)
for p, i in enumerate(atletas):
    print(f'{p:3}', end=' ')
    print(f'{str(i["nome"]):<15} {str(i["gols"]):<15} {str(i["total"]):<3}')
print('---' * 15)
while True:
    mostrar = int(input('Verificar CÓDIGO de qual jogador? (999 para parar): '))
    if mostrar == 999:
        break
    while mostrar < 0 or mostrar >= len(atletas):
        print('CÓDIGO inválido!')
        mostrar = int(input('Verificar CÓDIGO de qual jogador? (999 para parar): '))
    print(f'   -- LEVANTAMENTO DO JOGADOR {atletas[mostrar]["nome"]}')
    for levantamento in range(0, len(atletas[mostrar]["gols"])):
        print(f'    No jogo {levantamento + 1} fez {atletas[mostrar]["gols"][levantamento]} gol')
    print('---' * 15)
print('FIM DA ANÁLISE')
