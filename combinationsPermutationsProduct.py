from itertools import combinations, product, permutations
lista = ['abacate', 'uva', 'morango', 'maça', 'pera']
print(*list(combinations(lista,2)),sep='\n')
print()
print(*list(permutations(lista,2)),sep='\n')
produtos = [
    ['preto', 'branco' ,'azul'],
    ['p','m','g'],
    ['masculino', 'feminino']
]
print()
print(*list(product(*produtos)),sep='\n') 