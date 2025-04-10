#Listas criação e acesso a dados.

# Criando uma lista de frutas
frutas = ["maçã", "banana", "laranja", "uva"]

# Acessando elementos da lista
print(frutas[0])  # Acessa o primeiro elemento (maçã)
print(frutas[2])  # Acessa o terceiro elemento (laranja)
print(frutas[-1])  # Acessa o último elemento (uva)
print(frutas[-2])  # Acessa o penúltimo elemento (laranja)
print(frutas[1:3])  # Acessa uma fatia da lista (banana e laranja)
print(frutas[:2])  # Acessa os dois primeiros elementos (maçã e banana)
print(frutas[2:])  # Acessa os elementos a partir do terceiro (laranja e uva)
print(frutas[::2])  # Acessa os elementos em posições pares (maçã e laranja)
print(frutas[::-1])  # Inverte a lista (uva, laranja, banana, maçã)
print(frutas[1:3][0])  # Acessa o primeiro elemento da fatia (banana)
print(frutas[1:3][1])  # Acessa o segundo elemento da fatia (laranja)
print(frutas[1:3][0:1])  # Acessa o primeiro elemento da fatia (banana)
print(frutas[1:3][0:2])  # Acessa os dois primeiros elementos da fatia (banana e laranja)
print(frutas[1:3][0:3])  # Acessa os três primeiros elementos da fatia (banana e laranja)
print(frutas[1:3][0:4])  # Acessa os quatro primeiros elementos da fatia (banana e laranja)
print(frutas[1:3][0:5])  # Acessa os cinco primeiros elementos da fatia (banana e laranja)
print(frutas[1:3][0:6])  # Acessa os seis primeiros elementos da fatia (banana e laranja)
print(frutas[1:3][0:7])  # Acessa os sete primeiros elementos da fatia (banana e laranja)
print(frutas[1:3][0:8])  # Acessa os oito primeiros elementos da fatia (banana e laranja)
print(frutas[1:3][0:9])  # Acessa os nove primeiros elementos da fatia (banana e laranja)
print(frutas[1:3][0:10])  # Acessa os dez primeiros elementos da fatia (banana e laranja)


# Adicionando elementos à lista

frutas.append("abacaxi")  # Adiciona "abacaxi" ao final da lista
frutas.insert(2, "kiwi")  # Insere "kiwi" na posição 2 (antes de laranja)

print(frutas)  # Exibe a lista atualizada

numeros = [12, 34, 56, 78, 90]  # Criando uma lista de números
pares = [numero for numero in numeros if numero % 2 == 0]  # Filtrando números pares

print(pares)  # Exibe a lista de números pares