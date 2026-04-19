#Atividade em Sala - Pedra, Papel e Tesoura
import random
print("BemVindo ao Jogo Pedra,Papel e Tesoura.\n")
pedra = 1
papel = 2
tesoura = 3
soma_player = 0
soma_pc = 0
play_again = "S"

while play_again == "S":

    player2 = random.randint(1, 3)
    escolha_usuario = int(input("Escolha entre: \nPedra [1]\nPapel [2]\nTesoura [3]\nSair [0]\n"))  

    if player2 == 1 and escolha_usuario == 3:
        print(f"\nO PC escolheu {player2} e o player {escolha_usuario}")
        print("O PC ganhou!\n")
        soma_pc = soma_pc + 1
    elif player2 == 2 and escolha_usuario == 1:
        print(f"\nO PC escolheu {player2} e o player {escolha_usuario}")
        print("O PC ganhou!\n")
        soma_pc = soma_pc + 1
    elif player2 == 3 and escolha_usuario == 2:
        print(f"\nO PC escolheu {player2} e o player {escolha_usuario}")
        print("O PC ganhou!\n")
        soma_pc = soma_pc + 1

    elif player2 == escolha_usuario:
        print(f"\nO PC escolheu {player2} e o player {escolha_usuario}")
        print("Deu empate, ningúem ganhou!\n")

    elif escolha_usuario == 0:
        break

    elif escolha_usuario > 3 or escolha_usuario < 0:
        print("Error: Digite uma das opções!\n")

    else:
        print(f"\nO PC escolheu {player2} e o player {escolha_usuario}")
        print("Você ganhou (O Player)!\n")
        soma_player = soma_player + 1


    if soma_pc == 3:
        print("O pc ganhou!\n")
        break
    if soma_player == 3:
        print("O player ganhou!\n")
        break
    
resposta = input("Voce quer continuar jogando? [S,N]: ")
print("\n")
if resposta == "S":
    play_again = "S"
else:
    play_again = "N"


print(f"\nPLACAR FINAL\nPlayer = {soma_player}\nPC = {soma_pc}\n")
print("\n")
print("Fim do Programa.")


