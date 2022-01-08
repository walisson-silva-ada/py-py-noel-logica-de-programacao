def novo_cadastro(desejos):
  nome=input('Digite seu nome:\n')
  desejos[nome]=[]
  for _ in range(3):
    p1=input('Digite um presente:\n')
    desejos[nome].append(p1)
  return desejos
def checagem(desejos):
  amigo=input('Quem você tirou?\n')
  presente=input('E que presente você pensou em dar pra essa pessoa?\n')
  if amigo in desejos:
    if presente in desejos[amigo]:
      print('Acertou em cheio!\n')
    else:
      print('Escolha outro presente!\n')
  else:
    print('Ops! Seu amigo não cadastrou preferências!\n')


desejos=dict()
while True:
  escolha=int(input('Bem vindo ao sistema de escolha de presentes de Natal!\nDigite 1 para cadastrar sua preferência, 2 para consultar ou 0 para sair.\n'))
  if escolha==0:
    print('Até mais!\n')
    break
  elif escolha==1:
      novo_cadastro(desejos)
  elif escolha==2:
    checagem(desejos)
  else:
    print('Opção inválida!\n')
