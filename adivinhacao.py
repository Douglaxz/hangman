# Ficha técnica
#Desenvolvedor : Douglas Amaral
#Contato: douglaxz@hotmail.com
#GitHub: https://github.com/Douglaxz/hangman
#Linguagem: Python
#Descrição do projeto: Jogo no estilo adivinhação de número, com dicas

#Instruções para utilização
#1 - No console, digite: python adivinhacao.py

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
    print("\n")
    print("-----------BEM VINDO AO JOGO DA ADIVINHAÇÃO DE NÚMEROS-----------")
    print("\n")    
    sorteio = (random.randint(1, 50))
    continuar = True
    acerto = False
    while(continuar == True):        
        rodada = 1
        while(rodada < 11):
            print("-------------------"+CYAN + "RODADA "+str(rodada)+RESET+"-------------------------------")
            
            palpite = int(input("Digite um número entre 1 e 50: "))
            if(palpite == sorteio):
                print(GREEN+ "PARABÉNS! " + RESET + "Você acertou o número...")
                break
            else:
                print(RED+ "ERROU! " + RESET + "Tente novamente")
                if(palpite < sorteio):
                    print(BLUE+ "DICA: " + RESET + "O número é maior que "+ str(palpite))
                else:
                    print(BLUE+ "DICA: " + RESET + "O número é menor que "+ str(palpite))
            rodada = rodada + 1

        print("-------------------------------------------------------------------------")
        resposta = input("Deseja tentar adivinhar novamente: 'S/N'")
        resposta = resposta.upper()
        if(resposta=='N'):
            exit()
        





#chamada da função principal, diretamente do arquivo
chamada = sys.argv[0]
if(chamada =="adivinhacao.py"):
    jogoAdivinhacao()