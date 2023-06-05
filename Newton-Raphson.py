from sympy import *

# Define a variável simbólica
x = symbols('x')

# Print da função logística
print("A função é: f(x) = r*x*(1-x)")

# Define os valores das variáveis
r = float(input("Escolha o r: "))
k = float(input("Escolha o valor inicial de x: "))
print(" ")

# Define a opção de iterações
opcao = int(input("Opção 1: 0 < n < 4 \nOpção 2: 101 <= n <= 104 \nEscolha sua opção: "))
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


def newton_raphson(f, df, x0, iteracao, opcao):
    x = x0
    for i in range(1, iteracao + 1):
        x = x - f(x) / df(x)
        if opcao == 1 and i <= 4:
            print(f"Iteração {i}: \n {x}")
        elif opcao == 2 and i >= 101 and i <= 104:
            print(f"Iteração {i}: \n {x}")
    return x


# opcões
if opcao == 1:
    newton_raphson(f, df, k, 4, opcao)
elif opcao == 2:
    newton_raphson(f, df, k, 104, opcao)

