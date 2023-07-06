import json
import os

# Criando um dicionário de informações de uma pessoa
pessoa = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo',
    'profissão': 'Engenheiro'
}

# Acessando valores do dicionário
print("Nome:", pessoa['nome'])
print("Idade:", pessoa['idade'])
print("Cidade:", pessoa['cidade'])
print("Profissão:", pessoa['profissão'])

# Modificando valores do dicionário
pessoa['idade'] = 31
pessoa['profissão'] = 'Desenvolvedor'

# Adicionando um novo par chave-valor
pessoa['telefone'] = '123456789'

# Removendo um par chave-valor
del pessoa['cidade']

# Imprimindo o dicionário atualizado
print(pessoa)


BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json')
with open(SAVE_TO, 'w') as file:
    json.dump(pessoa,file,ensure_ascii=False,indent=2)

with open(SAVE_TO,'r')as file:
    pessoa = json.load(file)
    print(pessoa)