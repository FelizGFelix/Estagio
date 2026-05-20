import os

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

lista_reviews = []

def main1():
    class Music():
        def __init__(self):
            self.musica = ""
            self.nota = 0
            self.critica = ""

        def main(self):
            self.musica = input("Digite o nome da música: ")
            self.nota = float(input("Digite a sua nota: "))
            self.critica = input("Digite a sua critica: ")

            review = {
                "Música" : self.musica,
                "Nota" : self.nota,
                "Critica" : self.critica
            }

            lista_reviews.append(review)

    variavel = input("Digite o nome do artista/banda: ")
    variavel = Music()
    variavel.main()

    limpar()
        
    
def main2():
    for i in lista_reviews:
        print("----------------------------------")
        print("Nome: ", i["Música"])
        print("Nota: ", i["Nota"])
        print("Critica: ", i["Critica"])

    print("----------------------------------")
    input("Deseja voltar para o menu principal? digite qualquer tecla: ")
    principal()


def principal():
    var = True

    while var:
        resposta = int(input("Escolha uma das opções abaixo:\n -> 1: escrever uma nota review\n -> 2: acessar suas reviews\n-> "))

        if resposta == 1:
            limpar()
            main1()

        elif resposta == 2:
            limpar()
            var = False
            main2()
        
if __name__ == "__main__":
    principal()