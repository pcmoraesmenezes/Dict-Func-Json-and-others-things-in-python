iteravel = ['eu', 'tenho', '__iter__'] 
iterador = iteravel.__iter__()
#O iteravel tem a responsabilidade de deter o valor(es)
#A unica responsabilidade do iterador e entregar um valor por vez, ele apenas sabe o proximo iterador
print(next(iterador))