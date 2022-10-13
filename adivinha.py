print('*********************************')
print('Bem vindo ao jogo de adivinhação')
print('*********************************')

numeroSecreto=42
suposicao=int(input('Digite o seu número número: '))
print("Você digitou: ",suposicao)

if numeroSecreto==suposicao:
  print('Você digitou o número correto!')
else:
  print('Você digitou o número errado')
print('Fim do jogo')
