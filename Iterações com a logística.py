# OBS: Recomenda-se usar, na maioria das vezes, a população inicial igual à 0

# Printa para mostrar a função logística
print("A funcao é : f(x)= r*x(1-x)+ xo")

# Escolhe as variáveis
r = float(input("Escolha o valor de r: "))
x = float(input("Escolha o valor de x: "))
xo = float(input("Escolha o valor da Populacao inicial(xo): "))

# Escolhe a quantidade de casais decimais máximo de 16
decimal = int(input("Escolha a quantidade de casas decimais: "))

# Escolhe a quantidade de iterações e também quais iterações que serão printadas
opcao = int(input("Opcao 1: 1 até n \nOpcao 2: de a até b \nescolha sua opcao: "))

# Funcao que itera a logística


def iteracao(r, x, xo, decimal, opcao, k, a):
    for i in range(k+1):
        y = r*x*(1-x)+xo
        x = y
        xo = 0
        y = round(y, decimal)
        if opcao == 1 and i < k:
            print(f"{i}º iteração: \n {y}")
        elif opcao == 2 and i >= a:
            print(f"{i}º iteração: \n {y}")


# opcoes que chamam a funcao
if opcao == 1:
    k = int(input("De 1 até quanto? "))
    iteracao(r, x, xo, decimal, opcao, k, 0)

elif opcao == 2:
    # Essa parte é para a segunda opcao de a até b
    a = int(input("de: "))
    k = int(input("até: "))
    iteracao(r, x, xo, decimal, opcao, k, a)

