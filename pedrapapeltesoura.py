#import de dependencias
import random

def pedrapapeltesoura():
    #declaração de variáveis
    opcaoUsuario = 0
    selecaoUsuario = 0
    opcoes = []
    resposta = True

    #carregamento da tupla
    opcao = ('PEDRA',"O")
    opcoes.append(opcao)
    opcao = ('PAPEL',"|||||")
    opcoes.append(opcao)
    opcao = ('TESOURA',"V")
    opcoes.append(opcao)


    #Cabeçalho do jogo    
    print("\n")
    print("---------- BEM VINDO AO JOGO PEDRA PAPEL TESOURA ----------")
    print("\n")

    sorteio = (random.randint(0, len(opcoes)-1))
    opcaoCPU = opcoes[sorteio]

    contador = 1
    for opcao in opcoes:
        print(str(contador) + " | ", end="")
        print(opcao[0])
        contador = contador + 1

    print("\n")

    #perguntando a opção do usuario
    while(int(selecaoUsuario) < 1 or int(selecaoUsuario) > 3):
        resposta = (input("Escolha conforme o número acima: "))
        if(resposta.isalpha()==False):
            selecaoUsuario = int(resposta)
        else:
            selecaoUsuario = 0


    #verificação de resposta com a tupla
    opcaoUsuario = opcoes[selecaoUsuario-1]

    #menu de resposta
    print("----------------------------------- RESULTADO ----------------------------------")
    print("| ", end="")
    print("CPU", end="")
    print("       |", end="")
    print(opcaoCPU[0])
    print("| ", end="")
    print("USUARIO", end="")
    print("   |", end="")
    print(opcaoUsuario[0])
    print("| ", end="")
    print("RESULTADO", end="")
    print(" |", end="")
    resultado = ""

    #conferindo o resultado
    if(opcaoCPU[0]=="PEDRA"):
        match opcaoUsuario[0]:
            case "PAPEL":
                resultado = "PAPEL EMBRULHA PEDRA - VITORIA DO USUARIO"
            case "TESOURA":
                resultado = "PEDRA AMASSA TESOURA - VITORIA DA CPU"
            case "PEDRA":
                resultado = "EMPATE - VITORIA DE NINGUEM"

    if(opcaoCPU[0]=="TESOURA"):
        match opcaoUsuario[0]:
            case "PAPEL":
                resultado = "TESOURA CORTA PAPEL - VITORIA DA CPU"
            case "TESOURA":
                resultado = "EMPATE - VITORIA DE NINGUEM"
            case "PEDRA":
                resultado = "PEDRA AMASSA TESOURA - VITORIA DO USUARIO"   

    if(opcaoCPU[0]=="PAPEL"):
        match opcaoUsuario[0]:
            case "PAPEL":
                resultado = "EMPATE - VITORIA DE NINGUEM"
            case "TESOURA":
                resultado = "TESOURA CORTA PAPEL - VITORIA DO USUARIO"
            case "PEDRA":
                resultado = "PAPEL EMBRULHA PEDRA - VITORIA DA CPU" 

    print(resultado)

#função principal
pedrapapeltesoura()
resposta = ""
while(resposta==""):
    print("\n")
    resposta = input("Deseja jogar novamente: 'S/N'")
    resposta = resposta.upper()
    if(resposta=='N'):
        exit()
    elif (resposta=='S'):
        pedrapapeltesoura()
        resposta = ""
    else:
        print("Resposta inválida")
        resposta = ""
print("--------------------------------------------------------")
