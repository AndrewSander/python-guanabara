lista=[]
for i in range(5):
    num=int(input("Digite o número 1: "))
    aux=False
    for j in range(len(lista)):
        if num < lista[j]:
            lista.insert(j,num)
            aux=True
            break
    if not aux:
        lista.append(num)
print(lista)