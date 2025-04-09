# Exemplos de interpolação de variáveis em Python

# 1. Usando o operador `%` (antigo estilo)
nome = "João"
idade = 25
print("Meu nome é %s e eu tenho %d anos." % (nome, idade))
# Explicação: O operador `%` é usado para substituir os placeholders (%s para string, %d para inteiros, etc.)
# pelos valores fornecidos em uma tupla.

# 2. Usando o método `str.format()` (estilo moderno)
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))
# Explicação: O método `format()` substitui os `{}` pelos valores fornecidos na ordem ou por índices nomeados.

# 3. Usando f-strings (a partir do Python 3.6)
print(f"Meu nome é {nome} e eu tenho {idade} anos.")
# Explicação: As f-strings permitem incluir expressões diretamente dentro de strings, usando `{}`.
# É a forma mais moderna e legível de interpolação.