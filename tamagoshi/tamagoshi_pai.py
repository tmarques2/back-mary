class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.saude = 100
        self.idade = 0
        self.tedio = 0
        self.energia = 100
        self.dormindo = False
        self.vivo = True

    def verificar_vida(self):
        if self.saude <= 0:
            self.saude = 0
            self.vivo = False
            print(f"\n{self.nome} morreu... 😢")
            return False
        return True


    def alimentar(self, quantidade):
        self.fome -= quantidade
        self.fome = max(0, min(100, self.fome))
        self.saude = max(0, min(100, self.saude + 5))
        print(f"{self.nome} foi alimentado e está menos faminto!")


    def brincar(self, quantidade):
        self.tedio -= quantidade
        self.energia -= quantidade // 2
        self.tedio = max(0, min(100, self.tedio))
        self.energia = max(0, min(100, self.energia))
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
        if not self.vivo:
            return
        self.fome += 5
        self.tedio += 5
        self.energia -= 5
        self.saude -= 2
        self.fome = min(100, self.fome)
        self.tedio = min(100, self.tedio)
        self.energia = max(0, self.energia)
        self.idade += 0.1
        self.verificar_vida()


    def status(self):
        print("\n===== STATUS DO PET =====")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade:.1f}")
        print(f"Saúde: {self.saude}")
        print(f"Fome: {self.fome}")
        print(f"Tédio: {self.tedio}")
        if hasattr(self, "felicidade"):
            print(f"Felicidade: {self.felicidade}")
        if hasattr(self, "motivacao"):
            print(f"Motivação: {self.motivacao}")
        if hasattr(self, "aura"):
            print(f"Aura: {self.aura}")
        if hasattr(self, "adrenalina"):
            print(f"Adrenalina: {self.adrenalina}")
        print("=========================\n")

    def dormir(self):
        self.dormindo = True
        print(f"{self.nome} foi de dormes.")
 
    def acordar(self):
        self.dormindo = False
        print(f"{self.nome} Acordouuuu")
        self.energia = 100
        self.saude = min(100, self.saude + 5)
 
    def salvar_estado(self):
        tipo = type(self).__name__
        with open("estado_tamagoshi.txt", "w") as f:
            f.write(f"{tipo};{self.nome};{self.fome};{self.saude};{self.idade};{self.tedio};{self.energia};{self.dormindo}\n")#pra salvar o estado em txt
   
    @classmethod
    def carregar_estado(cls):
        try:
            with open("estado_tamagoshi.txt", "r") as f:
                dados = f.readline().strip().split(";")
                tipo = dados[0]
                nome = dados[1]
                fome = float(dados[2])
                saude = int(dados[3])
                idade = float(dados[4])
                tedio = float(dados[5])
                energia = int(dados[6])
                dormindo = dados[7] == "True"

                if tipo == "TamagoshiDepressivo":
                    from tamagoshi_filho import TamagoshiDepressivo
                    bicho = TamagoshiDepressivo(nome)
                elif tipo == "TamagoshiSigma":
                    from tamagoshi_filho import TamagoshiSigma
                    bicho = TamagoshiSigma(nome)
                elif tipo == "TamagoshiRockeiro":
                    from tamagoshi_filho import TamagoshiRockeiro
                    bicho = TamagoshiRockeiro(nome)
                else:
                    return None

                bicho.fome = fome
                bicho.saude = saude
                bicho.idade = idade
                bicho.tedio = tedio
                bicho.energia = energia
                bicho.dormindo = dormindo

                if dormindo:
                    bicho.acordar()

                return bicho
        except FileNotFoundError:
            return None