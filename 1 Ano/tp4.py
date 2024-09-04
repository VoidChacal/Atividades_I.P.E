NMaximo = int(input("Digite o número máximo para a sequência de Fibonacci: "))

a, b = 0, 1
soma = 0

while a <= NMaximo:
    soma += a

    a, b = b, a + b

print(f"A soma dos números de Fibonacci até {NMaximo} é: {soma}")
