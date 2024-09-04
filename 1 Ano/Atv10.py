turno = str(input("Digite qual turno voce estuda: ")).strip().lower()

if (turno == "M" or turno == "matutino" or turno == "m"):
    print("Bom dia!")

elif (turno == "V" or turno == "vespertino" or turno == "v"):
    print("Boa tarde!")

elif (turno == "N" or turno == "noturno" or turno == "n"):
    print("Boa noite!")

else:
    print("Valor invalido!")