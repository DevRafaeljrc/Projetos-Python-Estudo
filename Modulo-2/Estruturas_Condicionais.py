# Estruturas condicionais em Python

# Exemplo básico de if, elif e else
idade = 20

if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você tem exatamente 18 anos.")
else:
    print("Você é maior de idade.")

# If aninhados
nota = 85

if nota >= 60:
    if nota >= 90:
        print("Parabéns! Você tirou uma nota excelente.")
    else:
        print("Você passou, mas pode melhorar.")
else:
    print("Infelizmente, você não passou.")

# If ternário (expressão condicional em uma linha)
numero = 10
resultado = "Par" if numero % 2 == 0 else "Ímpar"
print(f"O número {numero} é {resultado}.")

# Explicação:
# 1. `if` avalia uma condição e executa o bloco de código se for verdadeira.
# 2. `elif` permite adicionar condições adicionais.
# 3. `else` executa um bloco de código se nenhuma das condições anteriores for verdadeira.
# 4. If aninhados são usados para verificar condições dentro de outras condições.
# 5. If ternário é uma forma compacta de escrever uma estrutura condicional simples.