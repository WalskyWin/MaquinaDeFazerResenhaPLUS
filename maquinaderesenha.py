import random
import os
import webbrowser

def limpa():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    limpa()

    print("""
=====================================
▖  ▖      ▘    
▛▖▞▌▀▌▛▌▌▌▌▛▌▀▌
▌▝ ▌█▌▙▌▙▌▌▌▌█▌           
▄ 
▌▌█▌
▙▘▙▖
▄▖        
▙▖▀▌▀▌█▌▛▘
▌ █▌▙▖▙▖▌ 
          
▄▖▄▖▄▖▄▖▖ ▖▖▖▄▖
▙▘▙▖▚ ▙▖▛▖▌▙▌▌▌
▌▌▙▖▄▌▙▖▌▝▌▌▌▛▌
               
▄▖▖ ▖▖▄▖
▙▌▌ ▌▌▚ 
▌ ▙▖▙▌▄▌         feito por win melhor dev do país
                   
=====================================

1 - Diversão plus
2 - Desafio aleatório plus
3 - Sorteio plus
4 - Detector de mentira plus
5 - Frase resenhuda plus
6 - W Música plus
0 - Sair

""")

    op = input("> ")

    if op == "1":
        coisas = [
            "Primeiro a falar abacate ganha",
            "kaio mais resenha daqui",
            "essa e a melhor resenha que ja vi ez?"
        ]
        print("\n" + random.choice(coisas))

    elif op == "2":
        desafios = [
            "Faz 15 flexões",
            "Cantar qualquer musica plus",
            "Dar 3 mortais",
            "Dar um mortal"
        ]
        print("\nDESAFIO:")
        print(random.choice(desafios))

    elif op == "3":
        nomes = input("Nomes separados por vírgula: ")
        lista = nomes.split(",")

        print("\nO Sorteado foi o que eu vou falar ez")
        print(random.choice(lista).strip())

    elif op == "4":
        input("Digite qualquer coisa: ")

        chance = random.randint(0, 100)

        if chance > 70:
            print("\nMENTIRA ABSURDA")
        elif chance > 40:
            print("\nTem cara de mentira")
        else:
            print("\nTalvez seja verdade")

    elif op == "5":
        frases = [
            "Melhor resenha de todas?",
            "Resenha ez? eu amo fazer resenhas resenhudas",
            "Resenha forte ezzzzzzzzzzzzzzzzzzzzzzzzzzzz",
            "Nunca pertube o kaio enquanto ele ta ocupado."
        ]
        print("\n" + random.choice(frases))

    elif op == "6":
        print("""
===================
     W MÚSICA
===================

1 - Estou no Clubexx p l u s
0 - Voltar
""")

        while True:
            mus = input("> ")

            if mus == "1":
                print("\nTocando a musica resenha, vai pro seu navegador pra dar o play pq eu não consegui fazer isso ser automatico, ez")
                webbrowser.open("https://youtu.be/PSfIiB0yd8g")

            elif mus == "0":
                break

            else:
                print("opção inválida")

    elif op == "0":
        print("tchau volte sempre ezz resenha plus on top")
        break

    input("\nENTER...")
 
# porque tu ta lendo o meu código bro? eu não coloquei vírus
