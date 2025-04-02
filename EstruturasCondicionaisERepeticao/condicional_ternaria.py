saldo = 2000
saque = 2500

# Verifica se o usuário tem saldo suficiente para realizar o saque
# Usando condicional ternária para definir o status do saque
# Se o saldo for maior ou igual ao valor do saque, status será "Sucesso"
# Caso contrário, status será "Falha"
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")