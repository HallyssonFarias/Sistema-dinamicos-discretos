from sympy import *

# Define a variável simbólica
x = symbols('x')

# Print da função logística
print("A função é: f(x) = r*x*(1-x)")

# Define os valores das variáveis
r = float(input("Escolha o r: "))
xo = float(input("Escolha o valor inicial de x: "))
print(" ")

# Define a opção de iterações
opcao = int(input("Opção 1: 0 < n < 4 \nOpção 2: de A até B \nEscolha sua opção: "))
print(" ")

# Define a função
funcao = r*x*(1-x)
print("Função polinomial, f(x):\n", funcao)

# Calcula a derivada
derivada = diff(funcao, x)
print("Derivada, f'(x):\n", derivada)
print(" ")

# Converte as expressões simbolicas em expressões numéricas
f = lambdify(x, funcao)
df = lambdify(x, derivada)

# print so para deixar claro as iterações
print("As iterações são: \n ")

# Função


def newton_raphson(f, df, xo, iteracao, opcao, a):
    x_ = xo
    for i in range(1, iteracao + 1):
        x_ = x_ - f(x_) / df(x_)
        if opcao == 1 and i <= 4:
            print(f"Iteração {i}: \n {x_}")
        elif opcao == 2 and i >= a:
            print(f"Iteração {i}: \n {x_}")
    return x_


# opcões
if opcao == 1:
    newton_raphson(f, df, xo, 4, opcao, 0)
elif opcao == 2:
    a = int(input("de: "))
    b = int(input("até: "))
    newton_raphson(f, df, xo, b, opcao, a)
