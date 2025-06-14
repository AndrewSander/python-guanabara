import random
num1=random.randint(0,100)
num2=random.randint(0,100)
num3=random.randint(0,100)
num4=random.randint(0,100)
num5=random.randint(0,100)
tupla=(num1,num2,num3,num4,num5)
print(tupla)

#JEITO 1
# print(f"O menor número é: {min(tupla)}")
# print(f"O maior número é: {max(tupla)}")

#JEITO2
maior=tupla[0]
menor=tupla[0]
for i in range(1,len(tupla)):
    if tupla[i] > maior:
        maior= tupla[i]
    if tupla[i] < menor:
        menor= tupla[i]
print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")

