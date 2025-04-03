nome = "Caio"
idade = 20
profissao = "Estudante"
linguagem = "Python"
saldo = 45.435

pessoa = {"nome": nome, "idade": idade, "profissao": profissao, "linguagem": linguagem}

print("Nome: %s, Idade: %d" % (nome, idade)) # Old Style %s = string, %d = int, %f = float

print("Nome: {}, Idade: {}".format(nome, idade)) # format básico
print("Nome: {1}, Idade: {0}".format(idade, nome)) # format com endereço
print("Nome: {1}, Idade: {0}, Idade: {0}".format(idade, nome)) # Pode ser repetido
print("Nome: {nome}, Idade: {idade}".format(nome=nome, idade=idade)) # format com dict determinando um por um
print("Nome: {name}, Idade: {age}".format(age=idade, name=nome)) # a ordem não importa e não precisa ser o mesmo nome do parametro e da variável
print("Nome: {nome}, Idade: {idade}".format(**pessoa)) # format com dict direto

print(f"Nome: {nome}, Idade: {idade}") # f-String usa as variáveis diretamente
print(f"Nome: {nome}, Idade: {idade}, Saldo: {saldo:.2f}") # Limitação do float para 2 casas decimais arrendondando para o mais próximo
print(f"Nome: {nome}, Idade: {idade}, Saldo: {saldo:10.1f}") # Limitação do float para 1 casas decimais e 10 espaços para inteiros
