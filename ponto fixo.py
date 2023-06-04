from sympy import symbols, Eq, solve
import numpy as np

# Define a variável simbólica x
x = symbols('x')

# Define a função f(x) substitua pela funcao que deseja achar o ponto fixo
f = 68.921*x*(1 - x)*(-4.1*x*(1 - x) + 1)*(-16.81*x*(1 - x)*(-4.1*x*(1 - x) + 1) + 1)

# Resolve a equação f(x) = x para encontrar o ponto fixo
eq = Eq(f, x)
ponto_fixo = solve(eq, x)

#print dos resultados
print(ponto_fixo)

