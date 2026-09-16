import mysql.connector
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

con = os.getenv("SENHA")

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

conexao = mysql.connector.connect(
    host = "MacBook-Air-de-Felipe-3.local",
    database = "nether_recursos",
    user = "LAIN_FELIX",
    password = con
)

cursor = conexao.cursor()

class Mina():
    def ADICIONAR_MATERIAL(self):
        material = input("Digite o nome do material: ").upper()
        quantidade = int(input("Digite a quantidade desse material em estoque: "))


        cursor.execute("INSERT INTO MINA (material,quantidade) VALUES (%s,%s)", (material,quantidade,))
        conexao.commit()

    def VER_MATERIAL(self):
        comando = "SELECT * FROM MINA"
        df = pd.read_sql(comando, conexao)

        pd.set_option('display.max_columns', None)
        print(df)

    def ATUALIZAR_QUANTIDADE(self):
        id_material = int(input("Digite oo ID do material para ser alterado: "))
        quantidade = int(input("Digite a nova quantidade do material em questão: "))

        cursor.execute("UPDATE MINA SET quantidade = %s WHERE id = %s",(quantidade,id_material,))
        conexao.commit()

    def EXCLUIR_MATERIAL(self):
        id_material = int(input("Digite oo ID do material para ser excluido: "))

        cursor.execute("DELETE FROM MINA WHERE id = %s", (id_material,))
        conexao.commit()

ativar = Mina()

def mina():
    resposta = 0

    while True:

        resposta = int(input("1- ADICIONAR MATERIAL\n2- CONFERIR MATERIAL\n3- ATUALIZAR QUANTIDADE\n4- EXCLUIR QUANTIDADE\n->"))

        if resposta == 1:
            limpar()
            ativar.ADICIONAR_MATERIAL()

        elif resposta == 2:
            limpar()
            ativar.VER_MATERIAL()
        
        elif resposta == 3:
            limpar()
            ativar.ATUALIZAR_QUANTIDADE()

        elif resposta == 4:
            limpar()
            ativar.EXCLUIR_MATERIAL()

def main():
    resposta = 0

    while True:
        resposta = int(input("1 - MINA\n->"))

        if resposta == 1:
            limpar()
            mina()

if __name__ == "__main__":
    main()