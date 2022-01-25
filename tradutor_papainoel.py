tradutor={'brasil':'Feliz Natal!','alemanha':'Frohliche Weihnachten!',
'austria':'Frohe Weihnacht!','coreia':'Chuk Sung Tan!','espanha':'Feliz Navidad!',
'grecia':'Kala Christougena!','estados-unidos':' Merry Christmas!','inglaterra':'Merry Christmas!',
'australia':'Merry Christmas!','portugal':'Feliz Natal!','suecia':'God Jul!','turquia':'Mutlu Noeller',
'argentina':'Feliz Navidad!','chile':'Feliz Navidad!','mexico':'Feliz Navidad!','antardida':'Merry Christmas!',
'canada':'Merry Christmas!','irlanda':'Nollaig Shona Dhuit!','belgica':'Zalig Kerstfeest!','italia':'Buon Natale!',
'libia':'Buon Natale!','siria':'Milad Mubarak!','marrocos':'Milad Mubarak!','japao':'Merii Kurisumasu!'}
def mensagem(tradutor):
  pais=input('Por onde estamos sobrevoando?\n')
  if pais in tradutor:
    print(tradutor[pais])
  else:
    print('--- NOT FOUND ---')
###

while True:
  continua=int(input('Digite 1 para traduzir e 0 para sair:\n'))
  if continua==1:
    mensagem(tradutor)
  else:
    print('Até mais!')
    break