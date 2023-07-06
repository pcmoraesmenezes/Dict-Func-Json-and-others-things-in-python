import os
import sqlite3

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def desfazer(lista1, lista2):
    lista2.append(lista1.pop())

def refazer(lista1, lista2):
    lista1.append(lista2.pop())

# Conexão com o banco de dados
con = sqlite3.connect('tarefas.db')
cur = con.cursor()

# Criação da tabela caso não exista
cur.execute("CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY AUTOINCREMENT, tarefa TEXT)")

# Função para salvar a tarefa no banco de dados
def salvarTarefa(tarefa):
    cur.execute("INSERT INTO tarefas (tarefa) VALUES (?)", (tarefa,))
    con.commit()

# Função para recuperar todas as tarefas do banco de dados
def recuperarTarefas():
    cur.execute("SELECT tarefa FROM tarefas")
    rows = cur.fetchall()
    return [row[0] for row in rows]

tarefas = recuperarTarefas()
lista = []
usuario = None

while True:
    print('Comandos: listar, desfazer, refazer')
    print("Digite uma tarefa ou um comando:")
    usuario = str(input())

    if usuario == 'listar':
        if len(tarefas) == 0:
            print('Lista vazia')
        else:
            limparTela()
            print('\n'.join(tarefas))
    elif usuario == 'desfazer':
        if len(tarefas) == 0:
            print("Nada a desfazer!")
        else:
            print('Desfeito')
            desfazer(tarefas, lista)
    elif usuario == 'refazer':
        if len(tarefas) == 0 or len(lista) == 0:
            print("Nada a ser refeito!")
        else:
            refazer(tarefas, lista)
            print('Refeito')
    elif usuario == 'limpar':
        limparTela()
    elif usuario == 'sair':
        break
    else:
        tarefas.append(usuario)
        salvarTarefa(usuario)

con.close()
