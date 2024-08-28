Produto1 = float(input("Digite o preço do primeiro Produto: "))
Produto2 = float(input("Digite o preço do segundo Produto: "))
Produto3 = float(input("Digite o preço do terceiro Produto: "))

menor_preco = min(Produto1, Produto2, Produto3)

if(menor_preco == Produto1):
    print("Compre o primeiro produto")

elif(menor_preco == Produto2):
    print("Compre o segundo produto")

elif(menor_preco == Produto3):
    print("Compre o terceiro produto")