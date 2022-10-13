print('*********************************')
print('Bem vindo ao jogo de adivinhação')
print('*********************************')
#área de declaração de variáveis
numeroSecreto=42
suposicao=int(input('Digite o seu número número: '))
acertou = numeroSecreto == suposicao
maior = suposicao > numeroSecreto
menor = suposicao < numeroSecreto

print("Você digitou: ",suposicao)

#Condição de acerto
if numeroSecreto==suposicao:
  print('Você digitou o número correto!')
else:
  if(maior):
    print('Você errou! O seu chute foi maior que o número secreto.\n')
  elif(menor):
    print('Você errou! O seu chute foi menor que o número secreto.\n')

print('*********************************')
print('Fim do jogo')
print('*********************************')
