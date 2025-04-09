# Operadores de associação em Python

# Exemplo com listas
frutas = ["maçã", "banana", "laranja"]

print("maçã" in frutas)  # True, porque "maçã" está na lista
print("uva" in frutas)   # False, porque "uva" não está na lista
print("uva" not in frutas)  # True, porque "uva" não está na lista

# Exemplo com strings
texto = "Olá, mundo!"

print("Olá" in texto)  # True, porque "Olá" está na string
print("Python" in texto)  # False, porque "Python" não está na string
print("Python" not in texto)  # True, porque "Python" não está na string

# Exemplo com tuplas
numeros = (1, 2, 3, 4, 5)

print(3 in numeros)  # True, porque 3 está na tupla
print(6 in numeros)  # False, porque 6 não está na tupla