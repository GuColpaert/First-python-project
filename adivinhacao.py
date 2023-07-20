print("***********************************")
print("Bem-vindo ao jogo de adivinhação!!!")
print("***********************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1

# Nosso laço de repetição para o jogo continuar
# cod antigo >  while(total_tentativas > 0):
while rodada <= total_tentativas:
    print("\nTentativa {} de {}".format(rodada, total_tentativas))  # String interpolation
    chute_str = input("Digite o seu número: ")  # Aqui solicitamos a entrada de dados do usuário.
    print("\nvocê digitou: ", chute_str)

    # utilizamos essa variável para converter o input para inteiro para validar a condição.
    chute_int = int(chute_str)

    acertou = chute_int == numero_secreto
    maior = chute_int > numero_secreto
    menor = chute_int < numero_secreto

    # se numero_secreto for igual a chute, então mostra mensagem de acerto - se não, mostra a mensagem de erro.
    if numero_secreto == chute_int:
        print("Você acertou!! parabens!!")
    else:
        if(maior):
            print("Você errou!! numero maior que o correto.")
        elif(menor):
            print("Você errou!! numero menor que o correto.")

    # cod antigo >  total_tentativas -= 1
    rodada += 1

print("Fim do jogo.")
