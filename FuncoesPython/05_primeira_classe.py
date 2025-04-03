def somar(a, b):
  return a + b

def test(a, b):
  if a and b:
    return True
  return False


def exibir_resultado(a, b, funcao):
  resultado = funcao(a, b)
  print(f"Resultado da operação: {resultado}")

exibir_resultado(10, 10, somar)  # Resultado da operação: 20
exibir_resultado(10, -1, test)  # Resultado da operação: True

soma = somar

print(somar(10,4)) # 14