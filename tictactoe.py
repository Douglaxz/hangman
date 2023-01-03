import random

celulas = ['','','','','','','','','']

def tabuleiro():
    
    for y in range(0, 9, 3):
        for x in range(3):      
            print("|", end="")
            if(celulas[x+y]!=''):
                print(" ", end="")
                print(celulas[x+y], end="")
                print(" ", end="")
            else:
                print(" ", end="")
                print(" ", end="")
                print(" ", end="")
        print("|")
        





print("BEM VINDO AO JOGO DA VELHA")
print("\n")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")
print("\n")
jogada = input("Jogador X, escolha uma posição conforme o diagrama abaixo:")
print("\n")
if (int(jogada) > 0 and int(jogada) < 10):
    celulas[int(jogada )- 1] = "X"
    tabuleiro()
else:
    print("Escolha um numero entre 1 e 9")






