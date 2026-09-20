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
    host = "localhost",
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

def atualizar_quantidade_global(tabela, id_registro, nova_qtd):
    cursor.execute(f"SELECT MATERIAL FROM {tabela} WHERE id = %s", (id_registro,))
    linha = cursor.fetchone()

    material = linha[0]

    cursor.execute("SELECT TABLE_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = DATABASE() AND COLUMN_NAME IN ('MATERIAL', 'QUANTIDADE') GROUP BY TABLE_NAME HAVING COUNT(*) = 2")
    tabelas = [t[0] for t in cursor.fetchall()]

    for t in tabelas:
        cursor.execute(
            f"UPDATE {t} SET QUANTIDADE = %s WHERE MATERIAL = %s",
            (nova_qtd, material)
        )
 
    conexao.commit()

class Mina():
    #lembrar que a tabela da mina se chama MINA
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
        atualizar_quantidade_global("MINA", id_material, quantidade)

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

    def ADICIONAR_MATERIAL_EXISTENTE_MINA():
        cursor.execute("SHOW TABLES;")
        tabelas = cursor.fetchall()

        print("Qual tabela deseja exportar o material?")
        for tabela in tabelas:
            print(tabela[0])

        resultado = input("->").upper()

        comando = f"SELECT * FROM {resultado}"

        df = pd.read_sql(comando, conexao)

        pd.set_option('display.max_columns', None)
        print(df)

        id_procurar = int(input("Digite o ID do material que deseja passar para a tabela: "))

        cursor.execute(f"INSERT INTO MINA (MATERIAL, QUANTIDADE) SELECT MATERIAL, QUANTIDADE FROM {resultado} WHERE id = %s", (id_procurar, ))

        conexao.commit()

        retornar()

ativar = Mina()

class Caverna():
    def __init__(self):
        cursor.execute("CREATE TABLE IF NOT EXISTS CAVERNA (MATERIAL TEXT, QUANTIDADE INTEGER, id  INTEGER PRIMARY KEY AUTO_INCREMENT)")
    #lembrar que a tabela da caverna se chama CAVERNA

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
        atualizar_quantidade_global("CAVERNA", id_material, quantidade)

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

    def ADICIONAR_MATERIAL_EXISTENTE_CAVERNA(self):
        cursor.execute("SHOW TABLES;")
        tabelas = cursor.fetchall()

        print("Qual tabela deseja exportar o minério?")
        for tabela in tabelas:
            print(tabela[0])

        resultado = input("->").upper()

        comando = f"SELECT * FROM {resultado}"

        df = pd.read_sql(comando, conexao)

        pd.set_option('display.max_columns', None)
        print(df)

        id_procurar = int(input("Digite o ID do material que deseja passar para a tabela: "))

        cursor.execute(f"INSERT INTO CAVERNA (MATERIAL, QUANTIDADE) SELECT MATERIAL, QUANTIDADE FROM {resultado} WHERE id = %s", (id_procurar, ))

        conexao.commit()

        retornar()

ativar2 = Caverna()

