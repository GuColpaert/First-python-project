import random


def jogar():
    print("***********************************")
    print("Bem-vindo ao jogo de adivinhação!!!")
    print("***********************************")

    numero_secreto = random.randrange(1, 101) # imprime numero aleatório de 1 a 100
    total_tentativas = 0
    pontos = 1000

    print("Qual o nivel da dificuldade???", numero_secreto)
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nivel: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    # print(numero_secreto)

    # Nosso laço de repetição para o jogo continuar
    # cod antigo >  while(total_tentativas > 0):
    # cod antigo > while rodada <= total_tentativas:  > funcional mas trocado pelo for
    for rodada in range(1, total_tentativas + 1):
        print("\nTentativa {} de {}".format(rodada, total_tentativas))  # String interpolation
        chute_str = input("Digite o seu número entre 1 e 100: ")  # Aqui solicitamos a entrada de dados do usuário.
        print("\nvocê digitou: ", chute_str)

        # utilizamos essa variável para converter o input para inteiro para validar a condição.
        chute_int = int(chute_str)

        if(chute_int < 1 or chute_int > 100):
            print("Você deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute_int == numero_secreto
        maior = chute_int > numero_secreto
        menor = chute_int < numero_secreto

        # se numero_secreto for igual a chute, então mostra mensagem de acerto - se não, mostra a mensagem de erro.
        if acertou:
            print("Você acertou e fez {} pontos!!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou!! numero maior que o correto.")
            elif(menor):
                print("Você errou!! numero menor que o correto.")

            pontos_perdidos = abs(numero_secreto - chute_int)
            pontos = pontos - pontos_perdidos

        # cod antigo >  total_tentativas -= 1
        # cod antigo > rodada += 1

    print("Fim do jogo.")


if(__name__ == "__main__"):  # se o nome do arquivo for igual a principal roda o código.
    jogar()
