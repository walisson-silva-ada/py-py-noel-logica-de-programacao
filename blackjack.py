import random

def principal():
    jogadores = {}
    baralho = []
    numero_jogadores = int(input("Digite o número de jogadores: "))
    for elemento in range(numero_jogadores):
        jogador = input(f"Digite o nome do {elemento + 1}º jogador: ")
        jogadores[jogador] = 0
    criar_baralho(baralho)
    jogada(jogadores, baralho)
    verificacao(jogadores)
    

def criar_baralho(baralho):
    naipes = ['Paus', 'Copas', 'Espadas', 'Ouros']
    cartas = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Dama', 'Valete', 'Rei']
    for naipe in naipes:
        for carta in cartas:
            baralho.append(carta + ' de ' + naipe)

def sortear_carta(baralho):
    cartas = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Dama', 'Valete', 'Rei']
    carta_sorteada = random.choice(baralho)
    pontos = 0
    for elemento in cartas[0:10]:
        if elemento in carta_sorteada:
            pontos += (cartas.index(elemento) + 1)
    for elemento in cartas[10:13]:
        if elemento in carta_sorteada:
            pontos += 10
    return carta_sorteada, pontos

def jogada(jogadores, baralho):
    jogadores_ativos = [jogador for jogador in jogadores]
    while len(jogadores_ativos) > 0:
        for jogador in jogadores_ativos:
            if ativo(jogador, jogadores) == True:
                carta_sorteada, pontos = sortear_carta(baralho)
                print(carta_sorteada)
                jogadores[jogador] += pontos
            else:
                jogadores_ativos.remove(jogador)
        print(jogadores)
        
def ativo(jogador, jogadores):
    if jogadores[jogador] < 21:
        jogar = input(f"{jogador}, você quer comprar uma carta? (s/n) ").lower()
        if jogar == 's':
            return True

def verificacao(jogadores):
    placar = []
    for jogador, pontos in jogadores.items():
        if pontos <= 21:
            placar.append(pontos)
    if len(placar) == 0:
        return print("Não houve ganhador")
    maior_pontuacao = max(placar)
    for jogador, pontos in jogadores.items():
        if pontos == maior_pontuacao:
            print(f"O ganhador é {jogador} com {pontos} pontos")
    return maior_pontuacao

principal()
