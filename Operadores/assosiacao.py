frutas = ["limao", "uva"]
curso = "Curso de Python"

# Operadores de associação em Python
# O operador 'in' verifica se um elemento está presente em uma lista ou string
# O operador 'not in' verifica se um elemento não está presente em uma lista ou string
# Ambos operadores são case-sensitive, ou seja, diferenciam maiúsculas de minúsculas

# Exemplo de uso do operador 'in'
print("uva" in frutas) # True
print("laranja" in frutas) # False
print("Limao" in frutas) # False (case-sensitive)

# Exemplo de uso do operador 'not in'
print("banana" not in frutas) # True
print("uva" not in frutas) # False
print("UVA" not in frutas) # True (case-sensitive)

# Exemplo de uso do operador 'in' com strings
print("Python" in curso) # True
print("python" in curso) # False (case-sensitive)
