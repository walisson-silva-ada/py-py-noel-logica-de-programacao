def super_digito(str_numero):
    lista = []
    contador = 0
    lista.append(str_numero)
    
    sup = list(map(int, str_numero))
    
    soma = sum(sup)
    
#     print(soma)
    
    while soma > 9:
        novo_num = str(soma)
        lista.append(novo_num)
        soma = super_digito(novo_num)
        
#     print(lista)
    return(soma)

print('\::: Bem vindo ao cálculo de super dígito :::\n')
n = int(input('Digite um número:'))
k = int(input('Digite um número:'))
str_numero = str(k*n)

resultado = super_digito(str_numero)
print('O super dígito do produto dos números digitados é', resultado)