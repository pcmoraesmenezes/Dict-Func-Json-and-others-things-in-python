
try:
    a = 18
    b = 0
    print('linha 1')
    c = a/b
    print('linha 2')
except ZeroDivisionError as erro:
    print('Não dividiu por 0x')
    print('msg: ', erro)
except NameError:
    print("Não definiu o valor de a")

#Note que os erros funcionam como if e else

try:
    a = 18
    b = 0
    print('linha 1')
    c = a/b
    print('linha 2')
except Exception:
    print('erro desconhecido')

#Exception é a top tier dos erros, tem prioridade de execução
#É possível passar uma tupla para as exceções para ter o tratamento de duas exceções
#Utilizando 'as' é possível pegar a instancia do erro e exibir na tela

try:
    print(1)
    # 8/0
except ZeroDivisionError:
    print('Dividiu por 0 ')
else:
    print('Nem sempre é executado')
finally:
    print('Sempre será executado')
