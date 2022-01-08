
notas = {'W':1, 'H':1/2, 'Q':1/4, 'E':1/8, 'S':1/16, 'T':1/32, 'X':1/64}

incorretos = []
corretos = 0

musica = input('Insira sua composição [Utilize "/" para separar os compassos]:')
musica = musica.upper()
musica = musica.split('/')

for compasso in musica:
    soma = 0
    for nota in compasso:
        soma += notas[nota]
    if soma != 1:
        incorretos.append(compasso)
    else:
        corretos += 1

print(f'''Número de compassos corretos:', {corretos}
Compassos incorretos: [{', '.join(incorretos)}]''')
