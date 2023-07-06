#Exercicio de perguntas e respostas:
perguntas = [
    {
        'pergunta': 'Quanto é 2+2?',
        'opções': ['1','3','4','5'],
        'resposta': '4',
    },
    {
        'pergunta': 'Quanto é 5*5?',
        'opções':['25','10','51','21'],
        'resposta': '25',
    },
    {
        'pergunta':'Quanto é 10/5?',
        'opções':['4','5','1','10'],
        'resposta': '5',
    },
    {
        'pergunta': 'Quanto é 9*7',
        'opções': ['81','78','64','63'],
        'resposta': '63',
    }
]
i = 0
x = 0
cont = 0
resp = 0
while i < len(perguntas) :
    print('Pergunta:', end=' ')
    print(perguntas[i]['pergunta'])
    print('Opções:')
    while x < len(perguntas[i]['opções']):
        print(x,end=") ")
        print(perguntas[i]['opções'][x])
        x = x+1
    resp = int(input())
    if perguntas[i]['resposta'] == perguntas[i]['opções'][resp]:
        print('Acertou!!!')
        cont = cont+1
    else:
        print('Você errou :(')
    x = 0
    i = i+1
print(f'Você acertou',cont,'de',i, 'questões!')