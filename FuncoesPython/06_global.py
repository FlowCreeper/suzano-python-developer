salario = 2000


def salario_bonus(bonus, lista):
  global salario
  lista_aux = lista.copy()
  lista_aux.append(2)

  print("Auxiliar: ", lista_aux)

  salario += bonus
  return salario

lista = [1]
print(salario_bonus(500,lista))  # 2500

print("Inicial: ", lista)