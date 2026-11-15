import os
import networkx as nx
import matplotlib.pyplot as plt
from dotenv import load_dotenv

grafo = nx.Graph()

load_dotenv()

con = os.getenv("senha")
pc = os.getenv("senhapc")

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def retorno():
    print("--------------------")
    input("Digite qualquer valor para retornar: ")
    limpar()

def senha():
    print("Digite a senha para liberar acesso ao programa: ")

    contador = 0

    resposta = input("-> ")

    while resposta != con or resposta != pc:

        if resposta == con or resposta == pc:

            limpar()
             
            while True:
                main()
        
        else:

            limpar()

            contador += 1
            print("Acesso negado, tente novamente!")

            resposta = input("-> ")

            if contador == 5:
                print("Acesso máximo de tentativas excedido, bloqueando o sistema!")
                break

class Dados():
    def __init__(self):
        self.nome = ""
        self.info = ""

    def inserir_dados(self):
        limpar()
        self.nome = input("Digite o nome do suspeito/local: ").upper()

        lista_info = []
        
        ativo = True

        while ativo:
            print("Digite tudo o que sabe relacionado a isso (Digite a senha do sistema para parar): ")

            self.info = input("-> ").upper()

            lista_info.append(self.info)

            if self.info.lower() == con or self.info.lower() == pc:
                limpar()
                ativo = False
                print("INFORMAÇÕES SALVAS COM SUCESSO!")

        lista_info.pop()

        entidade = {
            "Nome" : self.nome,
            "Informações" : lista_info
        }

        grafo.add_node(self.nome, **entidade)

        retorno()

    def add_relacao(self):
        limpar()
        print("ENTIDADES CONHECIDAS: ")
        print(grafo.nodes())
        print("QUAL DESSES DESEJA LIGAR?")
        resposta = input("-> ").upper()
        print("A QUAL ELE ESTÁ LIGADO?")
        resposta2 = input("-> ").upper()

        grafo.add_edge(resposta, resposta2)

        retorno()

        return grafo

    def vizu_entidades(self):
        limpar()
        print("ENTIDADES CONHECIDAS: ")
        print(grafo.nodes())
        print("QUAL DELAS DESEJA VER AS INFORMAÇÕES?")
        resposta = input("-> ").upper()

        if resposta in grafo:
            print(f"NOME: {grafo.nodes[resposta]["Nome"]}")

            print("INFORMAÇÕES: ")

            for i in grafo.nodes[resposta]["Informações"]:
                print(f"- {i}")

        retorno()

    def visualizar_grafos_mapa(self):
        limpar()
        pos = nx.spring_layout(grafo)
        nx.draw(grafo, pos, with_labels=True)
        rotulos = nx.get_edge_attributes(grafo, "weight")
        nx.draw_networkx_edge_labels(grafo, pos, edge_labels=rotulos)
        plt.show()

principal = Dados()

def main():
    resposta = 0

    while True:
        resposta = int(input("1 - INSERIR ENTIDADES\n2 - ADICIONAR LIGAÇÃO\n3 - VER INFORMAÇÕES DAS ENTIDADES\n4 - VISUALIZAR RELAÇÕES\n->"))

        if resposta == 1:
            principal.inserir_dados()

        elif resposta == 2:
            principal.add_relacao()

        elif resposta == 3:
            principal.vizu_entidades()

        elif resposta == 4:
            principal.visualizar_grafos_mapa()

if __name__ == "__main__":
    senha()