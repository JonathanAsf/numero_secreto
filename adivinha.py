
print(10 * "*")
print('Bem vindo ao jogo de adivinhação')
print(10 * "*")
#área de declaração de variáveis globais
numeroSecreto = 42
total_de_tentativas = 3
rodada= 1

while (rodada <= total_de_tentativas):

  print('Tentiva {} de {}'.format(rodada, total_de_tentativas))
  suposicao=int(input('Digite o seu número:\n')) #Tentativa de acertar o numero secreto
  print("Você digitou: ",suposicao)

  acertou = numeroSecreto == suposicao
  maior = suposicao > numeroSecreto
  menor = suposicao < numeroSecreto

  #Caso de acerto
  if numeroSecreto==suposicao:

   print(10 * "*")
   print('Parabéns!')
   print('Você digitou o número correto!')
   print(10 * "*")
   
   #Dica para o jogador
  else:
    if(maior):
      print('Você errou! O seu chute foi maior que o número secreto.')
    elif(menor):
      rodada = rodada + 1
      print('Você errou! O seu chute foi menor que o número secreto.')
  total_de_tentativas = total_de_tentativas - 1

  #Caso o número tentativas máximas foi alcançado.

  if (rodada > total_de_tentativas):
    print("Game Over, melhor sorte na próxima vez")
    break
