import random
import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0

    def alimentar(self, quantidade):
        if 0 <= quantidade <= 100:
            self.fome = max(0, self.fome - (self.fome * (quantidade / 100)))
            print(f"{self.nome} foi alimentado e está menos faminto!")

    def brincar(self, quantidade):
        if 0 <= quantidade <= 100:
            self.tedio = max(0, self.tedio - (self.tedio * (quantidade / 100)))
            print(f"{self.nome} brincou bastante e está mais animado!")

    def getHumor(self):
        return ((self.fome + self.tedio) / 2)

    def vida(self):
        if self.fome > 99 or self.tedio > 99:
            self.saude = 0
            print("Seu bichinho morreu T_T")
        elif self.fome > 90 or self.tedio > 90:
            self.saude -= 70
            print("Estou morrendo... AAAAAAAAH")
        elif self.fome > 80 or self.tedio > 80:
            self.saude -= 50
        elif self.fome > 60 or self.tedio > 60:
            self.saude -= 30
        elif self.fome > 50 or self.tedio > 50:
            self.saude -= 10

        self.saude = max(0, self.saude)

    def tempoPassando(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5

class TamagoshiDepressivo(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.felicidade = 0
        self.motivacao = 50
        self.frases_tristes = ["quero me matar",
                               "tomara que eu morra hoje às 23:99",
                               "queria uma arma...",
                               "Você foi muito especial pra mim, adeus"]

    def ouvirMusgaTriste(self):
        print(f"{self.nome} está ouvindo musga triste :(")
        self.felicidade -= 1
        self.motivacao -= 5

    def fumar(self):
        print(f"{self.nome} acendeu o cigarro...")
        frase = random.choice(self.frases_tristes)
        print(f"💭 {frase}")
        self.felicidade += 1
        self.motivacao -= 5

    
    def terapia(self):
        print(f"{self.nome} está fazendo terapia...")
        self.motivacao += 20
        self.felicidade += 15
        self.saude += 10


class TamagoshiSigma(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.aura = 50
    
    def cara_de_sigma(self):
        print("🗿🧏🤫")
        self.aura += 40
    
    def old_money(self):
        print("Vestindo camisa social, calça de alfaiataria, sapato social e sueter")
        self.aura += 10
    
    def clear_man_CR7(self):
        print(f"{self.nome} usou clear man do Cristiano Ronaldo e agora está com o cabelo cheiroso e sedoso")
        self.aura += 30
    
    def chorar(self):
        print(f"{self.nome} não tankou a opressão da sociedade e chorou")
        self.aura -= 50
    
    def skincare(self):
        print(f"{self.nome} quis cuidar da pele facial...")
        self.aura -= 10


class TamagoshiRockeiro(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.felicidade = 50
        self.adrenalina = 50
    
    def tocar_guitarra(self):
        print(f"{self.nome} está tocando guitarra!! 🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘")
        self.felicidade += 20
        self.adrenalina += 30
    
    def show(self):
        print(f"{self.nome} realizou um sonho e foi no show do System of a Down")
        self.felicidade += 50
        self.adrenalina += 40
    
    def maquiagem(self):
        print(f"{self.nome} fez uma maquiagem dark 🤘")



def main():
    print("==Bem-Vindo ao Tamagoshi!==")
    nome = input("Digite o nome do seu pet virtual: ")
    print("\nEscolha a skin do seu pet: ")
    print("1 - Depressivo")
    print("2 - Sigma")
    print("3 - Rockeiro")

    try:
        escolha = int(input("Digite o número da sua opção: "))
    except ValueError:
        print("Entrada inválida! Criando um Tamagoshi comum...")
        escolha = 0

    if escolha == 1:
        pet = TamagoshiDepressivo(nome)
    elif escolha == 2:
        pet = TamagoshiSigma(nome)
    elif escolha == 3:
        pet = TamagoshiRockeiro(nome)
    else:
        print("Opção inválida, criando um tamagoshi comum...")
        pet = Tamagoshi(nome)
        
    while True:
        
        print("\nO que deseja fazer: ")
        print("1 - Alimentar")
        print("2 - Brincar")
        if isinstance (pet, TamagoshiDepressivo):
            print("3 - Ouvir musga triste")
            print("4 - Fumar")
            print("5 - Terapia")
        elif isinstance (pet, TamagoshiSigma):
            print("3 - Cara de Sigma")
            print("4 - Vestir old money")
            print("5 - Usar clear man do Cristiano Ronaldo")
            print("6 - Chorar")
            print("7 - Fazer skincare")
        elif isinstance (pet, TamagoshiRockeiro):
            print("3 - Tocar guitarra")
            print("4 - Ir ao show de rock")
            print("5 - Fazer maquiagem dark")
        print("0 - Sair do Jogo")


        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            continue

        if opcao == 0:
            print("Até a próxima!")
            limpar_tela()
            break

        if opcao == 1:
            pet.alimentar(50)
        elif opcao == 2:
            pet.brincar(30)

        elif isinstance (pet, TamagoshiDepressivo):
            if opcao == 3:
                pet.ouvirMusgaTriste()
            elif opcao == 4:
                pet.fumar()
            elif opcao == 5:
                pet.terapia()
        elif isinstance (pet, TamagoshiSigma):
            if opcao == 3:
                pet.cara_de_sigma()
            elif opcao == 4:
                pet.old_money()
            elif opcao == 5:
                pet.clear_man_CR7()
            elif opcao == 6:
                pet.chorar()
            elif opcao == 7:
                pet.skincare()
        elif isinstance (pet, TamagoshiRockeiro):
            if opcao == 3:
                pet.tocar_guitarra()
            elif opcao == 4:
                pet.show()
            elif opcao == 5:
                pet.maquiagem()
        else:
            print("Opção Inválida")

        
        pet.tempoPassando()



def jogar():
    while True:
        main()

        print("\nDeseja jogar novamente? (s/n)")
        resposta = input("> ").lower()
        if resposta != "s":
            print("Obrigado por jogar! Até a próxima!")
            break
        limpar_tela()


if __name__ == "__main__":
    jogar()