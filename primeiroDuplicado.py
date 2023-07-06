"""
Exercicio:
Crie uma função que encontra o primeiro duplicado considerando o segundo numero como duplicado. Retorne a duplicação encontrada
Requisitos:
    A ordem do numero duplicado é considerada a partir da segunda
    Ocorrencia do numero duplicado, ou seja, o numero duplicado em si
    Exemplo:
        [1,2,3,3,2,1] -> 1,2,3 São duplicados, retorne 3 
        [1,2,3,4,5,6] -> Retorne -1 (não tem duplicados)
    Se não encotnrar duplicados na lista retorne -1
"""
lista_de_lista_de_inteiros = [
    [1,2,3,4,5,6,7,8,9,10],
    [9,1,8,9,9,7,2,1,6,8],
]

def encontraPrimeiroDuplicado(listaDeInteiros):
    numerosChecados = set()
    primeiroDuplicado = -1

    for numero in listaDeInteiros:
        if numero in numerosChecados:
            primeiroDuplicado = numero
            break
        numerosChecados.add(numero)

    print()
    print()

    return primeiroDuplicado

for lista in lista_de_lista_de_inteiros:
    print(
        lista,
        encontraPrimeiroDuplicado(lista)
    )     

