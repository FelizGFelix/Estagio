import os
import networkx as nx

grafo = nx.Graph()

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def retorno():
    print("--------------------")
    input("Digite qualquer valor para retornar: ")
    limpar()

class CinemaCon():
    def __init__(self):
        self.cinema = ""
        self.cidade = ""
        self.loc = ""
        self.preco = 0
        self.transporte = ""
        self.referencia = ""
        self.origem = ""
        self.saldo = 0
        self.nome = ""

    def info_origem(self):
        limpar()

        self.nome = input("Digite o seu nome: ")

        if not self.nome:
            limpar()
            print("Digite um nome váldio!")
            self.nome = input("Digite o seu nome: ")

        else:
            print("Nome registrado com sucesso!")

        self.saldo = float(input("Digite o seu saldo atual: "))

        print("Saldo registrado com sucesso!")

        self.origem = input("Digite o seu ponto de origem: ").upper()

        if not self.origem:
            limpar()
            print("Digite um valor váldio!")
            self.origem = input("Digite o seu ponto de origem: ").upper()

        else:
            print("Local registrado com sucesso!")

        usuario = {
            "Nome" : self.nome,
            "Saldo atual" : self.saldo,
            "Ponto de origem" : self.origem
        }

        grafo.add_node(self.saldo, **usuario)

        retorno()

    def adicionar_cinema(self):
        limpar()
        self.cinema = input("Digite o nome do cinema: ").upper()
        self.cidade = input("Digite a cidade em que esse cinema fica: ").upper()
        self.loc = input("Digite a localização: ").upper()
        preco_int = float(input("Digite o preço do ingreço: "))

        self.preco = (preco_int * 50) / 100

        self.transporte = input("Digite o meio para chegar até lá: ").upper()

        conexao = {
            "Nome do Cinema" : self.cinema,
            "Localização" : self.loc,
            "Preço (inteiro)" : preco_int,
            "Preço (meia entrada)" : self.preco,
            "Ônibus" : self.transporte
        }

        grafo.add_node(self.loc, **conexao)

        grafo.add_edge(self.origem, self.loc, weight = self.preco)

        retorno()

        #print(grafo.nodes())
        #print(grafo.edges())
        #print(grafo.nodes(data=True))

        return grafo

cinema = CinemaCon()

def main():
    resposta = 0

    while True:
        resposta = int(input("1 - INFORMAÇÕES DE ORIGEM\n2 - ADICIONAR CINEMA\n->"))

        if resposta == 1:
            cinema.info_origem()

        elif resposta == 2:
            cinema.adicionar_cinema()

if __name__ == "__main__":
    main()