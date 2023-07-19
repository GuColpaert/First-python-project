print("*************************************")
print("Bem-vindo ao jogo de adivinhação!!!\n")
print("*************************************")

numero_secreto = 42

# Aqui solicitamos a entrada de dados do usuário.
chute_str = input("Digite o seu número: ")

print("você digitou: ", chute_str)

# utilizamos essa variável para converter o input para inteiro para validar a condição.
chute_int = int(chute_str)

# se numero_secreto for igual a chute, então mostra mensagem de acerto - se não, mostra a mensagem de erro.
if numero_secreto == chute_int:
    print("Você acertou, parabens!!")
else:
    print("Você errou, tente novamente.")

print("Fim do jogo.")
