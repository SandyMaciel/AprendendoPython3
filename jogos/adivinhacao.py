print("**********************************")
print("Bem-vindo ao jogo de Adivinhação!")
print("**********************************")

numero_secreto = 42
total_tentativas = 3

for rodada in range (1,total_tentativas + 1):
    print ("Tentativa {} de {}".format(rodada,total_tentativas))
    chute_str = input("Digite seu número de 1 a 100:")
    print("Você digitou ",chute_str)
    chute = int (chute_str)
    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 0 e 100")
        continue
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Vc acertou")
        break
    else:
        if(maior):
            print("Vc errou! O seu chute foi maior")
        elif (menor):
            print("Vc errou! O seu chute foi menor")

print("Fim do Jogo")