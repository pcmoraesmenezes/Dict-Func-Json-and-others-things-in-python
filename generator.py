#Funções que sabem pausar em determinada ocasião
#Iterator é uma classe que tem que ter o metodo iter e next e geralemnte iterator lida com o iteravel 
#Todo generator é um iteretaor também
#Mas um iterator não é um generator

import sys

exemplo= [n for n in range(10)]
print(exemplo) 

#Para esse caso não há tanto 'desperdicio de memoria', mas imagine um situação desse tipo

exemplo2 = [n for n in range(1000000)]
#print(exemplo2)

#Note que levou um certo tempo para se obter um resultado, e caso se desejasse acessar um valor especifico a lista ja existiria, mas seria necessario utilizasr de metodos que acarretariam em um 
#Grande desperdicio de memoria, para isso temos o generator:

generator = (n for n in range(10000000))
print(generator) #Mostra o local da memoria do generator

print(sys.getsizeof(generator)) #Retorna o tamanho em bytes
print(sys.getsizeof(exemplo2))

print(next(generator)) #Note que ele começa pelo primeiro valor, o generator está aguardando a requisição de pedidos

#print(generator[0]) -> Não é possivel acessar um local especifico do generator
#print(len(generator)) -> Não é possível determinar o tamanho do generator
# for n in generator:
#     print(n)

def generator(n = 0):
    yield 1
    print('ok')
    print('teste')
    yield 2
    print('vou encerrar')
    return 'Acabou'

gen = generator(n=0)

for n in gen:
    print(n)

def gen1():
    yield 1
    print('teste som')
    yield 2
    print('ei som')
    print('testando')

def gen2():
    yield from gen1()
    print("teste")
    

g = gen2()
for n in g:
    print(n)