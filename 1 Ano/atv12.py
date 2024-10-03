lista = []
MultLista = []

multi = 0

i = 0

while( i < 8  ):

    Num = int(input("Digite 8 numeros: "))
    multi = Num * Num
    lista.append(Num)
    MultLista.append(multi)
    i = i + 1

print("Numeros adicionados: ", lista)
print("Numeros multiplicados ao quadrado: ", MultLista)
