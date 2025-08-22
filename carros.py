class Veiculo:
    def __init__(self, marca, modelo, ano_fab, cor, qtd_porta):
        self.marca = marca
        self.modelo = modelo
        self.ano_fab = ano_fab
        self.cor = cor
        self.qtd_porta = qtd_porta
        self.ligado = False

    def andar(self):
        print(f"{self.modelo} andando")

    def frear(self):
        print(f"{self.modelo} freiando")

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.modelo} ligado")
        else:
            print(f"{self.modelo} já está ligado")

    def imprimir(self):
        print(f"O veículo tem as seguintes características: \n"
              f"Marca: {self.marca}\n"
              f"Modelo: {self.modelo}\n"
              f"Ano de fabricação: {self.ano_fab}\n"
              f"Cor: {self.cor}\n"
              f"{self.qtd_porta} portas\n")


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano_fab, cor, qtd_rodas):
        # Ajuste dos parâmetros na chamada do super()
        super().__init__(marca, modelo, ano_fab, cor, qtd_porta=0)  # Moto não precisa de qtd_porta
        self.qtd_rodas = qtd_rodas

    def empinar(self):
        print("Empinando a moto!")

    def fazer_barulho(self):
        print("RAM DAM DAM DAM RAM DAM DAM DAM DAM")

    def imprimir(self):
        super().imprimir()
        print(f"Quantidade de rodas: {self.qtd_rodas}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano_fab, cor, qtd_rodas):
        # Ajuste dos parâmetros na chamada do super()
        super().__init__(marca, modelo, ano_fab, cor, qtd_porta=4)  # Carro tem 4 portas por padrão
        self.qtd_rodas = qtd_rodas

    def abrir_porta_malas(self):
        print("Porta-malas aberto.")

    def imprimir(self):
        super().imprimir()
        print(f"Quantidade de rodas: {self.qtd_rodas}")

    def tocar_musica(self):
        print("Tocando System of a Down")


class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano_fab, cor, qtd_rodas):
        # Ajuste dos parâmetros na chamada do super()
        super().__init__(marca, modelo, ano_fab, cor, qtd_porta=2)  # Caminhão tem 2 portas (por padrão)
        self.qtd_rodas = qtd_rodas

    def dar_re(self):
        print("Dando ré: PI PI PI")

    def carregar_carga(self):
        print("Carregando carga do caminhão")


# Função para mostrar as funcionalidades do carro
def carro():
    carro = Carro("Toyota", "Corolla", 2008, "Azul", 4)
    carro.imprimir()
    carro.abrir_porta_malas()
    carro.tocar_musica()


# Função para mostrar as funcionalidades da moto
def moto():
    moto = Moto("Honda", "Ninja", 2022, "Verde", 2)
    moto.imprimir()
    moto.empinar()
    moto.fazer_barulho()


# Função para mostrar as funcionalidades do caminhão
def caminhao():
    caminhao = Caminhao("Volvo", "FH", 2020, "Preto", 18)
    caminhao.imprimir()
    caminhao.dar_re()
    caminhao.carregar_carga()


# Chamada das funções para testar
carro()
print("\n")
moto()
print("\n")
caminhao()
