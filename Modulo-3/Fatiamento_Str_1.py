# capitalize(): Converte o primeiro caractere da string para maiúsculo.
texto = "python é incrível"
print(texto.capitalize())  # Saída: "Python é incrível"

# upper(): Converte todos os caracteres da string para maiúsculo.
print(texto.upper())  # Saída: "PYTHON É INCRÍVEL"

# lower(): Converte todos os caracteres da string para minúsculo.
print(texto.lower())  # Saída: "python é incrível"

# strip(): Remove espaços em branco (ou caracteres especificados) do início e do fim da string.
texto_com_espacos = "   Olá, Mundo!   "
print(texto_com_espacos.strip())  # Saída: "Olá, Mundo!"

# replace(): Substitui uma substring por outra.
print(texto.replace("incrível", "fantástico"))  # Saída: "python é fantástico"

# split(): Divide a string em uma lista com base em um delimitador.
frase = "Aprender Python é divertido"
print(frase.split())  # Saída: ['Aprender', 'Python', 'é', 'divertido']

# join(): Junta elementos de uma lista em uma string, usando um delimitador.
palavras = ['Python', 'é', 'incrível']
print(" ".join(palavras))  # Saída: "Python é incrível"

# find(): Retorna o índice da primeira ocorrência de uma substring. Retorna -1 se não encontrada.
print(texto.find("incrível"))  # Saída: 10

# isdigit(): Verifica se todos os caracteres da string são dígitos.
numero = "12345"
print(numero.isdigit())  # Saída: True

# startswith(): Verifica se a string começa com uma substring específica.
print(texto.startswith("python"))  # Saída: True

# endswith(): Verifica se a string termina com uma substring específica.
print(texto.endswith("incrível"))  # Saída: True

# center(): Centraliza a string em um determinado comprimento, preenchendo com espaços ou outro caractere.
print(texto.center(30, "-"))  # Saída: "----------python é incrível----------"  

