# Indentação e blocos de código
# A indentação em Python é fundamental para definir blocos de código, como os que estão dentro de funções, loops e condicionais.
# A falta de indentação correta pode levar a erros de sintaxe ou lógica no código.
# Abaixo está um exemplo de função que verifica se o saldo é suficiente para realizar um saque.
def sacar(valor: float): 
  # Aqui começa o bloco da função
  saldo = 500

  if saldo >= valor:
    # Aqui começa o bloco do if
    print("Valor sacado!")
    print("Retire o seu dinheiro na boca do caixa.")
    # Aqui termina o bloco do if
  print("Obrigado por ser nosso cliente, tenha um bom dia!") # Essa linha sempre será executada, independentemente do saldo, pois está fora do bloco do if.
  # Aqui termina o bloco da função

# Se a identação não for respeitada, o Python levantará um erro de sintaxe.
# def depositar(valor):
# saldo = 500
# saldo += valor

# Forma correta de indentação para a função depositar
def depositar(valor):
  saldo = 500
  saldo += valor

# Exemplo de uso da função
sacar(100) # valor sacado!