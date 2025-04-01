# Operadores lógicos em Python

# AND = para ser verdadeiro, ambos os lados devem ser verdadeiros
print(True and True) # True
print(True and False) # False
print(False and False) # False
# OR = para ser verdadeiro, pelo menos um dos lados deve ser verdadeiro
print(True or True) # True
print(True or False) # True
print(False or False) # False
# NOT = inverte o valor lógico (se for verdadeiro, torna-se falso e vice-versa)
print(not True) # False
print(not False) # True

# Exemplo prático de uso de operadores lógicos

saldo = 1000
saque = 250
limite = 200
conta_especial = True

# Verifica se o saldo é suficiente para o saque
# O saque só pode ser realizado se o saldo for maior ou igual ao valor do saque
# E se o saque for menor ou igual ao limite ou se a conta for especial
exp = saldo >= saque and (saque <= limite or conta_especial)

print(exp) # True

# Outra forma de escrever a mesma expressão
exp_2 = saldo >= saque and saque <= limite or saldo >= saque and conta_especial

print(exp_2) # True

# Como boa prática, evite escrever expressões muito longas e complexas

# Use parênteses para deixar o código mais legível
exp_3 = (saldo >= saque and saque <= limite) or (saldo >= saque and conta_especial)

# Ou separe em variáveis
conta_normal_com_saldo = saldo >= saque and saque <= limite
conta_especial_com_saldo = saldo >= saque and conta_especial
exp_4 = conta_normal_com_saldo or conta_especial_com_saldo

print(exp_4) # True
