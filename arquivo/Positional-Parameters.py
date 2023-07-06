def soma(x,y,/,z,w):
    return (x+y+z+w)
# soma(x=0, y=0, w=0, z=0) -> Dessa forma é erro
print(soma(0,5,w=2, z=3))
x = 3
y = 2
print(soma(x,y, w=2, z = 3))