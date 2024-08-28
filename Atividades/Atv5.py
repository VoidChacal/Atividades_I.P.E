Nota1 = int(input("Digite a primeira nota: "))
Nota2 = int(input("Digite a segunda nota: "))

Media = (Nota1 + Nota2) / 2

if(Media > 9):
    print("Aprovado")
    print("com Distinção!")
elif(Media == 7):
        print("Aprovado")   
else:
     print("Reprovado!")