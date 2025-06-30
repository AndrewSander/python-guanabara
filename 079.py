lista=[]
while True:
    num=int(input("Qual número você quer adicionar? "))
    if num in lista:
        print("Valor duplicado, não vou adicionar")
    if num not in lista:
        lista.append(num)
        print("Valor adicionado com sucesso...")
    continuar=input("Você deseja continuar? [S/N] ")
    if continuar == "N":
        break
lista.sort()
print(lista)