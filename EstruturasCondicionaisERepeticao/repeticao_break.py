while True:
  opcao = int(input("Informe um número: "))
  
  if opcao == 10:
    # O break é usado para interromper o loop imediatamente.
    break

  print(opcao)

for numero in range(100):
  if numero == 10:
    # Ele também pode ser usado para interromper um loop for.
    break

  print(numero)

for numero in range(100):
  if numero % 2 == 0:
    # O continue é usado para pular a iteração atual e continuar com a próxima.
    continue

  print(numero)  