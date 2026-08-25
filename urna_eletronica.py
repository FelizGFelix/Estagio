import os
import sqlite3
import pandas as pd
from sqlalchemy import create_engine

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

candidatos_disponiveis = [27, 21, 70, 22, 16, 13, 28, 14, 55, 29, 80, 35, 30]

candidatos = {
    "CLARIANA BARAO": 27,
    "EDMILSON COSTA" : 21,
    "AUGUSTO CURY" : 70,
    "FLAVIO BOLSONARO" : 22,
    "HERTZ DIAS" : 16,
    "LULA" : 13,
    "PABLO MARÇAL" : 28,
    "RENAN SANTOS" : 14,
    "RONALDO CAIADO" : 55,
    "RUI COSTA PIMENTA" : 29,
    "SAMARA MARTINS" : 80,
    "WILSON GRASSI JUNIOR" : 35,
    "ROMEU ZEMA" : 30
}

def votar():
    limpar()
    votar = int(input("Vote para presidente (candidatos de 2026): "))

    while votar not in candidatos_disponiveis:
        print("Este candidato não existe, tente novamente")
        votar = int(input("Vote para presidente (candidatos de 2026): "))

    if votar in candidatos_disponiveis:
        print("Voto confirmado!")

    for presidente, numero in candidatos.items():
        if votar == numero:
            localizado = presidente
            break

    banco = sqlite3.connect("votos.db")
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tabela_votos ('numero_candidato' INTEGER)")
    cursor.execute("INSERT INTO tabela_votos (numero_candidato) VALUES (?)", (votar,))
    banco.commit()
    banco.close()

    input("Digite qualquer valor para retornar: ")
    limpar()

def conferir_ganhador():
    limpar()
    engine = create_engine("sqlite:///votos.db")
    df = pd.read_sql_query("SELECT * FROM tabela_votos", engine)

    candidato_vencedor = pd.Series(df.values.ravel()).mode()[0]

    for presidente, numero in candidatos.items():
        if numero == candidato_vencedor:
            localizado = presidente
            break

    print(f"O candidato vencedor até agora é: {localizado}")
    input("Digite qualquer valor para retornar: ")
    limpar()

def main():
    resposta = 0

    while True:
        print("Bem-Vindo a urna eletrônica!")
        resposta = int(input("Escolha uma das opções:\n1- Votar\n2- Exibir vencedor\n->"))

        if resposta == 1:
            votar()

        elif resposta == 2:
            conferir_ganhador()

        else:
            limpar()
            print("Digite uma opção válida!")


if __name__ == "__main__":
    main()
        

