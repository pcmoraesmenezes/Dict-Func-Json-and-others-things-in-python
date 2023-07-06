"""
Considerando duas listas de inteiros ou floats (listaA ou listaB)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a lista so vai considerar o valor da menor, ex:
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10,11,12]
listaNova = [7,9,11,13,15]
"""
def menor(lista1,lista2):
    if len(lista1) < len(lista2):
        return lista1
    else:
        return lista2

def somaLista(lista1,lista2):
    i = 0
    listaNova = []
    while i < len(menor(lista1,lista2)):
        if not isinstance(lista1[i],(int,float)) and isinstance(lista2[i],(int,float)):
             raise TypeError("Você informou um valor diferente de int ou float")
        else:
            elemento = lista1[i] + lista2[i]
            listaNova.append(elemento)
        i = i+1
    return listaNova

lista1 = [1.1,2,3,4,5]
lista2 = [1,2,3,4,]
print(somaLista(lista1,lista2))