def soma(x,y):
    return x+y

def multplica(x,y):
    return x*y

def executa(funcao, x):
     def interna(y):
        return funcao(x,y)
     return interna

soma_com_cinco = executa(soma,5)
print(soma_com_cinco(10))


multplica_por_dez = executa(multplica,10)
print(multplica_por_dez(5))