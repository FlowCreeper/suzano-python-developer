texto = input("Informe um texto: ")

VOGAIS = "AEIOU"

# O for é uma estrutura de repetição que percorre uma sequência de elementos, como uma lista ou uma string.
# Neste exemplo, o for percorre cada letra do texto informado pelo usuário.
# A cada iteração, a variável letra recebe o valor da letra atual.
for letra in texto:
  if letra.upper() in VOGAIS:
    print(letra, end="")

# O else do for é executado quando o loop termina normalmente, ou seja, sem encontrar um break.
else:
  print()

# Exemplo de for utilizando a função built-in range()
# O range é uma função que gera uma sequência de números inteiros, começando do valor inicial (inclusivo) e terminando no valor final (exclusivo).
# O passo é opcional e define o intervalo entre os números gerados.
# Neste exemplo, o for percorre os números de 0 a 50, com um passo de 5.
for numero in range(0, 51, 5):
  print(numero, end=" ")

# Se for passado apenas um argumento, o range começa do 0 e vai até o número informado (exclusivo).
# Neste exemplo, o for imprime de 0 a 6
for numero in range(7):
  print(numero, end=" ")