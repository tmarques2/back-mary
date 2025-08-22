from tamagoshi_pai import Tamagoshi
from tamagoshi_filho import TamagoshiDepressivo, TamagoshiSigma, TamagoshiRockeiro

import os
import time


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def esperar():
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(1)
    print("\n")


def escolher_bicho():
    print("==Bem-Vindo ao Tamagoshi!==")
    nome = input("Escolha um nome para o seu pet virtual: ")
    print("\nEscolha a skin do seu pet: ")
    print("[1] - Depressivo")
    print("[2] - Sigma")
    print("[3] - Rockeiro")

    try:
        escolha = int(input("Digite o número da sua opção: "))
    except ValueError:
        escolha = 0

    if escolha == 1:
        classe_escolhida = TamagoshiDepressivo
    elif escolha == 2:
        classe_escolhida = TamagoshiSigma
    elif escolha == 3:
        classe_escolhida = TamagoshiRockeiro
    else:
        classe_escolhida = Tamagoshi

    return nome, classe_escolhida


def loop_jogo(pet):
    while True:
        if not pet.vivo:
            break

        print(f"\nVocê escolheu o {type(pet).__name__}")
        pet.status()
        print("\nO que deseja fazer: ")
        print("1 - Alimentar")
        print("2 - Brincar")

        if isinstance(pet, TamagoshiDepressivo):
            print("3 - Ouvir musga triste")
            print("4 - Fumar")
            print("5 - Terapia")
        elif isinstance(pet, TamagoshiSigma):
            print("3 - Cara de Sigma")
            print("4 - Vestir old money")
            print("5 - Usar clear man do Cristiano Ronaldo")
            print("6 - Chorar")
            print("7 - Fazer skincare")
        elif isinstance(pet, TamagoshiRockeiro):
            print("3 - Tocar guitarra")
            print("4 - Ir ao show de rock")
            print("5 - Fazer maquiagem dark")
            print("6 - Ouvir funk")

        print("0 - Sair do Jogo")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            continue

        if opcao == 0:
            pet.salvar_estado()
            print("Até a próxima!")
            limpar_tela()
            break

        if opcao == 1:
            esperar()
            pet.alimentar(10)
        elif opcao == 2:
            esperar()
            pet.brincar(20)
        elif isinstance(pet, TamagoshiDepressivo):
            if opcao == 3:
                esperar()
                pet.ouvirMusgaTriste()
            elif opcao == 4:
                esperar()
                pet.fumar()
            elif opcao == 5:
                esperar()
                pet.terapia()
        elif isinstance(pet, TamagoshiSigma):
            if opcao == 3:
                esperar()
                pet.cara_de_sigma()
            elif opcao == 4:
                esperar()
                pet.old_money()
            elif opcao == 5:
                esperar()
                pet.clear_man_CR7()
            elif opcao == 6:
                esperar()
                pet.chorar()
            elif opcao == 7:
                esperar()
                pet.skincare()
        elif isinstance(pet, TamagoshiRockeiro):
            if opcao == 3:
                esperar()
                pet.tocar_guitarra()
            elif opcao == 4:
                esperar()
                pet.show()
            elif opcao == 5:
                esperar()
                pet.maquiagem()
            elif opcao == 6:
                esperar()
                pet.ouvir_funk()
        else:
            print("Opção Inválida")

        pet.tempoPassando()


def main():
    while True:
        print("\nDeseja continuar com o bichinho anterior? (s/n)")
        resposta = input("> ").lower()
        if resposta == "s":
            pet = Tamagoshi.carregar_estado()
            if pet is None:
                print("Nenhum bichinho salvo encontrado. Criando novo.")
                nome, classe_escolhida = escolher_bicho()
                pet = classe_escolhida(nome)
        else:
            nome, classe_escolhida = escolher_bicho()
            pet = classe_escolhida(nome)

        limpar_tela()
        loop_jogo(pet)

        print("\nDeseja jogar novamente? (s/n)")
        if input("> ").lower() != "s":
            print("Obrigado por jogar! Até a próxima!")
            break
        limpar_tela()


if __name__ == "__main__":
    main()
