# Condicionais
# Estruturas condicionais são usadas para tomar decisões em um programa.

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

# Pede para o usuário digitar a idade
idade = int(input("Digite sua idade: "))

# Verifica se a idade é maior ou igual a MAIOR_IDADE
if idade >= MAIOR_IDADE:
  print("Maior de idade, pode tirar a CNH.")

# Verifica se a idade é menor que MAIOR_IDADE
if idade < MAIOR_IDADE:
  print("Ainda não pode tirar a CNH.")

# Verifica denovo se a idade é maior ou igual a MAIOR_IDADE
if idade >= MAIOR_IDADE:
  print("Maior de idade, pode tirar a CNH.")
# Neste exemplo, podemos usar o else pois nesse caso se não for maior de idade, só pode ser menor de idade
# Neste caso, o else é mais eficiente que o if, pois não precisamos verificar novamente a condição
else:
  print("Ainda não pode tirar a CNH.")

# Verifica novamente se a idade é maior ou igual a MAIOR_IDADE, caso não seja ele passa para o elif/else
if idade >= MAIOR_IDADE:
  print("Maior de idade, pode tirar a CNH.") 
# Neste exemplo, usamos o elif para verificar se a idade é igual a IDADE_ESPECIAL, e se for, imprime uma mensagem diferente
elif idade == IDADE_ESPECIAL:
  print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
# Else sendo usado novamente, mas agora para verificar se a idade é menor que MAIOR_IDADE e diferente de IDADE_ESPECIAL
else:
  print("Ainda não pode tirar a CNH.")


# Neste exemplo, mesmo que ele seja maior de idade, ele ainda verificará se a idade é 15, e se for, imprime uma mensagem diferente
if idade >= MAIOR_IDADE:
  print("Maior de idade, pode tirar a CNH.")
if idade == 15:
  print("Você tem 15 anos.")
else:
  print("Você não possui 15 anos")