class Minerios():
    def __init__(self):
        cursor.execute("CREATE TABLE IF NOT EXISTS MINERIOS (MATERIAL TEXT, QUANTIDADE INTEGER, id  INTEGER PRIMARY KEY AUTO_INCREMENT)")

        conexao.commit()

    def ADICIONAR_MINERIO(self):
        material = input("Digite o nome do minério: ").upper()
        quantidade = int(input("Digite a quantidade desse material em estoque: "))


        cursor.execute("INSERT INTO MINERIOS (material,quantidade) VALUES (%s,%s)", (material,quantidade,))
        conexao.commit()
        retornar()

    def VER_MINERIO(self):
        comando = "SELECT * FROM MINERIOS"
        df = pd.read_sql(comando, conexao)

        pd.set_option('display.max_columns', None)
        print(df)
        retornar()

    def ATUALIZAR_QUANTIDADE_MINERIO(self):
        id_material = int(input("Digite oo ID do minério para ser alterado: "))
        quantidade = int(input("Digite a nova quantidade do minério em questão: "))

        cursor.execute("UPDATE MINERIOS SET quantidade = %s WHERE id = %s",(quantidade,id_material,))
        atualizar_quantidade_global("MINERIOS", id_material, quantidade)

        conexao.commit()
        retornar()

    def EXCLUIR_MINERIO(self):
        id_material = int(input("Digite oo ID do minério para ser excluido: "))

        cursor.execute("DELETE FROM MINERIOS WHERE id = %s", (id_material,))
        conexao.commit()
        retornar()

    def GRAFICO_MINERIO(self):
        cursor.execute("SELECT * FROM MINERIOS")
        dados = cursor.fetchall()

        categorias = [linha[0] for linha in dados]
        valores = [linha[1] for linha in dados]

        plt.bar(categorias, valores, color='red')

        plt.title('Valores por Categoria')
        plt.xlabel('Minérios')
        plt.ylabel('Quantidade')

        plt.show()
        plt.close()
        retornar()

    def ADICIONAR_MINERIO_EXISTENTE(self):
        cursor.execute("SHOW TABLES;")
        tabelas = cursor.fetchall()

        print("Qual tabela deseja exportar o minério?")
        for tabela in tabelas:
            print(tabela[0])

        resultado = input("->").upper()

        comando = f"SELECT * FROM {resultado}"

        df = pd.read_sql(comando, conexao)

        pd.set_option('display.max_columns', None)
        print(df)

        id_procurar = int(input("Digite o ID do material que deseja passar para a tabela: "))

        cursor.execute(f"INSERT INTO MINERIOS (MATERIAL, QUANTIDADE) SELECT MATERIAL, QUANTIDADE FROM {resultado} WHERE id = %s", (id_procurar, ))

        conexao.commit()

        retornar()

ativar3 = Minerios()    

def minerios_geral():
    resposta = 0

    while True:
        resposta = int(input("1- ADICIONAR MINÉRIO\n2- CONFERIR MINÉRIO\n3- ATUALIZAR QUANTIDADE\n4- EXCLUIR MINÉRIO\n5- GRÁFICO MINÉRIO\n6- ADICIONAR MINÉRIO EXISTENTE\n7- RETORNAR\n->"))

        if resposta == 1:
            limpar()
            ativar3.ADICIONAR_MINERIO()

        elif resposta == 2:
            limpar()
            ativar3.VER_MINERIO()

        elif resposta == 3:
            limpar()
            ativar3.ATUALIZAR_QUANTIDADE_MINERIO()

        elif resposta == 4:
            limpar()
            ativar3.EXCLUIR_MINERIO()

        elif resposta == 5:
            limpar()
            ativar3.GRAFICO_MINERIO()

        elif resposta == 6:
            limpar()
            ativar3.ADICIONAR_MINERIO_EXISTENTE()

        elif resposta == 7:
            limpar()
            main()

def caverna_overworld():
    resposta = 0

    while True:

        resposta = int(input("1- ADICIONAR MATERIAL\n2- CONFERIR MATERIAIS\n3- ATUALIZAR QUANTIDADE\n4- EXCLUIR MATERIAL\n5- GRÁFICO MATERIAIS\n6- ADICIONAR MATERIAL EXISTENTE\n7- RETORNAR\n->"))

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
            ativar2.ADICIONAR_MATERIAL_EXISTENTE_CAVERNA()

        elif resposta == 7:
            limpar()
            main()
    
def mina_nether():
    resposta = 0

    while True:

        resposta = int(input("1- ADICIONAR MATERIAL\n2- CONFERIR MATERIAIS\n3- ATUALIZAR QUANTIDADE\n4- EXCLUIR MATERIAL\n5- GRÁFICO MATERIAIS\n6- ADICONAR MATERIAL EXISTENTE\n7- RETORNAR\n->"))

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
            ativar.ADICIONAR_MATERIAL_EXISTENTE_MINA()

        elif resposta == 7:
            limpar()
            main()

def main():
    limpar()
    resposta = 0

    while True:
        resposta = int(input("1 - MINA - NETHER\n2 - CAVERNA - OVERWORLD\n3 - MINÉRIOS - GERAL\n->"))

        if resposta == 1:
            limpar()
            mina_nether()

        elif resposta == 2:
            limpar()
            caverna_overworld()

        elif resposta == 3:
            limpar()
            minerios_geral()

if __name__ == "__main__":
    senha()