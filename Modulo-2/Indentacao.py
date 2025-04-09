# Exemplo de indentação e blocos em Python

# Função que verifica se um número é par ou ímpar
def verificar_par_ou_impar(numero):
    if numero % 2 == 0:  # Bloco do if
        print(f"{numero} é par.")  # Indentação de 4 espaços
    else:  # Bloco do else
        print(f"{numero} é ímpar.")  # Indentação de 4 espaços

# Chamando a função
verificar_par_ou_impar(10)
verificar_par_ou_impar(7)