from sympy import symbols

# Se quiser compor outra função substitua as variáveis "expr_" na linha 10 e substituir o segundo argumento na linha 22

# Define a variável da função
x = symbols('x')

# Define o valor de r
r = float(input("Escolha o valor de r: "))
expr_ = r*x*(1-x)

# Somente para ter um retorno e checar que está correto o valor escolhido
print("A função: ", expr_)
print(" ")

# Escolhe a quantidade de composições/iterações
quantidade = int(input("Escolha a quantidade de composições: "))
print(" ")

# Loop que faz a composição
for k in range(1, quantidade + 1):
    expr = expr_.subs(x, r*x*(1-x))
    expr_ = expr
    print(f"{k}º composição: \n{expr_}")
    print(" ")
