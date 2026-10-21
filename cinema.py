import os
import networkx as nx
import matplotlib.pyplot as plt

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
        self.destino = ""

    def info_origem(self):
        limpar()

        self.nome = input("Digite o seu nome: ").upper()

        if not self.nome:
            limpar()
            print("Digite um nome váldio!")
            self.nome = input("Digite o seu nome: ").upper()

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

        self.destino = input("Digite o local a qual deseja ir: ").upper()

        if not self.destino:
            limpar()
            print("Digite um valor válido!")
            self.destino = input("Digite o local a qual deseja ir (nome do estabelecimento): ").upper()

        else:
            print("Local registrado com sucesso!")

        usuario = {
            "Nome" : self.nome,
            "Saldo atual" : self.saldo,
            "Ponto de origem" : self.origem,
            "Local que deseja ir" : self.destino
        }

        grafo.add_node(self.nome, **usuario)

        grafo.add_edge(self.nome, self.origem)
        grafo.add_edge(self.origem, self.destino)

        retorno()

    def adicionar_cinema(self):
        limpar()
        self.cinema = input("Digite o nome do cinema: ").upper()
        self.cidade = input("Digite a cidade em que esse cinema fica: ").upper()
        self.loc = input("Digite a localização (estabelecimento aonde fica o cinema): ").upper()
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

        if self.destino != self.loc:
            grafo.add_edge(self.destino, self.loc, weight=0)

        grafo.add_node(self.loc, **conexao)

        grafo.add_edge(self.origem, self.loc, weight = self.preco)

        retorno()

        #print(grafo.nodes())
        #print(grafo.edges())
        #print(grafo.nodes(data=True))

        return grafo
    
    def visualizar_grafos_mapa(self):
        limpar()
        pos = nx.spring_layout(grafo)
        nx.draw(grafo, pos, with_labels=True)
        rotulos = nx.get_edge_attributes(grafo, "weight")
        nx.draw_networkx_edge_labels(grafo, pos, edge_labels=rotulos)
        plt.show()

    def conferir_grafos(self):
        limpar()
        print("O grafo você gostaria de conferir os dados?")
        print(grafo.nodes())

        escolhido = input("-> ").upper()

        if escolhido in grafo:
            print(grafo.nodes[escolhido])

        retorno()

cinema = CinemaCon()

def main():
    resposta = 0

    while True:
        resposta = int(input("1 - INFORMAÇÕES DE ORIGEM\n2 - ADICIONAR CINEMA\n3 - VISUALIZAR MAPA\n4 - CONFERIR ATRIBUTOS\n->"))

        if resposta == 1:
            cinema.info_origem()

        elif resposta == 2:
            cinema.adicionar_cinema()

        elif resposta == 3:
            cinema.visualizar_grafos_mapa()

        elif resposta == 4:
            cinema.conferir_grafos()

if __name__ == "__main__":
    main()