n=int(input('Termo que deseja encontrar:'))
ultimo=1
penultimo=1
# comentario

if(n==1) or (n==2):
    print("1")
else:
    count=3
while count <= n:
    termo=ultimo + penultimo
    penultimo=ultimo
    ultimo=termo
    count+=1
    print(termo)
