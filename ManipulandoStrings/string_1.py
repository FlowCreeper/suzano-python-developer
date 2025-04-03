nome = "FloW CreepEr"

# Manipulação de strings através de algumas funções built-in

print(nome.upper()) # Nome normal
print(nome.upper()) # Deixa todos os caracteres maiúsculos
print(nome.lower()) # Deixa todos os caracteres minúsculos
print(nome.title()) # Deixa os primeiros caracteres maiúsculos e o restante minúsculos, se usado espaço ele deixará o primeiro caracter após o espaço maiúsculo

texto = "  Hello World         "

print(texto + ".") # Texto normal
print(texto.strip() + ".") # Tira os espaços em excesso tanto da esquerda quanto da direita
print(texto.lstrip() + ".") # Tira apenas da esquerda
print(texto.rstrip() + ".") # Tira apenas da direita

menu = "Python"

print("####" + menu + "####") # Feito de forma manual
print(menu.center(14)) # Centraliza automáticamente, usando o valor como total de caracteres da string
print(menu.center(14, "~")) # Utiliza o caracter do segundo parâmetro para preencher os lados 

print("P-y-t-h-o-n") # Feito de forma manual
print("-".join(menu)) # Retorna a string passada no parâmetro com a string chamando a função separando cada caracter do parâmetro
# Loop equivalente a função join()
for x in range(len(menu)):
  if x == len(menu) - 1:
    print(menu[x])
    continue
  print(menu[x], end="-")