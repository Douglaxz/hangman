#import de dependencias
import random #para poder utilizar a função random
import sys #para utilizar args

#estrutura de cores

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

def jogoAdivinhacao():
    sorteio = (random.randint(1, 50))
    continuar = True
    rodada = 1
    while(continuar == True):
        print("\n")
        for i in range(50):
            print(i+1, end="")
            print(" ", end="")
        
        print("\n")
        #print(BOLD + RED + "ERROR!" + RESET + "Something went wrong...")
        print(sorteio)
        print("------------------- RODADA "+str(rodada)+"-------------------------------")
        palpite = int(input("Digite um número entre 1 e 50: "))
        if(palpite == sorteio):
            print(GREEN+ "PARABÉNS! " + RESET + "Você acertou o número...")
        else:
            print(RED+ "ERROU! " + RESET + "Tente novamente")
            if(palpite < sorteio):
                print(BLUE+ "DICA " + RESET + "O número é maior que "+ str(palpite))
            else:
                print(BLUE+ "DICA " + RESET + "O número é menor que "+ str(palpite))
        print("--------------------------------------------------------")
        print("\n")

        resposta = input("Deseja tentar adivinhar novamente: 'S/N'")
        resposta = resposta.upper()
        if(resposta=='N'):
            exit()
        print("--------------------------------------------------------")
        rodada = rodada + 1





#chamada da função principal, diretamente do arquivo
chamada = sys.argv[0]
if(chamada =="adivinhacao.py"):
    jogoAdivinhacao()