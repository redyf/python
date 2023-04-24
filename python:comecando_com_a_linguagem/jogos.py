import forca
import adivinhacao


def escolhe_jogo():
    print("Escolha o seu jogo!")

    print("(1) Forca (2) Adivinhação")
    try:
        jogo = int(input("Qual a sua escolha? "))
    except EOFError:
        pass
    if jogo == 1:
        print("Jogando forca")
        forca.jogar()

    elif jogo == 2:
        print("Jogando adivinhação")
        adivinhacao.jogar()


if __name__ == "__main__":
    escolhe_jogo()
