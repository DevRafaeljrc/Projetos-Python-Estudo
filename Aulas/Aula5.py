# Aprender a converter os tipos de variáveis

# int -> float
a = 10
b = float(a)
print(a, type(a))  # 10 <class 'int'>
print(b, type(b))  # 10.0 <class 'float'>       

# float -> int
a = 10.5
b = int(a)
print(a, type(a))  # 10.5 <class 'float'>
print(b, type(b))  # 10 <class 'int'>

# str -> int
a = '10'
b = int(a)
print(a, type(a))  # 10 <class 'str'>
print(b, type(b))  # 10 <class 'int'>

# str -> float
a = '10.5'
b = float(a)
print(a, type(a))  # 10.5 <class 'str'>
print(b, type(b))  # 10.5 <class 'float'>

# int -> str
a = 10
b = str(a)
print(a, type(a))  # 10 <class 'int'>
print(b, type(b))  # 10 <class 'str'>

# float -> str
a = 10.5
b = str(a)
print(a, type(a))  # 10.5 <class 'float'>
print(b, type(b))  # 10.5 <class 'str'>

# str -> bool
a = 'True'
b = bool(a)
print(a, type(a))  # True <class 'str'>
print(b, type(b))  # True <class 'bool'>

# int -> bool
a = 10
b = bool(a)
print(a, type(a))  # 10 <class 'int'>
print(b, type(b))  # True <class 'bool'>

# float -> bool
a = 10.5
b = bool(a)
print(a, type(a))  # 10.5 <class 'float'>
print(b, type(b))  # True <class 'bool'>

# bool -> int
a = True
b = int(a)
print(a, type(a))  # True <class 'bool'>
print(b, type(b))  # 1 <class 'int'>

# bool -> float
a = True
b = float(a)
print(a, type(a))  # True <class 'bool'>
print(b, type(b))  # 1.0 <class 'float'>

# bool -> str
a = True
b = str(a)
print(a, type(a))  # True <class 'bool'>
print(b, type(b))  # True <class 'str'>

