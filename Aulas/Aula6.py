# Funções de entrada e saída

# Função input() - Entrada de dados

# A função input() lê uma linha de texto do usuário e retorna essa linha como uma string.
# O valor retornado pode ser atribuído a uma variável para uso posterior.

# Exemplo de uso da função input()
nome = input("Digite seu nome: ")
print("Olá, " + nome + "!")

# A função input() pode ser usada para ler diferentes tipos de dados, como números inteiros ou flutuantes.
# Para isso, é necessário converter a string retornada pela função input() para o tipo desejado.
# Isso pode ser feito usando as funções int() ou float().
# Exemplo de leitura de um número inteiro
numero_inteiro = int(input("Digite um número inteiro: "))
print("Você digitou o número inteiro:", numero_inteiro)

# A função print() - Saída de dados
# A função print() é usada para exibir dados na tela.
# Ela pode receber vários argumentos, que serão convertidos em strings e exibidos na tela.
# A função print() também pode formatar a saída de dados usando o caractere de formatação % ou o método format().   

# Exemplo de uso da função print()
print("Olá, " + nome + "! Você digitou o número inteiro:", numero_inteiro)
# Exemplo de formatação de strings com o caractere de formatação %  
print("Olá, %s! Você digitou o número inteiro: %d" % (nome, numero_inteiro))
# Exemplo de formatação de strings com o método format()
print("Olá, {}! Você digitou o número inteiro: {}".format(nome, numero_inteiro))
# Exemplo de formatação de strings com f-strings (Python 3.6+)
print(f"Olá, {nome}! Você digitou o número inteiro: {numero_inteiro}")

nome = input("Digite seu nome: ")
print("Olá, " + nome + "!")

