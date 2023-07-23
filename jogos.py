import forca
import adivinhacao

print("*****************************")
print("****Escolha o seu jogo!!!****")
print("*****************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("\nForca")
    forca.jogar() # especificamos o modulo do import e a função do mesmo para chama-lo
elif (jogo == 2):
    print("\nAdivinhação")
    adivinhacao.jogar()

