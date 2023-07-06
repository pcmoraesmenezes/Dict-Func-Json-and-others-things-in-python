

caminho_arquivo = 'C:\\Users\\pczin\\OneDrive\\Área de Trabalho\\vscode\\python\\udemy\\Anotações - Exemplos práticos\\arquivo\\teste.txt'

# arquivo = open(caminho_arquivo,'w')

# arquivo.close()
with open(caminho_arquivo,'w+', encoding='utf-8') as arquivo: #Utilizando 'w+' vocÃª habilita a possibilidade de escrita e leitura
    arquivo.write("Atenção 1\n")
    arquivo.write("Linha 2")
    arquivo.seek(0, 0)
    print(arquivo.read()) #NÃ£o funcionarÃ¡, Ã© necessÃ¡rio 'reinicializar' a posiÃ§Ã£o do arquivo para a 0 0, fazemos isso utilizando a funÃ§Ã£o seek
print()
with open(caminho_arquivo,'r') as arquivo:
    print(arquivo.read())