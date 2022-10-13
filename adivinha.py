print('*********************************')
print('Bem vindo ao jogo de adivinhação')
print('*********************************')
#área de declaração de variáveis globais
numeroSecreto=42
total_de_tentativas = 3
rodada=1

while (rodada <=total_de_tentativas > 0):
  print('Tentivas restantes: ',total_de_tentativas)
  suposicao=int(input('Digite o seu número número: '))
  acertou = numeroSecreto == suposicao
  maior = suposicao > numeroSecreto
  menor = suposicao < numeroSecreto
  print("Você digitou: ",suposicao)

  if numeroSecreto==suposicao:
   print('*********************************')
   print('Você digitou o número correto!')
   print('*********************************')
  else:
    if(maior):
      print('Você errou! O seu chute foi maior que o número secreto.')
    elif(menor):
      print('Você errou! O seu chute foi menor que o número secreto.')
  total_de_tentativas = total_de_tentativas - 1
print('*********************************')
print('Fim do jogo')
print('*********************************')
