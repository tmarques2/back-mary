from tamagoshi_pai import Tamagoshi
import os
import random

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

class TamagoshiDepressivo(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.felicidade = 0
        self.motivacao = 10
        self.frases_tristes = ["quero me matar",
                               "tomara que eu morra hoje às 23:99",
                               "queria uma arma...",
                               "Você foi muito especial pra mim, adeus"]

    def ouvirMusgaTriste(self):
        limpar_tela()
        print(f"{self.nome} está ouvindo musga triste :(\n")
        print("Felicidade -1 \nMotivação -5")
        self.felicidade -= 1
        self.motivacao -= 5
        self.saude = min(100, self.saude - 5)

    def fumar(self):
        limpar_tela()
        print(f"{self.nome} acendeu o cigarro...")
        frase = random.choice(self.frases_tristes)
        print(f"💭 {frase}\n")
        print("Felicidade +1 \nMotivação -5")
        self.felicidade += 1
        self.motivacao -= 5
        self.saude = min(100, self.saude - 20)

    
    def terapia(self):
        limpar_tela()
        print(f"{self.nome} está fazendo terapia...\n")
        print("Motivação +20 \nFelicidade +15 \nSaúde +10")
        self.motivacao += 20
        self.felicidade += 15
        self.saude = min(100, self.saude + 10)


class TamagoshiSigma(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.aura = 50
    
    def cara_de_sigma(self):
        limpar_tela()
        print("🗿🧏🤫\n")
        print("Aura +40")
        self.aura = min(100, self.aura + 40)
        if self.aura > 100:
            self.aura = 100
        if self.aura < 0:
            self.aura = 0
    
    def old_money(self):
        limpar_tela()
        print("Vestindo camisa social, calça de alfaiataria, sapato social e sueter\n")
        print("Aura +10")
        self.aura = min(100, self.aura+ 10)
        if self.aura > 100:
            self.aura = 100
        if self.aura < 0:
            self.aura = 0
    
    def clear_man_CR7(self):
        limpar_tela()
        print(f"{self.nome} usou clear man do Cristiano Ronaldo e agora está com o cabelo cheiroso e sedoso\n")
        print("Aura +30")
        self.aura = min(100, self.aura + 30)
        if self.aura > 100:
            self.aura = 100
        if self.aura < 0:
            self.aura = 0
    
    def chorar(self):
        limpar_tela()
        print(f"{self.nome} não tankou a opressão da sociedade e chorou\n")
        print("Aura -40")
        self.aura = min(100, self.aura - 40)
        self.saude = min(100, self.saude -5)
        if self.aura > 100:
            self.aura = 100
        if self.aura < 0:
            self.aura = 0
    
    def skincare(self):
        limpar_tela()
        print(f"{self.nome} quis cuidar da pele facial...")
        print("Aura -10")
        self.aura = min(100, self.aura - 15)
        self.saude = min(100, self.saude + 5)
        if self.aura > 100:
            self.aura = 100
        if self.aura < 0:
            self.aura = 0


class TamagoshiRockeiro(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.felicidade = 50
        self.adrenalina = 50
    
    def tocar_guitarra(self):
        limpar_tela()
        print(f"{self.nome} está tocando guitarra!! 🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘\n")
        print("Felicidade +20 \nAdrenalina +30")
        self.felicidade = min(100, self.felicidade + 20)
        self.adrenalina += 30
        if self.adrenalina > 100:
            self.adrenalina = 100
        if self.adrenalina< 0:
            self.adrenalina = 0

        if self.felicidade > 100:
            self.felicidade = 100
        if self.felicidade< 0:
            self.felicidade = 0
    
    def show(self):
        limpar_tela()
        print(f"{self.nome} realizou um sonho e foi no show do System of a Down\n")
        print("Felicidade +50 \nAdrenalina +40")
        self.felicidade = min(100, self.felicidade + 50)
        self.adrenalina += 40
        self.saude = min(100, self.saude - 5)
        if self.adrenalina > 100:
            self.adrenalina = 100
        if self.adrenalina< 0:
            self.adrenalina = 0

        if self.felicidade > 100:
            self.felicidade = 100
        if self.felicidade< 0:
            self.felicidade = 0
    
    def maquiagem(self):
        limpar_tela()
        print(f"{self.nome} fez uma maquiagem dark 🤘")
        print("Felicidade +10")
        self.felicidade = min(100, self.felicidade + 10)
        self.saude = min(100, self.saude - 5)
        if self.adrenalina > 100:
            self.adrenalina = 100
        if self.adrenalina< 0:
            self.adrenalina = 0
        
        if self.felicidade > 100:
            self.felicidade = 100
        if self.felicidade< 0:
            self.felicidade = 0
    
    def ouvir_funk(self):
        limpar_tela()
        print(f"\n{self.nome} foi obrigado a ouvir poluição sonora")
        self.felicidade = min(100, self.felicidade - 30)
        if self.felicidade > 100:
            self.felicidade = 100
        if self.felicidade< 0:
            self.felicidade = 0