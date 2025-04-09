# Fatiamento de strings em Python

# Em Python, você pode acessar partes de uma string usando fatiamento.
# A sintaxe básica é: string[início:fim:passo]

# Exemplo 1: Fatiamento básico
texto = "Python é incrível"
print(texto[0:6])  # Saída: Python (caracteres da posição 0 até 5)

# Exemplo 2: Omissão de índices
print(texto[:6])   # Saída: Python (do início até a posição 5)
print(texto[7:])   # Saída: é incrível (da posição 7 até o final)

# Exemplo 3: Índices negativos
print(texto[-9:])  # Saída: incrível (contando de trás para frente)

# Exemplo 4: Passo no fatiamento
print(texto[::2])  # Saída: Pto énrv (pula de 2 em 2 caracteres)

# Exemplo 5: Invertendo uma string
print(texto[::-1]) # Saída: levíicnI é nohtyP (string invertida)

# Observação:
# - O índice 'início' é inclusivo.
# - O índice 'fim' é exclusivo.
# - O 'passo' define o intervalo entre os caracteres selecionados.