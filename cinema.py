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
        self.saldo = 0
        self.nome = ""

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

        usuario = {
            "Nome" : self.nome,
            "Saldo atual" : self.saldo,
        }

        grafo.add_node(self.nome, **usuario)

        for no, dados in grafo.nodes(data=True):
            if "Localização" in dados:
                grafo.add_edge(self.nome, no, weight=dados["Preço (meia entrada)"])

        retorno()

    def adicionar_cinema(self):
        limpar()
        self.cinema = input("Digite o nome do cinema: ").upper()
        self.cidade = input("Digite a cidade em que esse cinema fica: ").upper()
        self.loc = input("Digite a localização (estabelecimento aonde fica o cinema): ").upper()
        preco_int = float(input("Digite o preço do ingreço: "))

        self.preco = round((preco_int * 50) / 100, 2)

        self.transporte = input("Digite o meio para chegar até lá: ").upper()

        conexao = {        
            "Nome do Cinema" : self.cinema,
            "Localização" : self.loc,
            "Preço (inteiro)" : preco_int,
            "Preço (meia entrada)" : self.preco,
            "Transporte" : self.transporte
        }

        grafo.add_node(self.cinema, **conexao)

        for no, dados in grafo.nodes(data=True):
            if "Saldo atual" in dados:
                grafo.add_edge(no, self.cinema, weight=self.preco)

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
        print("Qual grafo você gostaria de conferir os dados?")
        print(grafo.nodes())

        escolhido = input("-> ").upper()

        if escolhido in grafo:
            print(grafo.nodes[escolhido])

        retorno()

    def dijkstra(self):
        limpar()

        cinemas = [no for no, dados in grafo.nodes(data=True) if "Localização" in dados]

        melhor = min(
            cinemas,
            key=lambda c: nx.dijkstra_path_length(grafo, self.nome, c, weight="weight")
        )
        custo_total = nx.dijkstra_path_length(grafo, self.nome, melhor, weight="weight")

        print(f"Cinema de menor custo: {melhor}")
        print(f"Custo total: {custo_total}")

        retorno()

    def calcular_custo(self):
        limpar()
        print("Qual cinema você gostaria de calcular os custos?")
        print([no for no, dados in grafo.nodes(data=True) if "Nome do Cinema" in dados])

        escolhido = input("-> ").upper()

        if escolhido in grafo:
            calcular = grafo.nodes[escolhido]["Preço (inteiro)"]

            resultado = self.saldo - calcular

            resultado2 = self.saldo - ((calcular * 50)/100)

            print(f"Resultado:\nGasto com a inteira: {resultado}\nGasto com a meia entrada: {resultado2}")

        retorno()

cinema = CinemaCon()

def main():
    resposta = 0

    while True:
        resposta = int(input("1 - ADICIONAR MAIS PESSOAS\n2 - ADICIONAR CINEMA\n3 - VISUALIZAR MAPA\n4 - CONFERIR ATRIBUTOS\n5 - CONFERIR O MENOR VALOR\n6 - CONFERIR GASTOS\n->"))

        if resposta == 1:
            cinema.info_origem()

        elif resposta == 2:
            cinema.adicionar_cinema()

        elif resposta == 3:
            cinema.visualizar_grafos_mapa()

        elif resposta == 4:
            cinema.conferir_grafos()

        elif resposta == 5:
            cinema.dijkstra()

        elif resposta == 6:
            cinema.calcular_custo()

if __name__ == "__main__":
    cinema.info_origem()
    main()