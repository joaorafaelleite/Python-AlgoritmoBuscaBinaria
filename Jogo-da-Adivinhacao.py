from random import randint

print("Bem vindo ao jogo da adivinhação!")
print("\nEste é um jogo Player versus Environment, onde você pode jogar como Sorteador ou Adivinhador.")
print("\nO Sorteador deve pensar em número inteiro e fornecer um intervalo mínimo e máximo para que o oponente tente adivinhar, além disso ele tem como papel dar dicas escrevendo MENOR quando o palpite for superior ao valor pensado,"
      "\n MAIOR quando o palpite for inferior ao valor pensado e CORRETO quando o adversário acertar o palpite, estas indicações devem ser inseridas após a aparição do campo Resposta:")
print("\nO Adivinhador deve tentar acertar o número pensado pelo Sorteador, guiando-se pelas dicas MAIOR ou MENOR, para elaborar seus palpites futuros")
print("\nObs: Por se tratar de um jogo PvE, você irá enfrentar o computador, então caso ache engraçado zombar dele, indicando que o palpite está errado quando ele acertar,"
      "\n recomendo que você assista a saga O Exterminador do Futuro")

print("\nVamos começar, como você prefere jogar?")
tipo_de_jogo = int(input("Digite 1 para ser o Sorteador e 2 para ser o Adivinhador: "))

while tipo_de_jogo != 1 and tipo_de_jogo != 2:
    print("Opção inválida, favor escolher como prefere jogar!")
    tipo_de_jogo = int(input("Digite 1 para ser o Sorteador e 2 para ser o Adivinhador: "))

if tipo_de_jogo == 1:
    Min = int(input("Digite o valor mínimo: "))
    Max = int(input("Digite o valor máximo, sendo, no mínimo, 100 unidades a mais que o valor mínimo: "))
    while Max <  Min+100:
        print("Valores fora de parametros, favor redigitar!")
        Min = int(input("Digite o valor mínimo: "))
        Max = int(input("Digite o valor máximo, sendo, no mínimo, 100 unidades a mais que o valor mínimo: "))
    lista_palpites = []
    cont = 1
    palpite = int((Min+Max)/2)
    print("O valor seria: {}".format(palpite))
    Resposta = input("Resposta: ")
    Resposta = Resposta.lower()
    while Resposta != "correto":
        if Resposta == "menor":
            lista_palpites.append(palpite)
            Max = palpite
            palpite = int((Min+Max)/2)
            print("O valor seria: {}".format(palpite))
        elif Resposta == "maior":
            lista_palpites.append(palpite)
            Min = palpite
            palpite = int((Min+Max)/2)
            print("O valor seria: {}".format(palpite))
        Resposta = input("Resposta: ")
        Resposta = Resposta.lower()
        cont += 1
    lista_palpites.append(palpite)
    print("\n\nParabéns, o valor {} está correto!".format(palpite))
    print("\nForam dados {} palpites até acertar o valor".format(cont))
    print("\nOs palpites dados foram:")
    print(lista_palpites)

else:
    Min = int(input("Digite o valor mínimo: "))
    Max = int(input("Digite o valor máximo, sendo, no mínimo, 100 unidades a mais que o valor mínimo: "))
    X = randint(Min,Max)
    lista_palpites = []
    cont = 1
    palpite = int(input("Digite um palpite: "))
    while palpite != X:
        if palpite > X:
            lista_palpites.append(palpite)
            print("Palpite SUPERIOR ao valor a ser advinhado")
            palpite = int(input("Digite um palpite: "))
        elif palpite < X:
            lista_palpites.append(palpite)
            print("Palpite INFERIOR ao valor a ser adivinhado")
            palpite = int(input("Digite um palpite: "))
        cont += 1
    lista_palpites.append(palpite)
    print("\n\nParabéns, o valor {} está correto!".format(palpite))
    print("\nForam dados {} palpites até acertar o valor".format(cont))
    print("\nOs palpites dados foram:")
    print(lista_palpites)