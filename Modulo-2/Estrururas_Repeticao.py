# Estruturas de repetição em Python

# 1. Laço "for"
# O laço "for" é usado para iterar sobre uma sequência (como listas, strings ou intervalos).
print("Exemplo de 'for':")
for i in range(5):  # range(5) gera os números 0, 1, 2, 3, 4
    print(f"Iteração {i}")

# 2. Laço "while"
# O laço "while" continua executando enquanto a condição for verdadeira.
print("\nExemplo de 'while':")
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementa o contador

# 3. Uso de "break" para sair de um laço
print("\nExemplo de 'break':")
for i in range(10):
    if i == 5:  # Sai do laço quando i for igual a 5
        break
    print(f"Valor de i: {i}")

# 4. Uso de "continue" para pular uma iteração
print("\nExemplo de 'continue':")
for i in range(5):
    if i == 2:  # Pula a iteração quando i for igual a 2
        continue
    print(f"Valor de i: {i}")

# 5. Laços aninhados
print("\nExemplo de laços aninhados:")
for i in range(3):  # Laço externo
    for j in range(2):  # Laço interno
        print(f"i = {i}, j = {j}")

# 6. Uso de "else" com laços
# O bloco "else" é executado quando o laço termina normalmente (sem "break").
print("\nExemplo de 'else' com laço:")
for i in range(3):
    print(f"Valor de i: {i}")
else:
    print("Laço concluído sem interrupções.")