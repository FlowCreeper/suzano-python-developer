print(int(1.120)) # Converte o float 1.120 para inteiro >>> 1
print(int("1")) # Converte a string "1" para inteiro >>> 1
# print(int("1.1")) # Não é possivel converter pois é um float não um int >>> ValueError: invalid literal for int() with base 10: '1.1'
print(float("1.1")) # Converte a string "1.1" para float >>> 1.1
print(float("100")) # Converte a string "100" para float >>> 100.0

print(type(str(10.10))) # Converte o float 10.10 para string >>> <class 'str'>

valor = 10 # A variável valor recebe o valor 10
valor_str = str(valor) # Converte o inteiro 10 para string
print(type(valor)) # <class 'int'> 
print(type(valor_str)) # <class 'str'>

print(100 / 2) # Divisão de inteiros >>> 50.0
print(100 // 2) # Divisão inteira de inteiros >>> 50
# Se o qualquer um dos números for float, o resultado será float arredondado para baixo
print(100 / 2.0) # Divisão de int por float >>> 50.0
print(100.0 / 2) # Divisão de float por int >>> 50.0
print(100.0 // 2.0) # Divisão de float por float >>> 50.0
print(7 / 4) # Divisão de inteiros >>> 1.75
print(7.0 // 4.0) # Divisão de float por float arredondando para baixo >>> 1.0