num1=int(input("Número 01: "))
num2=int(input("Número 02: "))
num3=int(input("Número 03: "))
num4=int(input("Número 04: "))
noves=0
estado=True
posicao=0
pares=0
tupla=(num1,num2,num3,num4)
print(f"Você digitou os valores: {tupla}")
for i in range(len(tupla)):
    if tupla[i]==9:
        noves+=1
    if tupla[i]==3 and estado:
        posicao=i+1
        estado=False
print(f"O valor 9 apareceu {noves} vezes")
if posicao==0:
    print("O valor 3 não apareceu nenhuma vez")
else:
    print(f"O valor 3 apareceu na {posicao}° posição")

print("Os numeros pares foram: ",end="")
for i in range(len(tupla)):
    if tupla[i]%2==0:
        print(f"{tupla[i]} ", end="")
        pares+=1

if pares ==0:    
    print("Não foram escritos números pares")