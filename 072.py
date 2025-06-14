contagem=("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")
numero=int(input("Qual o número? "))
while numero < 0 or numero > 20:
    print("Valor incorreto")
    numero=int(input("Qual o número? "))
print(contagem[numero])