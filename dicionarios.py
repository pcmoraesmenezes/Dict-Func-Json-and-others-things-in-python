import copy
pessoa = {
    'nome': 'Paulo',
    'sobrenome': 'César Moraes de Menezes',
    'idade': 19,
    'altura': 1.76,
    'endereços':[
        
        {    'rua1': 'dos bobos', 'numero': 0},
        {    'rua2': 'x', 'numero': 5,},
        
    ],
}
print(pessoa,type(pessoa))
print(pessoa['idade'])
for chave in pessoa:
    print(chave,pessoa[chave])

print(pessoa['endereços'])

teste = {}
teste['asda'] = 'jailson'

print(teste)

del pessoa['nome']
print(pessoa)

print(pessoa.get('idade'))

if pessoa.get('nome'):
    print('existe')

print(pessoa.__len__())
print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.setdefault('comida', 'macarrao'))
d2= pessoa.copy()
d2 = copy.deepcopy(pessoa)
print(pessoa.get('idade'))
print(pessoa.get('nome', 'nao existe'))
teste = pessoa.pop('sobrenome')
print(teste)
print(pessoa)
print(pessoa.popitem())
pessoa.update({
    'nome': 'paulo',
    'comida': 'macarrao',
})
print(pessoa)