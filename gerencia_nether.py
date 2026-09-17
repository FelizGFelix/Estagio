import mysql.connector
import os
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt

load_dotenv()

con = os.getenv("SENHA")
pc = os.getenv("PC")

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def retornar():
    print(f"ATUALIZAÇÃO: {True}")
    input("Digite qualquer valor para retornar: ")
    limpar()

conexao = mysql.connector.connect(
    host = "MacBook-Air-de-Felipe-3.local",
    database = "nether_recursos",
    user = "LAIN_FELIX",
    password = con
)

def senha():
    print("Bem-Vindo ao sistema de gerencia do Nether!")
    resposta = input("Digite a senha: ")

    contador = 0

    while resposta != con or resposta != pc:
        if resposta == con or resposta == pc:
            limpar()
            print("Acesso liberado!")

            while True:
                main()

        elif resposta != con or resposta != pc:
            print("Acesso negado, tente novamente!")
            resposta = input("Digite a senha: ")

            contador+=1

            if contador == 5:
                print("Número de tentativas excedido!")
                print("Sistema bloqueado!")
                break

cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS CAVERNA (MATERIAL TEXT, QUANTIDADE INTEGER, id  INTEGER PRIMARY KEY AUTO_INCREMENT)")


class Mina():
    def ADICIONAR_MATERIAL_MINA(self):
        material = input("Digite o nome do material: ").upper()
        quantidade = int(input("Digite a quantidade desse material em estoque: "))


        cursor.execute("INSERT INTO MINA (material,quantidade) VALUES (%s,%s)", (material,quantidade,))
        conexao.commit()
        retornar()

    def VER_MATERIAL_MINA(self):
        comando = "SELECT * FROM MINA"
        df = pd.read_sql(comando, conexao)

        pd.set_option('display.max_columns', None)
        print(df)
        retornar()

    def ATUALIZAR_QUANTIDADE_MINA(self):
        id_material = int(input("Digite oo ID do material para ser alterado: "))
        quantidade = int(input("Digite a nova quantidade do material em questão: "))

        cursor.execute("UPDATE MINA SET quantidade = %s WHERE id = %s",(quantidade,id_material,))
        conexao.commit()
        retornar()

    def EXCLUIR_MATERIAL_MINA(self):
        id_material = int(input("Digite oo ID do material para ser excluido: "))

        cursor.execute("DELETE FROM MINA WHERE id = %s", (id_material,))
        conexao.commit()
        retornar()

    def GRAFICO_MATERIAL_MINA(self):
        cursor.execute("SELECT * FROM MINA")
        dados = cursor.fetchall()

        categorias = [linha[0] for linha in dados]
        valores = [linha[1] for linha in dados]

        plt.bar(categorias, valores, color='red')

        plt.title('Valores por Categoria')
        plt.xlabel('Materiais')
        plt.ylabel('Quantidade')

        plt.show()
        plt.close()
        retornar()

ativar = Mina()

class Caverna():
    def ADICIONAR_MATERIAL_CAVERNA(self):
        material = input("Digite o nome do material: ").upper()
        quantidade = int(input("Digite a quantidade desse material em estoque: "))


        cursor.execute("INSERT INTO CAVERNA (material,quantidade) VALUES (%s,%s)", (material,quantidade,))
        conexao.commit()
        retornar()

    def VER_MATERIAL_CAVERNA(self):
        comando = "SELECT * FROM CAVERNA"
        df = pd.read_sql(comando, conexao)

        pd.set_option('display.max_columns', None)
        print(df)
        retornar()

    def ATUALIZAR_QUANTIDADE_CAVERNA(self):
        id_material = int(input("Digite oo ID do material para ser alterado: "))
        quantidade = int(input("Digite a nova quantidade do material em questão: "))

        cursor.execute("UPDATE CAVERNA SET quantidade = %s WHERE id = %s",(quantidade,id_material,))
        conexao.commit()
        retornar()

    def EXCLUIR_MATERIAL_CAVERNA(self):
        id_material = int(input("Digite oo ID do material para ser excluido: "))

        cursor.execute("DELETE FROM CAVERNA WHERE id = %s", (id_material,))
        conexao.commit()
        retornar()

    def GRAFICO_MATERIAL_CAVERNA(self):
        cursor.execute("SELECT * FROM CAVERNA")
        dados = cursor.fetchall()

        categorias = [linha[0] for linha in dados]
        valores = [linha[1] for linha in dados]

        plt.bar(categorias, valores, color='red')

        plt.title('Valores por Categoria')
        plt.xlabel('Materiais')
        plt.ylabel('Quantidade')

        plt.show()
        plt.close()
        retornar()
    
ativar2 = Caverna()

def caverna_overworld():
    resposta = 0

    while True:

        resposta = int(input("1- ADICIONAR MATERIAL\n2- CONFERIR MATERIAIS\n3- ATUALIZAR QUANTIDADE\n4- EXCLUIR MATERIAL\n5- GRÁFICO MATERIAIS\n6- RETORNAR\n->"))

        if resposta == 1:
            limpar()
            ativar2.ADICIONAR_MATERIAL_CAVERNA()

        elif resposta == 2:
            limpar()
            ativar2.VER_MATERIAL_CAVERNA()

        elif resposta == 3:
            limpar()
            ativar2.ATUALIZAR_QUANTIDADE_CAVERNA()

        elif resposta == 4:
            limpar()
            ativar2.EXCLUIR_MATERIAL_CAVERNA()

        elif resposta == 5:
            limpar()
            ativar2.GRAFICO_MATERIAL_CAVERNA()

        elif resposta == 6:
            limpar()
            main()
    
def mina_nether():
    resposta = 0

    while True:

        resposta = int(input("1- ADICIONAR MATERIAL\n2- CONFERIR MATERIAIS\n3- ATUALIZAR QUANTIDADE\n4- EXCLUIR MATERIAL\n5- GRÁFICO MATERIAIS\n6- RETORNAR\n->"))

        if resposta == 1:
            limpar()
            ativar.ADICIONAR_MATERIAL_MINA()

        elif resposta == 2:
            limpar()
            ativar.VER_MATERIAL_MINA()
        
        elif resposta == 3:
            limpar()
            ativar.ATUALIZAR_QUANTIDADE_MINA()

        elif resposta == 4:
            limpar()
            ativar.EXCLUIR_MATERIAL_MINA()

        elif resposta == 5:
            limpar()
            ativar.GRAFICO_MATERIAL_MINA()

        elif resposta == 6:
            limpar()
            main()

def main():
    limpar()
    resposta = 0

    while True:
        resposta = int(input("1 - MINA - NETHER\n2 - CAVERNA - OVERWORLD\n->"))

        if resposta == 1:
            limpar()
            mina_nether()

        elif resposta == 2:
            limpar()
            caverna_overworld()

if __name__ == "__main__":
    senha()