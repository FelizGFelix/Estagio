import sqlite3
import random
import os
import pandas as pd

banco = sqlite3.connect("alunos.db")
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS chamada_alunos ('aluno'	TEXT,'num_chamada' INTEGER PRIMARY KEY AUTOINCREMENT)")


def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

alunos_nomes = ["Denji", 
                "Marceline", 
                "Gwendoly Poole", 
                "James Wattson", 
                "Percy Jackson", 
                "Waly West", 
                "Laura", 
                "Nathiel Phillipes", 
                "Shang Chi", 
                "Yumiko Akame", 
                "Zuri Baraka", 
                "Alexandru Popa", 
                "Oliver Smith", 
                "Ivan", 
                "Shigeo Kageyama", 
                "Ayna Niyazon", 
                "Nanaue", 
                "Yelena Way",
                "Daniel Duarte Dantas"]
class Aluno():
    def inicializacao(self):
        alunos_chamada = random.sample(alunos_nomes, len(alunos_nomes))

        for i in alunos_chamada:
            cursor.execute("INSERT INTO chamada_alunos (aluno) VALUES (?)", (i,))
            
        banco.commit()

    def aluno_random(self):
        num_indexrandom = random.randrange(1, 19)
        cursor.execute("SELECT * FROM chamada_alunos WHERE num_chamada = (?)", (num_indexrandom,))
        resultado = cursor.fetchone()

        print(f"{resultado}")
    
    def escolher_entre2alunos(self):
        impar = input("IMPAR, ALUNO 1: ")
        par = input("PAR, ALUNO 2: ")

        num = random.randrange(1, 7)

        if num % 2 == 0:
            print(par) 
        else:
            print(impar)

    def mostrar_alunos(self):
        comando = "SELECT * FROM chamada_alunos"
        df = pd.read_sql(comando, banco)

        pd.set_option('display.max_columns', None)
        print(df)

    def excluir_aluno(self):
        id_aluno = int(input("Digite o ID do Aluno: "))
        cursor.execute("DELETE FROM chamada_alunos WHERE num_chamada = (?)", (id_aluno,))

        banco.commit()

    def adicionar_aluno(self):
        nome_aluno = input("Digite o nome do aluno: ")
        cursor.execute("INSERT INTO chamada_alunos (aluno) VALUES (?)", (nome_aluno,))

        banco.commit()

    def contar_alunos(self):
        cursor.execute("SELECT COUNT(*) FROM chamada_alunos")
        (total,) = cursor.fetchone()
        print(f"Total de alunos: {total}")

alunos = Aluno()

def main():
    resposta = 0
    while True:
        cursor.execute("SELECT COUNT(*) FROM chamada_alunos")
        valores = cursor.fetchone()[0]

        if valores > 0:
            print(f"BANCO ATIVO: {True}")

        else:
            print(f"BANCO ATIVO: {False}")

        resposta = int(input("1- Inciar Programa\n2- Escolher um aluno aleatório\n3- Decidir batalha NPC\n4- Mostrar Alunos\n5- Excluir Aluno\n6- Adicionar Aluno\n7- Contar Alunos\n->"))

        if resposta == 1:
            limpar()
            alunos.inicializacao()

        elif resposta == 2:
            limpar()
            alunos.aluno_random()
        
        elif resposta == 3:
            limpar()
            alunos.escolher_entre2alunos()
        
        elif resposta == 4:
            limpar()
            alunos.mostrar_alunos()

        elif resposta == 5:
            limpar()
            alunos.excluir_aluno()

        elif resposta == 6:
            limpar()
            alunos.adicionar_aluno()

        elif resposta == 7:
            limpar()
            alunos.contar_alunos()

if __name__ == "__main__":
    main()