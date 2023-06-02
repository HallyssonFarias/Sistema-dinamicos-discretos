from sympy import symbols, Eq, solve
import numpy as np

# Define a variável simbólica x
x = symbols('x')

# Define a função f(x) substitua pela a qual queira achar o ponto fixo
f = (4.1**(2))*4.1*x*(1-x)*(1-4.1*x*(1-x))*(1-4.1*4.1*x*(1-x)*(1- 4.1*x*(1-x)))

# Resolve a equação f(x) = x para encontrar o ponto fixo
eq = Eq(f, x)
ponto_fixo = solve(eq, x)

#print dos resultados
print(ponto_fixo)

