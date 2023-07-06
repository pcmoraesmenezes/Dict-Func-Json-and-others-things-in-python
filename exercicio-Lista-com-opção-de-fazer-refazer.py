#Lista de tarefa com a opção de desfazer e refazer
import os
import json
def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def desfazer(lista1, lista2):
    lista2.append(lista1.pop())

def refazer(lista1, lista2):
    lista1.append(lista2.pop())

def ler(tarefas,caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        salvar(tarefas, caminho_arquivo)
        print('teste')
    return dados

def salvar(tarefas,caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf-8' ) as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
        return dados

CAMINHO_ARQUIVO = 'tarefasExericicio.json'
tarefas = ler([], CAMINHO_ARQUIVO)
lista = []
usuario = None
while True:
    print('Comandos: listar, desfazer, refazer, limpar(Limpa a tela), sair(sai do programa)')
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
            print('desfeito')
            desfazer(tarefas,lista)

    elif usuario == 'refazer':
        if len(lista) != 0 :
            refazer(tarefas, lista)
        elif len(tarefas) == 0:
            print('Lista vazia')
        elif len(lista) == 0:
            print("Nada a ser refeito! ")

    elif usuario == 'limpar':
        limparTela()

    elif usuario == 'sair':
        break

    else:
        tarefas.append(usuario)

salvar(tarefas,CAMINHO_ARQUIVO)