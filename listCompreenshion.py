import os

import os

def limpar_terminal():
    if os.name == 'posix':  # Verifica se o sistema é baseado em Unix (Linux, macOS, etc.)
        os.system('clear')
    elif os.name == 'nt':  # Verifica se o sistema é Windows
        os.system('cls')

# Utilize a função para limpar o terminal



lista = []
for i in range(10):
    lista.append(i)
print(lista)

#Temos duas opções para lidar com map e filter, podemos fazer manualmente ou utilizando as funções map() e filter()
def multiplicaPorDois(n):
    return n * 2

listaDobrada = list(map(multiplicaPorDois,lista)) 
print(listaDobrada)

lista = []
listaDobrada = []

print(lista,listaDobrada)

lista = [i for i in range(10)]
print(lista)

listaDobrada = list((2*i for i in lista))
print(listaDobrada)

listaDobrada = [2*i for i in lista]
print(listaDobrada)

limpar_terminal()

def eh_Par(n):
    return n % 2 == 0

lista = []
lista_nova = []

lista = [i for i in range(10)]
print(lista)

lista = list(filter(eh_Par,lista))
print(lista)

lista = [i for i in range (10)]

lista_nova = [ i for i in lista if i % 2 == 0 ]
print(lista_nova)

limpar_terminal()
#Temos agora aplicações mais pesadas de list compreenshion, mas note , se utilizarmos coerentemente a biblioteca map e filter, conseguimos evitar um certo trabalho

info = {
    'nome': 'Paulo',
    'sobrenome': 'César'
}
infoExtras = {
    'telefone': '30988874',
    'endereço': 'Rua dos boco'
}

materias = {
    'mat':'calculo'
}

infocompleta = {**info,**infoExtras}
print(infocompleta)

listaComplexa = [
    {
        **info, 'nome': 'Paulo' * 2
    },
    {
       **infoExtras, 'telefone': '30988874' if 'ender' in {**infoExtras}  else {**materias}
    }

]
print(*listaComplexa)

limpar_terminal()

lista = []
for i in range(3):
    for j in range(4,7):
        lista.append((i,j))

print(lista)
    
lista1 = []
lista1 = [(x,y) for x in range(3)
          for y in range(4,7)]
print(lista1)

lista2 = [] 
lista2 = list(map(lambda x: [(x, y) for y in range(4, 7)], range(3)))
