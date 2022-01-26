def super_digito(str_numero):
    lista = []
    lista.append(str_numero)
    sup = list(map(int, str_numero))
    soma = sum(sup)
    
    while soma > 9:
        novo_num = str(soma)
        lista.append(novo_num)
        soma = super_digito(novo_num)
    return(soma)

print('\::: Bem vindo ao cálculo de super dígito :::\n')
n = int(input('Digite um número:'))
k = int(input('Digite um número:'))
str_numero = str(k*n)

print('O super dígito do produto dos números digitados é', super_digito(str_numero))