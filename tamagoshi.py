import random
class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0

    def alimentar(self, quantidade):
        if (quantidade >=0) and (quantidade <=100):
            self.fome -= self.fome * (quantidade / 100)
            print(f"{self.nome} foi alimentado e está menos faminto!")

    def brincar(self, quantidade):
        if (quantidade >=0) and (quantidade<=100):
            self.tedio -= self.tedio * (quantidade / 100)
            print(f"{self.nome} brincou bastante e está mais animado!")

    def getHumor(self):
        return ((self.fome + self.tedio) / 2)

    def vida(self):
        if (self.fome > 50 and self.fome <= 60) or (self.tedio > 50 and self.tedio <=60):
            self.saude -= 10
        elif (self.fome > 60 and self.fome <= 80) or (self.tedio > 60 and self.tedio <=80):
            self.saude -= 30
        elif (self.fome > 80 and self.fome <= 90) or (self.tedio > 80 and self.tedio <=90):
            self.saude -= 50
        elif (self.fome > 90) or (self.tedio > 90):
            self.saude -= 70
            print("Estou morrendo... AAAAAAAAH")
        elif (self.fome > 99) or (self.tedio > 99):
            self.saude = 0
            print("Seu bichinho morreu T_T")

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
