def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    left = quicksort(left)
    right = quicksort(right)
    return quicksort(left) + middle + quicksort(right)
nomes = []
for i in range(3):
    nome = input(f"Digite o {i+1}° nome: ")
    nomes.append(nome)
nomes_ordenados = quicksort(nomes)
print("Lista ordenada: ", nomes_ordenados)