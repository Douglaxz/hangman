import random

#Declaração de váriáveis

palavras = ['abacate','maca', 'tomate','laranja','tangerina','jaca','amendoim']


#desenhar forca
def desenharForca():
    print("-------¬")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("\n")


#funcao forca
def jogoforca():
    erros = 0
    #sortear palavras   
    sorteio = (random.randint(0, len(palavras)))
    palavra = palavras[sorteio-1]    
    letrasCorretas = []    
    letrasErradas = []    

    desenharForca()
    

    #desenhar os espaços da palavra em um vetor vazio, que irá receber as letras acertadas
    for p in palavra:
        letrasCorretas.append("_")

    for letra in letrasCorretas:
        print(letra + " ", end="")
    
    print("\n")
    #pedir pro usuario uma letra
    while(erros < 5):
        letra = (input("Digite uma letra: "))
        print("\n")

        contador = 0
        
        #verificar se a letra consta na palavra
        
        for p in palavra:
            acerto = 0
            print(contador)
            print(p)
            print(letra)
            print("------")
            if(p == letra):
                letrasCorretas[contador] = letra
                acerto = 1
            contador = contador + 1
            
        if(acerto==0):
            letrasErradas.append(letra)
            erros =+1
        
        print(palavra)
        print(letrasCorretas)
        print(letrasErradas)
        print(erros)


jogoforca()