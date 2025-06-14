palavras="cabeça","moeda","mesa"
for i in range(len(palavras)):
    print(f"Na palavra {palavras[i]} temos ",end="")
    for j in palavras[i]:
        if j=="a" or j=="e" or j=="i" or j=="o" or j=="u":
            print(f"{j} ",end="")
    print()