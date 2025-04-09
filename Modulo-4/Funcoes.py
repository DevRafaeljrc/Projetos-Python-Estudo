# Função simples sem parâmetros
def saudacao():
    """Exibe uma mensagem de saudação."""
    print("Olá! Bem-vindo ao programa.")

# Chamando a função
saudacao()

# Função com parâmetros
def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

# Chamando a função com argumentos
resultado = soma(5, 3)
print(f"A soma é: {resultado}")

# Função com valor padrão
def saudacao_personalizada(nome="Visitante"):
    """Exibe uma saudação personalizada."""
    print(f"Olá, {nome}!")

# Chamando a função com e sem argumento
saudacao_personalizada("Maria")
saudacao_personalizada()

# Função com número variável de argumentos
def listar_itens(*itens):
    """Exibe uma lista de itens."""
    for item in itens:
        print(f"- {item}")

# Chamando a função com múltiplos argumentos
listar_itens("Maçã", "Banana", "Laranja")

# Função com argumentos nomeados
def exibir_dados(nome, idade):
    """Exibe os dados de uma pessoa."""
    print(f"Nome: {nome}, Idade: {idade}")

# Chamando a função com argumentos nomeados
exibir_dados(idade=25, nome="João")