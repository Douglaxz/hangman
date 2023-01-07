#import de dependencias
import random #para poder utilizar a função random
import sys #para utilizar args

#Declaração de váriáveis e vetores
continuar = True
palavras = []

#Carregando arquivo txt  com palavras

palavras = open("palavrasforca.txt","r", encoding="utf-8").read().splitlines()

#colocando todas as letras em maiusculo
for palavra in palavras:
    palavraMaiuscula = palavra.upper()
    palavras.append(palavraMaiuscula)
    palavras.remove(palavra)

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
        print("|     | |")
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
    print(palavra)
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
            invalido = True
            while (invalido==True):
           
                invalido=False

                letra = (input("Digite uma letra: "))
                if(len(letra)!=1):
                    print("Você digitou mais do que 1 letra")
                    invalido=True                    
                    

                if(letra.isalpha()==False):
                    print("Você digitou um caractere invalido")
                    invalido=True
            

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



#chamada da função principal, diretamente do arquivo
chamada = sys.argv[0]
if(chamada =="forca.py"):
    jogoforca()