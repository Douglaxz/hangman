import random

#Declaração de váriáveis
erros = 0
palavras = ['abacate','maca', 'tomate','laranja','tangerina','jaca','amendoim']


#desenhar forca
def desenharForca():
    print("-------¬")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")


#funcao forca
def jogoforca():
          
    
    #sortear palavras   
    sorteio = (random.randint(0, len(palavras)))
    palavra = palavras[sorteio-1]    
    letras = []    

    desenharForca()
    

    #desenhar os espaços da palavra em um vetor vazio, que irá receber as letras acertadas
    for p in palavra:
        letras.append("_")

    print(letras)
    
    print("\n")
    #pedir pro usuario uma letra
    #letra = (input("Digite uma letra? "))

    print("\n")

    #verificar se a letra consta na palavra
    #for p in palavra:
    #    if(p == letra):
    #        print(" "+p+" ", end="")
    #    else:
    #        print(" _ ", end="")
    
    print("\n")


    print("\n")

    
    
    print(palavra)


jogoforca()