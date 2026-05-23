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
            self.artista = input("Digite o nome do artista/banda: ")
            self.musica = input("Digite o nome da música: ")
            self.nota = float(input("Digite a sua nota: "))

            if self.nota > 10:
                    print("Valores acima de 10 não são permitidos")
                    self.nota = float(input("Digite um valor válido: "))

            self.critica = input("Digite a sua critica: ")

            review = {
                "Artista/Banda" : self.artista,
                "Música" : self.musica,
                "Nota" : self.nota,
                "Critica" : self.critica
            }

            lista_reviews.append(review)

            variavel = self.artista

    variavel = Music()
    variavel.main()

    limpar()
        
    
def main2():
    for i in lista_reviews:
        print("----------------------------------")
        print("Artista/Banda: ", i["Artista/Banda"])
        print("Nome: ", i["Música"])
        print("Nota: ", i["Nota"])
        print("Critica: ", i["Critica"])

    print("----------------------------------")
    input("Deseja voltar para o menu principal? digite qualquer tecla: ")
    limpar()
    principal()



def principal():

    while True:
        try:
            resposta = int(input("Escolha uma das opções abaixo:\n -> 1: escrever uma nota review\n -> 2: acessar suas reviews\n-> "))

            if resposta == 1:
                limpar()
                main1()

            elif resposta == 2:
                limpar()
                main2()

            else:
                limpar()
                print("Digite um valor válido")
                input("Digite qualquer valor para voltar: ")
                limpar()

        except:
            limpar()
            print("Digite um valor válido")
            input("Digite qualquer valor para voltar: ")
            limpar()
        
if __name__ == "__main__":
    principal()