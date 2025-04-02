conta_normal = False
conta_universitaria = True
conta_especial = False

saldo = 2000
saque = 500
cheque_especial = 450

# Verifica se o usuário tem conta normal ou universitária
if conta_normal:

  # Faz mais verificações de forma aninhada
  if saldo >= saque:
    print("Saque realizado com sucesso!")
  elif saque <= (saldo + cheque_especial):
    print("Saque realizado com uso do cheque especial!")
  else:
    print("Não foi possível realizar o saque, saldo insuficiente!")

elif conta_universitaria:

  # Faz mais verificações de forma aninhada
  if saldo >= saque:
    print("Saque realizado com sucesso!")
  else:
    print("Sadldo insuficiente!")

elif conta_especial:
  print("Conta especial, selecionada!")

else:
  print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")