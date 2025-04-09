# Em Python, strings de múltiplas linhas podem ser criadas usando aspas triplas (simples ou duplas).

# Exemplo 1: String de múltiplas linhas com aspas triplas duplas
texto1 = """Este é um exemplo
de uma string
com múltiplas linhas."""

print(texto1)

# Exemplo 2: String de múltiplas linhas com aspas triplas simples
texto2 = '''Você também pode usar
aspas simples triplas
para criar strings de múltiplas linhas.'''

print(texto2)

# Exemplo 3: String de múltiplas linhas com quebra de linha explícita
texto3 = "Se preferir, você pode usar\n" \
         "quebras de linha explícitas\n" \
         "com o caractere de nova linha '\\n'."

print(texto3)

# Observação:
# Strings de múltiplas linhas são úteis para armazenar textos longos, como mensagens, documentos ou código formatado.
# Elas preservam quebras de linha e espaços exatamente como estão no código.

# Exemplo 4: String de múltiplas linhas com f-strings
nome = "João"
idade = 30
cidade = "São Paulo"

texto4 = f"""Olá, meu nome é {nome}.
Eu tenho {idade} anos.
Eu moro em {cidade}."""

print(texto4)