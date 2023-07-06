#Exercicios:
#Aumente o preço dos produtos a seguir em 10%
#Gere novos produtos por deep copy(copia profunda)
import copy
produtos = [

    {'nome':  'Produto 5', 'valor': 10.00} ,
    { 'nome': 'Produto 3', 'valor': 22.32},
    { 'nome': 'Produto 2', 'valor': 10.11},
    { 'nome': 'Produto 1', 'valor': 105.87},
    { 'nome': 'Produto 4', 'valor': 69.9},
]

produtosValorDiferente = copy.deepcopy(produtos) #Copia profunda
i = 0
while i < len(produtosValorDiferente):
    produtosValorDiferente[i]['valor'] = round(produtosValorDiferente[i]['valor'] * 1.1,2)
    i = i+1
print(produtosValorDiferente) #Retona os valores com 10% de aumento


#Ordene os produtos por nome_decrescente(do maior para o menor)
#Gere produtos_ordenados por deep copy

produtoOrdenadoNome = copy.deepcopy(produtos)
print(produtoOrdenadoNome)
i = 0

while i < len(produtoOrdenadoNome):
    j = 0
    while j < len(produtoOrdenadoNome) - 1:
        if produtoOrdenadoNome[j]['nome'] > produtoOrdenadoNome[j+1]['nome']:
            aux = produtoOrdenadoNome[j]
            produtoOrdenadoNome[j] = produtoOrdenadoNome[j+1]
            produtoOrdenadoNome[j+1] = aux
        j = j + 1
    i = i + 1


print(produtoOrdenadoNome)


#Ordene os produtos por valor crescente (do menor para o maior)
#Gere produtos ordenados por deep copy

produtoOrdenadoValor = copy.deepcopy(produtos)
print(produtoOrdenadoValor)
produtoOrdenadoValor = sorted(produtoOrdenadoValor, key=lambda x: x['valor'])
print(produtoOrdenadoValor)

