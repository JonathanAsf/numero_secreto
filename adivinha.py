import random

print(10 * "*")
print('Bem vindo ao jogo de adivinhação')
print(10 * "*")

#Área de declaração de variáveis globais
numero_secreto = round(random.randrange(1, 101)) #Numeros aleatórios com range de 1 à 100
total_de_tentativas = 0
pontos = 1000

#Seleção de dificuldade
print('Selecione um nível de dificuldade: ')
print('1 - Fácil')
print('2 - Médio')
print('3 - Difícil')

dificuldade = int(input(''))

if dificuldade == 1:
  total_de_tentativas = 20
elif dificuldade == 2:
  total_de_tentativas = 10
else:
  total_de_tentativas = 5

#Laço de repetição das chances
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
   print("A sua pontuação foi {}!\n".format(pontos))
   break
   #Dica para caso de erro
  else:

    if(maior):
      print('Você errou! O seu chute foi maior que o número secreto.')
    elif(menor):
      print('Você errou! O seu chute foi menor que o número secreto.')
    pontos_perdidos = abs(numero_secreto - suposicao) #Valor absoluto  para não haver pontuação negativa
    pontos = pontos - pontos_perdidos
print('Fim de jogo')
