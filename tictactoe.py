#Declaração de variáveis
celulas = ['','','','','','','','','']
continuar = True
jogador = "X"
jogadaconcluida = False
rodada = 1


#Função reiniciar o jogo
def reiniciar():
    global jogador
    global celulas
    global continuar
    global jogadaconcluida
    global rodada
    celulas = ['','','','','','','','','']
    continuar = True
    jogador = "X"
    jogadaconcluida = False
    rodada = 1




#Função para verificar se houve vitoria de algum jogador
def vitoria(jogador,celulas):
    vitoria = 0
    
    def celulasPreenchidas(x,y,z,jogador):
        if(celulas[x]==jogador and celulas[y]==jogador and celulas[z]==jogador):
            return(1)
        else:
            return(0)


    #condições de vitoria do jogador    

    #vitoria em linha
    # 1 2 3
    if(vitoria == 0):
        vitoria = celulasPreenchidas(0,1,2,jogador)
    # 4 5 6
    if(vitoria == 0):
        vitoria = celulasPreenchidas(3,4,5,jogador)       
    # 7 8 9
    if(vitoria == 0):
        vitoria = celulasPreenchidas(6,7,8,jogador)    
    
    #vitoria em transversal
    # 1 5 9
    if(vitoria == 0):
        vitoria = celulasPreenchidas(0,4,8,jogador)    
    # 3 5 7
    if(vitoria == 0):
        vitoria = celulasPreenchidas(2,4,6,jogador)    

    #vitoria em coluna
    # 1 4 7
    if(vitoria == 0):
        vitoria = celulasPreenchidas(0,3,6,jogador)    
    
    # 2 5 8
    if(vitoria == 0):
        vitoria = celulasPreenchidas(1,4,7,jogador)        
    # 3 6 9
    if(vitoria == 0):
        vitoria = celulasPreenchidas(2,5,8,jogador)    

    if(vitoria==1):
        print("JOGADOR "+jogador+" VENCEU")
        print("--------------------------------------------------------")
        resposta = input("Deseja jogar novamente: 'SIM/NÃO'")
        if(resposta=='não'):
            exit()
        else:
            reiniciar()
            jogodavelha()



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

#Cabeçalho do jogo    
print("\n")
print("--------------------------------------------------------")
print("BEM VINDO AO JOGO DA VELHA")
print("--------------------------------------------------------")
print("\n")

#Função do jogo da velha
def jogodavelha():
    global rodada
    global jogador
    global celulas
    while (rodada < 10):
        print("\n")
        print("--------------------------------------------------------")
        print("RODADA "+ str(rodada))
        print("--------------------------------------------------------")
        vitoria(jogador,celulas)
        tabuleiro()
        
        jogada = int(input("Jogador '"+jogador+"' faça sua jogada: "))
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

        #função para alterancia de jogadores
        if(jogadaconcluida == True):
            if(jogador == "X"):
                jogador = "O"
            else:
                jogador = "X"
        rodada = int(rodada) + 1

#chamando a função
jogodavelha()
    
    






