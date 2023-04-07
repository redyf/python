import random


def jogar():
    print("*****************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*****************************")

    numero_secreto = round(random.randrange(1, 101))  # Valor aleátorio entre 1/100
    total_de_tentativas = 0
    pontos = 1000

    print("Níveis do jogo ")
    print("(1) Fácil (2) Médio (3) Difícil")

    try:
        nivel = int(input("Escolha a dificuldade: "))
    except EOFError:
        print("EOFError: The input has reached the end of a file.")
        return

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou:", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou!")
            break
        else:
            if maior:
                print("O chute foi mais alto que o número secreto")
            elif menor:
                print("O chute foi menor que o número secreto")
                pontos_perdidos = abs(numero_secreto - chute) * 3
                pontos = round(pontos - pontos_perdidos)
    print(
        f"Fim do jogo, o número secreto era: {numero_secreto}. Você fez {pontos} pontos"
    )


if __name__ == "__main__":
    jogar()
