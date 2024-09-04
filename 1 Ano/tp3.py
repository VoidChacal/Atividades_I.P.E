numero = int(input("Digite um número inteiro e positivo: "))

while numero <= 0:
    print("Número inválido. Por favor, insira um número positivo.")
    numero = int(input("Digite um número inteiro e positivo: "))

print(f"Números primos menores ou iguais a {numero}:")
for i in range(2, numero + 1):

    primo = True
    for j in range(2, i):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i)
