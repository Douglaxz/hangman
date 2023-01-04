import random

#Declaração de variáveis
celulas = ['','','','','','','','','']
continuar = True
jogador = "X"
jogadaconcluida = False
rodada = 1
placarX = 0
placarY = 0


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
    global placarY
    global placarX
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

    # se houve alguma condição de vitória, irá aparecer a mensagem
    if(vitoria==1):
        resposta = ""
        print("JOGADOR '"+jogador+"' VENCEU")
        if(jogador=="X"):
            placarX = int(placarX + 1)
        else:
            placarY = int(placarY + 1)

        print("-------------------------PLACAR------------------------")
        print("          JOGADOR 'X'", end="")
        print("         |", end="")
        print("          JOGADOR 'O'")
        print("--------------------------------------------------------")
        print("              "+str(placarX),end="")
        print("               |", end="")
        print("              "+str(placarY))            
        print("--------------------------------------------------------")
        while(resposta==""):
            resposta = input("Deseja jogar novamente: 'S/N'")
            resposta = resposta.upper()
            if(resposta=='N'):
                exit()
            elif (resposta=='S'):
                reiniciar()
                jogodavelha()
            else:
                print("Resposta inválida")
                resposta = ""
        print("--------------------------------------------------------")


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
    print("-------------------------------------------------")

#Cabeçalho do jogo    
print("\n")
print("-----------BEM VINDO AO JOGO DA VELHA-----------")
print("\n")

#Função do jogo da velha
def jogodavelha():
    global rodada
    global jogador
    global celulas
    while (rodada < 10):
        
        print("-------------------RODADA "+ str(rodada)+"---------------------")
        
        tabuleiro()
        
        jogada = int(input("Jogador '"+jogador+"' faça sua jogada: "))
        print("\n")
        if (jogada > 0 and jogada < 10):
            if (celulas[jogada- 1])=="":
                celulas[jogada - 1] = jogador
                jogadaconcluida = True
                rodada = int(rodada) + 1
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

        #verificação de vitória
        vitoria(jogador,celulas)

        #função para alterancia de jogadores
        if(jogadaconcluida == True):
            if(jogador == "X"):
                jogador = "O"
            else:
                jogador = "X"
        
#funcao forca
def jogoforca():
    erros = 0
    print("forca")
    #carregar palavras
    palavras = ['abacate','maca', 'tomate','laranja','tangerina','jaca','amendoim']
    
    #sortear palavras
    sorteio = (random.randint(0, len(palavras)))
    palavra = palavras[sorteio-1]    
    letras = []

    #desenhar forca
    print("-------¬")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")

    #desenhar os espaços da palavra
    for p in palavra:
        print(" _ ", end="")
    
    letra = int(input("Digite uma letra? "))


    print("\n")

    #pedir pro usuario uma letra
    #verificar se a letra consta na palavra
    print(palavra)


#chamando a função
print("\n")
print("----------SELECIONE O JOGO QUE VOCÊ QUER JOGAR----------")
print("( 1 ) Jogo da velha")
print("( 2 ) Forca")
jogo = int(input("Qual a sua opção? "))
print("\n")
if(jogo==1):
    jogodavelha()
else:
    jogoforca()

    
    






