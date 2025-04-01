# A função input() exibe uma mensagem e aguarda o usuário digitar algo
nome = input("Informe seu nome: ") 
idade = input("Informe sua idade: ")

print(nome, idade) # Exibe o nome e a idade informados pelo usuário
print("teste", end=" ") # Exibe a string "teste" e não pula linha
print(nome, idade, end="...\n") # Exibe o nome e a idade informados pelo usuário, mas com '...' no final
print(nome, idade, end="...\n", sep="#") # Exibe o nome e a idade informados pelo usuário, mas com '...' no final e '#' entre eles
print(nome, idade, sep="#") # Exibe o nome e a idade informados pelo usuário, mas com '#' entre eles