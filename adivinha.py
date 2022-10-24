
print(10 * "*")
print('Bem vindo ao jogo de adivinhação')
print(10 * "*")

#área de declaração de variáveis globais
numero_secreto = 42
total_de_tentativas = 3


for rodada in range (1, total_de_tentativas + 1 ):
  
  print('Tentiva {} de {}'.format(rodada, total_de_tentativas))
  suposicao=int(input('** Digite o seu número de 1 a 100 **\n')) #Tentativa de acertar o numero secreto
  print("Você digitou: ",suposicao)

  if(suposicao < 1 or suposicao > 100):
      print('** Você deve digitar um número entre 1 e 100! ** ')
      continue
  #Variáveis internas do laço
  acertou =  suposicao == numero_secreto 
  maior = suposicao > numero_secreto
  menor = suposicao < numero_secreto

  #Caso de acerto
  if numero_secreto == suposicao:
   print(10 * "*")
   print('Parabéns!')
   print('Você digitou o número correto!')
   print(10 * "*")
   break
   #Dica para caso de erro
  else:
    if(maior):
      print('Você errou! O seu chute foi maior que o número secreto.')
    elif(menor):
    
      print('Você errou! O seu chute foi menor que o número secreto.')
  
print('Fim de jogo')

