lista = [
    'a', 1,1,1, 1.1, True, [0,1,2],(1,2),
    {0,1}, {'nome':'Paulo'},
]
for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item,set))

    elif isinstance(item, str):
        print(item.upper())
        print(item,isinstance(item.upper(),set))

    elif isinstance(item,(int,float)):
        print('NUM:')
        print(item, item * 2)

    else:
        print('OUTRO')