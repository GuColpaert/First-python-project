import random


def jogar():  # estamos criando uma função

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)  # imprime apenas o underscore da quantidade de palavras

    enforcou = False
    acertou = False
    tentativas = 0

    #  enquanto (True)
    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            tentativas += 1
            desenha_forca(tentativas)


        enforcou = tentativas == 7  # true
        acertou = "_" not in letras_acertadas  # true
        print(letras_acertadas)

    #  Condição de ganhar ou perder
    if(acertou):
        mensagem_ganhador()
    else:
        mensagem_perdedor(palavra_secreta)

    print("Fim do jogo!!!")


def imprime_mensagem_abertura():
    print("*****************************")
    print("Bem-vindo ao jogo de forca!!!")
    print("*****************************")


def carrega_palavra_secreta():
    with open("arquivo.txt", "r", encoding="utf-8") as arquivo:  # abre o arquivo
        palavras = []  # lista para armazenar os dados do arquivo

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))  # Pega um valor aleatorio com base nas palavras da list
    palavra_secreta = palavras[numero].upper()  # Procura o numero da casa da palavra sorteada
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    lista = ["_" for letra in palavra]  # cada letra em palavra secreta vai adicionar um "_"
    return lista


def pede_chute():
    chute = input("Qual letra?? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, palavra, letras):
    index = 0
    for letra in palavra:
        if chute == letra:
            letras[index] = letra
        index += 1


def mensagem_perdedor(palavra):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def mensagem_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()
