import tictactoe
import forca

#chamando a função
print("\n")
print("----------SELECIONE O JOGO QUE VOCÊ QUER JOGAR----------")
print("( 1 ) Jogo da velha")
print("( 2 ) Forca")
jogo = int(input("Qual a sua opção? "))
print("\n")
if(jogo==1):
    tictactoe.jogodavelha()
else:
    forca.jogoforca()