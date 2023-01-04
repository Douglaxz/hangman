#Declaração de variáveis
celulas = ['','','','','','','','','']
continuar = True
jogador = "X"
jogadaconcluida = False


#Função de criação e atualização do tabuleiro do jogo da velha
def tabuleiro():
    print ("| Escolha uma posição conforme o diagrama abaixo: |")
    print("\n")

    for y in range(0, 9, 3):
        for x in range(3):      
            print("|", end="")
            if(celulas[x+y]==''):
                print(" ", end="")
                print(int(x+y)+1, end="")
                print(" ", end="")
            else:
                print(" ", end="")
                print(" ", end="")
                print(" ", end="")
        print("|")

    print("\n")

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
        




while (continuar == True):
    print("\n")
    print("--------------------------------------------------------")
    print("BEM VINDO AO JOGO DA VELHA")
    print("--------------------------------------------------------")
    print("\n")
    tabuleiro()

    jogada = int(input("Jogador "+jogador+" faça sua jogada: "))
    print("\n")
    if (jogada > 0 and jogada < 10):
        if (celulas[jogada- 1])=="":
            celulas[jogada - 1] = jogador
            jogadaconcluida = True
        elif (celulas[jogada- 1])!="":
            print("Essa celula já está preenchida")    
            jogadaconcluida = False
            print("\n")
        print("\n")
        tabuleiro()
        print("\n")
    else:
        print("\n")
        tabuleiro()
        print("\n")
        print("Escolha um numero entre 1 e 9")
        print("\n")

    if(jogadaconcluida == True):
        if(jogador == "X"):
            jogador = "O"
        else:
            jogador = "X"

    
    






