print("Seja bem vindo ao jogo de adivinhação!")

numero_secreto = 50

rodada = 1
numero_de_tentativas = 5

while rodada <= numero_de_tentativas:
    print("Você está na rodada {} de {}".format(rodada, numero_de_tentativas))
    chute_str = input("Digite o seu valor: ")
    chute = int(chute_str)
    print("Você digitou", chute)
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    acertou = chute == numero_secreto

    if maior:
        print("Tente um valor menor... entre 1 e 100")
    elif menor:
        print("Tente um valor maior!")

    elif acertou:
        print("Parabéns você acertou o número secreto!")
        break

    rodada = rodada + 1

print("Game Over...")
