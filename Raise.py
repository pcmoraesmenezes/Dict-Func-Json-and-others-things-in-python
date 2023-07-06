#
# raise ValueError("Deu erro")
# print(456)

def divide(m,n):
    if not isinstance(m, (float, int)):
        raise TypeError("Informou Valores impossiveis")
    if not isinstance(n, (float, int)):
        raise TypeError("Informou valores impossiveis")
    if n == 0:
        raise ZeroDivisionError("Não é possivel dividir por zero ")
    return m/n


print(divide(1,2))
print(divide('a','b'))
print(8/0)