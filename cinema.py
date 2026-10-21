import os

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def retorno():
    print("--------------------")
    input("Digite qualquer valor para retornar: ")
    limpar()

grafo = {}

class CinemaCon():
    def __init__(self):
        self.cinema = ""
        self.loc = ""
        self.preco = 0
        self.ponto = ""
        self.referencia = ""

    def adicionar_no(self):
        limpar()
        self.cinema = input("Digite o nome do cinema: ").upper()
        self.loc = input("Digite a localização: ").upper()
        preco_int = float(input("Digite o preço do ingreço: "))

        self.preco = (preco_int * 50) / 100

        self.ponto = input("Digite o ponto de ônibus que leva para lá: ").upper()

        conexao = {
            "Nome do Cinema" : self.cinema,
            "Localização" : self.loc,
            "Preço (inteiro)" : preco_int,
            "Preço (meia entrada)" : self.preco,
            "Ônibus" : self.ponto
        }

        grafo[self.loc] = []

        limpar()

        return conexao

    def adicionar_aresta(self):
        limpar()
        dados = self.adicionar_no()

        if len(grafo) < 2:
            print("Cadastre mais um cinema para poder criar uma conexão.")
            retorno()
            return

        self.referencia = dados["Localização"]
        destino = input("Digite a localização que deseja ir: ").upper()

        while destino not in grafo or destino == self.referencia:
            print("Destino não consta na lista")
            destino = input("Digite novamente: ").upper()
                

        grafo[self.referencia].append(destino)
        grafo[destino].append(self.referencia)

        retorno()

    def listar_grafo(self):
        limpar()
        print("CINEMAS REGISTRADOS:")
        for no in grafo:
            print(f"{no} -> {grafo[no]}")

        retorno()

cinema = CinemaCon()

def main():
    resposta = 0

    while True:
        resposta = int(input("1 - CRIAR CONEXÃO\n2 - LISTAR GRAFOS\n->"))

        if resposta == 1:
            cinema.adicionar_aresta()

        elif resposta == 2:
            cinema.listar_grafo()

if __name__ == "__main__":
    main()