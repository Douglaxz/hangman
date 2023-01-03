import random

palavrasAdivinhacao = ['banana', 'maca', 'pera', 'uva']

tamanhoArray = len(palavrasAdivinhacao)

sorteio = int(random.randint(0, tamanhoArray))

celulas = ['','','','','','','','','']

print("BEM VINDO AO JOGO DA VELHA")
print("\n")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")
print("\n")
jogada = input("Jogador X, escolha uma posição conforme o diagrama abaixo:")
print("\n")
if (int(jogada) > 0 and int(jogada) < 10):
    celulas[int(jogada )- 1] = "X"
    print(celulas)
else:
    print("Escolha um numero entre 1 e 9")




