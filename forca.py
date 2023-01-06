import random

#Declaração de váriáveis

palavras = ['abacate','maca', 'tomate','laranja','tangerina','jaca','amendoim']
continuar = True

#desenhar forca
def desenharForca(erros):
    if(erros==0):
        print("-------¬")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")

    if(erros==1):
        print("-------¬")
        print("|      O")
        print("|")
        print("|")
        print("|")
        print("|")

    if(erros==2):
        print("-------¬")
        print("|      O")
        print("|      |")
        print("|")
        print("|")
        print("|")

    if(erros==3):
        print("-------¬")
        print("|      O")
        print("|      |")
        print("|     |")
        print("|")
        print("|")

    if(erros==4):
        print("-------¬")
        print("|      O")
        print("|      |")
        print("|     | |'")
        print("|")
        print("|")

    if(erros==5):
        print("-------¬")
        print("|      O")
        print("|      |--")
        print("|     | |'")
        print("|")
        print("|")

    if(erros==6):
        print("-------¬")
        print("|      O")
        print("|    --|--")
        print("|     | |'")
        print("|")
        print("|")  
    
    
    print("\n")


def jogarNovamente():
    resposta = ""
    while(resposta==""):
        resposta = input("Deseja jogar novamente: 'S/N'")
        resposta = resposta.upper()
        if(resposta=='N'):
            exit()
        elif (resposta=='S'):
            jogoforca()
        else:
            print("Resposta inválida")
            resposta = ""
    print("--------------------------------------------------------")

def finalDeJogo(msg, palavra):
    print("|----------------- "+msg.upper()+" ! -----------------|")
    print("A PALAVRA SECRETA ERA: "+ palavra.upper())
    print("\n")


#funcao forca
def jogoforca():
    erros = 0
    #sortear palavras   
    sorteio = (random.randint(0, len(palavras)))
    palavra = palavras[sorteio-1]
    letrasCorretas = []    
    letrasErradas = []    
    
    #desenhar os espaços da palavra em um vetor vazio, que irá receber as letras acertadas
    for p in palavra:
        letrasCorretas.append("_")

    for letra in letrasCorretas:
        print(letra + " ", end="")
    
    print("\n")
    
    while(continuar == True):
        while(erros < 6):
            #chamada da função de desenho da forca
            desenharForca(erros)

            #criação do placar
            print("|----------------- PLACAR -----------------|")
            print("|    ACERTOS     | ", end="")
            for letra in letrasCorretas:
                print(letra, end="")
                print(" ", end="")
            print("\n")
            print("| LETRAS ERRADAS | ", end="")
            for letra in letrasErradas:
                print(letra, end="")
                print(" ", end="")        
            print("\n")        
            print("|      ERROS     | ", end="")
            print(erros)
            print("\n")     

            #pedir pro usuario uma letra
            letra = (input("Digite uma letra: "))
            

            #verificar se a letra consta na palavra
            contador = 0
            if(letra in palavra):
                for p in palavra:
                    if(p == letra):
                        letrasCorretas[contador] = letra.upper()
                    contador = contador + 1
            else:
                if(letra not in letrasErradas):
                    letrasErradas.append(letra.upper())
                erros = erros + 1
            print("\n")
            
            #verificar se houve vitoria
            novapalavra = ''.join(letrasCorretas)
            
            if(novapalavra == palavra.upper()):
                finalDeJogo("ganhou", palavra)
                jogarNovamente()



            #verificar se houve derrota
            if(erros==6):
                desenharForca(erros)
                finalDeJogo("perdeu", palavra)
                jogarNovamente()



jogoforca()