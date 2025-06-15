lista=[]
for i in range(5):
    lista.append(int(input(f"Número {i+1}: ")))

# Jeito 01
# print(f"O maior valor da lista é: {max(lista)} e sua posição na lista é: {lista.index(max(lista))+1}")
# print(f"O menor valor da lista é: {min(lista)} e sua posição na lista é: {lista.index(min(lista))+1}")

#Jeito 02
maior=lista[0]
pos_maior=1
menor=lista[0]
pos_menor=1
for i in range(1,5):
    if lista[i] > maior:
        maior=lista[i]
        pos_maior=i+1
    if lista[i] < menor:
        menor=lista[i]
        pos_menor=i+1
print(f"O maior valor da lista é: {maior} e sua posição na lista é: {pos_maior}")
print(f"O menor valor da lista é: {menor} e sua posição na lista é: {pos_menor}")
