#Exercicio - Unir listas
#Crie uma função zipper
#O trabalho dessa função será unir duas listas
#Listas na ordem
#Use todos os valores da menor lista
#EX:
#['Salvador', 'Ubatuba', 'Belo Horizonte']
#['BA', 'SP', 'MG' , 'RJ' ]
#Resultado : [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
def zipper(lista1, lista2):
    listaNova = []
    if menor(lista1, lista2) == lista1:
        listaNova = unir(lista1,lista2)
        return listaNova
    else:
        listaNova = unir(lista2,lista1)
        return listaNova

def unir(lista1,lista2):
    listaNova = []
    i = 0
    while i < len(lista1):
         elemento = (lista1[i], lista2[i])
         listaNova.append(elemento)
         i = i+1
    return listaNova
def menor(lista1, lista2):
    if len(lista1) < len(lista2):
        return lista1
    else:
        return lista2

lista1 = [1,3,5,7,9,11,13,15]
lista2 = [2,4,6,8,10,12]

print(zipper(lista1,lista2))

