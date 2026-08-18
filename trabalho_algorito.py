import sqlite3
import os

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def cadastro():
    limpar()
    class Cliente():
        def __init__(self):
            self.nome = ""
            self.cpf = 0
            self.credito = 0
            self.endereco = ""
            self.cep = 0
            self.cidade = ""
            self.estado = ""
            self.cargo = ""

        def cadastro_iniciar(self):
            print("Bem-vindo ao sistema de cadastro de funcionários da Hells Market")
            print("Para iniciar preenchencha o campo de informações básicas:")

            self.nome = input("Digite o seu nome: ")
            self.cpf = int(input("Digite o seu CPF: "))
            self.credito = float(input("Digite o seu limite de crédito: "))
            self.endereco = input("Digite o seu endereço: ")
            self.cep = int(input("Digite o seu CEP: "))
            self.cidade = input("Digite a cidade em que vive: ")
            self.estado = input("Digite o estado em que vive: ")
            self.cargo = input("Digite o seu cargo na empresa: ")

            ficha_funcionario = {
                "Nome" : self.nome,
                "CPF" : self.cpf,
                "Crédito" : self.credito,
                "Endereço" : self.endereco,
                "CEP" : self.cep,
                "Cidade" : self.cidade,
                "Estado" : self.estado,
                "Cargo" : self.cargo
            }

            limpar()

            print("Cadastro Finalizado!")

            return ficha_funcionario

    funcionario = Cliente()
    funcinario_cadastrado = funcionario.cadastro_iniciar()

    banco = sqlite3.connect("hell_market_funcionarios.db")
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS hells_market ('Codigo' INTEGER PRIMARY KEY AUTOINCREMENT, 'Nome' TEXT, 'CPF' INTEGER UNIQUE, 'Crédito' REAL, 'Endereço' TEXT, 'CEP' INTEGER UNIQUE, 'Cidade' TEXT, 'Estado' TEXT, 'Cargo' TEXT)")
    cursor.execute("INSERT INTO hells_market (Nome, CPF, Crédito, Endereço, CEP, Cidade, Estado, Cargo) VALUES (:Nome, :CPF, :Crédito, :Endereço, :CEP, :Cidade, :Estado, :Cargo)", funcinario_cadastrado)
    banco.commit()
    banco.close()

    return funcinario_cadastrado

def mostrar_funcionarios():
    limpar()

    banco = sqlite3.connect("hell_market_funcionarios.db")
    banco.row_factory = sqlite3.Row
    cursor = banco.cursor()
    cursor.execute("SELECT * from hells_market ORDER BY Nome")
    dict_list = [dict(row) for row in cursor.fetchall()]

    for i in dict_list:
        print("---------------------------------")
        print("Código: ", i["Codigo"])
        print("Nome: ", i["Nome"])
        print("CPF: ", i["CPF"])
        print("Crédito: ", i["Crédito"])
        print("Endereço: ", i["Endereço"])
        print("CEP: ", i["CEP"])
        print("Cidade: ", i["Cidade"])
        print("Estado: ", i["Estado"])
        print("Cargo: ", i["Cargo"])

    print("-------------------------------------")
    input("Digite qualquer valor para retornar: ")

    limpar()

def excluir_cadastro():
    limpar()
    codigo_cadastro = int(input("Digite o seu código de identificaçõ: "))

    banco = sqlite3.connect("hell_market_funcionarios.db")
    cursor = banco.cursor()
    cursor.execute(f"DELETE FROM hells_market WHERE Codigo = {codigo_cadastro}")
    banco.commit()
    print("Cadastro excluido!")

    input("Digite qualquer valor para retornar: ")
    limpar()

def atualizar_cadastro():
    limpar()
    codigo_alterar = int(input("Digite o seu código de identificação: "))

    class Novo_Cadastro():
        def __init__(self):
            self.nome = ""
            self.cpf = 0
            self.credito = 0
            self.endereco = ""
            self.cep = 0
            self.cidade = ""
            self.estado = ""
            self.cargo = ""

        def cadastro_iniciar(self):
            print("Bem-vindo ao sistema de cadastro de funcionários da Hells Market")
            print("Para iniciar preenchencha o campo de informações básicas:")

            self.nome = input("Digite o seu nome: ")
            self.cpf = int(input("Digite o seu CPF: "))
            self.credito = float(input("Digite o seu limite de crédito: "))
            self.endereco = input("Digite o seu endereço: ")
            self.cep = int(input("Digite o seu CEP: "))
            self.cidade = input("Digite a cidade em que vive: ")
            self.estado = input("Digite o estado em que vive: ")
            self.cargo = input("Digite o seu cargo na empresa: ")

            ficha_funcionario = {
                "Nome" : self.nome,
                "CPF" : self.cpf,
                "Crédito" : self.credito,
                "Endereço" : self.endereco,
                "CEP" : self.cep,
                "Cidade" : self.cidade,
                "Estado" : self.estado,
                "Cargo" : self.cargo
            }

            limpar()

            print("Cadastro Finalizado!")

            return ficha_funcionario
        
    funcionario = Novo_Cadastro()
    funcionario_cadastrado = funcionario.cadastro_iniciar()

    banco = sqlite3.connect("hell_market_funcionarios.db")
    cursor = banco.cursor()
    cursor.execute(f"UPDATE hells_market SET Nome = :Nome, CPF = :CPF, Crédito = :Crédito, Endereço = :Endereço, CEP = :CEP, Cidade = :Cidade, Estado = :Estado, Cargo = :Cargo WHERE Codigo = {codigo_alterar}", funcionario_cadastrado)

    banco.commit()
    banco.close()

    print("Atualização concluída!")
    input("Digite qualquer valor para retornar: ")

    limpar()
    
    

def main():
    resposta = 0

    while True:
        resposta = int(input("1 - Cadastrar Funcionário \n2 - Mostrar funcionários\n3 - Excluir cadastro\n4 - Atualizar cadastro\n->"))

        if resposta == 1:
            cadastro()

        elif resposta == 2:
            mostrar_funcionarios()

        elif resposta == 3:
            excluir_cadastro()

        elif resposta == 4:
            atualizar_cadastro()

        else:
            print("Digite uma opção válida")


if __name__ == "__main__":
    main()