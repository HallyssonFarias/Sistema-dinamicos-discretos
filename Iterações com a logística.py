# OBS: A lista não é usada no código é apenas para facilitar quando quiser visualizar mais facilmente,
# basta somente apagar '#' da frente da última linha

# Printa para mostrar a função logística
print("A funcao é : f(x)= r*x(1-x)+ xo")

# Escolhe as variáveis
r = float(input("escolha o r: "))
x = float(input("escolha o x: "))
xo = float(input("(populacao incial): "))  # Recomenda-se usar, na maioria das vezes, a população inicial igual à 0

# Escolhe a quantidade de casais decimais máximo de 16
decimal = int(input("escolha a quantidade de casas decimais: "))

# Escolhe a quantidade de iterações e também quais iterações que serão printadas
opcao = int(input("opcao 1: 1 até n \nopcao 2: de a até b \nescolha sua opcao: "))

# Parte do código que itera a logística
lista = []
c = 0
if opcao == 1:
    # Essa parte é para a 1 opção de 1 até n
    k = int(input("de 1 até quanto? "))
    while c < k:
        y = r*x*(1-x)+xo
        x = y
        xo = 0
        y = round(y, decimal)
        print(y)
        c = c + 1
        lista.append(x)
else:
    # Essa parte é para a segunda opção de a até b
    a = int(input("de: "))
    b = int(input("até: "))
    while c < b:
        y = r*x*(1-x)+xo
        x = y
        xo = 0
        c = c + 1
        lista.append(x)
        if c >= a:
            y = round(y, decimal)
            print(y)

# print(lista)
