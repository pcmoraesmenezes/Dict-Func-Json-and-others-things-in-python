string = 'paulo'
print(dir(string))
metodo = 'upper'
#hasattr -> Checa se um atributo tem determinado nome la dentro

if hasattr(string,'upper'):
    print('Existe')
    print(string.upper())

#É possivel utilizar dessa forma:

if hasattr(string, metodo):
    print('Existe')
    #print(string.metodo()) -> Note que não é possivel utilizar dessa maneira, para isso existe o getattr

print(getattr(string,metodo)()) 
print(getattr(string,metodo)) # -> Mostra a posição da memoria do metodo do objeto