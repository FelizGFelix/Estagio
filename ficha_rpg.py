import sqlite3
import os

registros = []

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def criar():
    class Ficha():
        def __init__(self):
            self.nome = ""
            self.HP = 0
            self.MP = 0
            self.forca = 0
            self.agilidade = 0
            self.PDF = 0
            self.inteligencia = 0
            self.resistencia = 0
            self.armadura = 0

        def base(self):
            self.nome = input("Digite o nome do seu personagem: ")
            limpar()
            print(f"Prazer {self.nome}, hora de definir os seus atributos!")
            print("Defina seus atributos: ")
            
            self.forca = int(input("Força: "))
            self.agilidade = int(input("Agilidade: "))
            self.PDF = int(input("PDF: "))
            self.inteligencia = int(input("Inteligência: "))
            self.resistencia = int(input("Resistência: "))
            self.armadura = int(input("Armadura: "))

            vida = self.resistencia * 5
            mp = self.inteligencia * 5

            personagem = {
                    "Nome" : self.nome,
                    "HP" : vida,
                    "MP" : mp,
                    "Forca" : self.forca,
                    "Agilidade" : self.agilidade,
                    "PDF" : self.PDF,
                    "Inteligencia" : self.inteligencia,
                    "Resistencia" : self.resistencia,
                    "Armadura" : self.armadura
                }
            
            registros.append(personagem)
            limpar()
            return personagem

    char = Ficha()
    personagem = char.base()
    banco = sqlite3.connect("registro_fichas.db")
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS character (Nome TEXT, HP INTEGER, MP INTEGER, Forca INTEGER, Agilidade INTEGER, PDF INTEGER, Inteligencia INTEGER, Resistencia INTEGER, Armadura INTEGER)")
    cursor.execute("INSERT INTO character VALUES (:Nome, :HP, :MP, :Forca, :Agilidade, :PDF, :Inteligencia, :Resistencia, :Armadura)", personagem)
    banco.commit()
    banco.close()

def mostrar():
    for i in registros:
        print("Nome:", i["Nome"])
        print("HP:", i["HP"])
        print("MP:", i["MP"])
        print("Forca:", i["Forca"])
        print("Agilidade:", i["Agilidade"])
        print("PDF:", i["PDF"])
        print("Inteligência:", i["Inteligencia"])
        print("Resistência:", i["Resistencia"])
        print("Armadura: ", i["Armadura"])
        print("---------------------")
    
    input("Digite qualquer valor para voltar: ")
    limpar()


while True:
    try: 
        resposta = int(input("Digite escolha uma das opções:\n1 - Criar ficha\n2 - Acessar fichas\n-> "))

        if resposta == 1:
            limpar()
            criar()

        elif resposta == 2:
            limpar()
            mostrar()

        else:
            limpar()
            print("Digite uma opção válida")
            input("Digite qualquer valor para voltar: ")

    except:
        limpar()
        print("Digite uma opção válida")
        input("Digite qualquer valor para voltar: ")


    



