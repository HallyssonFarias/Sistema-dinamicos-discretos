from sympy import symbols, Eq, solve
import numpy as np

## Se quiser compor outra função substitua as variáveis "expr_" na linha 11 e substituir o segundo argumento na linha 25 ##

# Define a variável da função
x = symbols('x')

# Define o valor de r
r = float(input("escolha o valor de r: "))
expr_ = r*x*(1-x)

# Somente para ter um retorno e checar que está correto o valor escolhido
print("A função: ", expr_)
print(" ")

# Escolhe a quantidade de composições/iterações
quantidade = int(input("Escolha a quantidade de composições: "))
print(" ")

# Parte do código que faz a composição
k = 0
while k < quantidade:

    expr = expr_.subs(x, r*x*(1-x))
    expr_ = expr
    print(k+1," composição")
    print(expr_)
    print(" ")
    k = k +1
