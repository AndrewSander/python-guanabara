mundial=("flamengo", "cruzeiro", "palmeiras", "santos", "vasco", "internacional", "sport", "bahia", "confiaça", "corinthias", "botafogo", "fluminense", "chapecoense", "barcelona", "real madrid", "psg", "são paulo", "ubers", "atlético de madrid","borussia")

print("Os primeiros colocados são: ")
for i in range(5):
    print(f"{i+1}: {mundial[i]}")

print("Os últimos quatro são: ")
for i in range(len(mundial)-4,len(mundial)):
    print(f"{i+1}: {mundial[i]}")

print("Os times em ordem alfabética são: ")
for i in range(len(mundial)):
    ordenada=sorted(mundial)
    print(f"{i+1}: {ordenada[i]}")

posicao=(mundial.index("chapecoense") + 1)
print(f"O time chapecoense está no a posição: {posicao} ")
