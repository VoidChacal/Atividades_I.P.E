import csv

# Definindo a estrutura de dados
class Pessoa:
    def __init__(self, nome, rg, telefone, endereco):
        self.nome = nome
        self.rg = rg
        self.telefone = telefone
        self.endereco = endereco

def receber_dados():
    pessoas = []
    print("Insira os dados da pessoa. Digite 'FIM' no nome para encerrar.")
    
    while True:
        nome = input("Nome: ")
        if nome.upper() == 'FIM':
            break
        rg = input("RG: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")

        # Armazenando no vetor de pessoas
        pessoa = Pessoa(nome, rg, telefone, endereco)
        pessoas.append(pessoa)
    
    return pessoas

def salvardados(pessoas):
    # Salvar todos os dados no arquivo csv
    with open('dadospessoas.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Nome', 'RG', 'Telefone', 'Endereço']) # <-- cabeçalho da lista
        for pessoa in pessoas:
            writer.writerow([pessoa.nome, pessoa.rg, pessoa.telefone, pessoa.endereco])

# Fluxo principal
pessoas = receber_dados()
salvardados(pessoas)

print("Dados salvos com sucesso no arquivo 'dados_pessoas.csv'.")
