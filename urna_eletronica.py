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
    votar = int(input(print("Vote para presidente (candidatos de 2026): ")))

    if votar not in candidatos_disponiveis:
        print("Este candidato não existe, tente novamente")
        votar = input(print("Vote para presidente (candidatos de 2026): "))
    
    else:
        print("Voto confirmado!")
        print("Digite qualquer valor para retornar: ")
        input()

    for presidente, numero in candidatos.items():
        if votar == numero:
            localizado = presidente

            return localizado
            

    banco = sqlite3.connect("votos.db")
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS ""tabela_votos"" ('numero_candidato' INTEGER UNIQUE,PRIMARY KEY('numero_candidato')")
    cursor.execute("INSERT INTO tabela_votos (numero_candidato) VALUES (:CLARIANA BARAO, :EDMILSON COSTA, :AUGUSTO CURY, :FLAVIO BOLSONARO, :HERTZ DIAS, :LULA, :PABLO MARÇAL, :RENAN SANTOS, :RONALDO CAIADO, :RUI COSTA PIMENTA, :SAMARA MARTINS, :WILSON GRASSI JUNIOR, :ROMEU ZEMA)", localizado)
    banco.commit()
    banco.close()

def conferir_ganhador():
    limpar()
    engine = create_engine("sqlite:///Users/felipefelix/Downloads/PROJECTS/urna_eletronica/urna_eletronica.py votos.db")
    df = pd.read_sql_query("SELECT * FROM votos", engine)

    candidato_vencedor = pd.Series(df.values.ravel()).mode()[0]

    print(f"O candidato vencedor até agora é: {candidato_vencedor}")
    print("Digite qualquer valor para retornar: ")
    input()
    limpar()

def main():
    resposta = 0

    while True:
        print("Bem-Vindo a urna eletrônica!")
        resposta = int(input(print("Escolha uma das opções:\n1- Votar\n2- Exibir vencedor\n->")))

        if resposta == 1:
            votar()

        elif resposta == 2:
            conferir_ganhador()

        else:
            print("Digite uma opção válida!")


if __name__ == "__main__":
    main()
        

