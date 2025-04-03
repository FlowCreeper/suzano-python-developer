def calcular_total(numeros):
  return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
  return numero - 1, numero + 1

def func_3():
  print("Olá mundo!")

print(calcular_total([10, 20, 34])) # 64
print(retorna_antecessor_e_sucessor(10)) # (9, 11)
print(func_3()) # None