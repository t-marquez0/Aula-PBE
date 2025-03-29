'''
#01
nome = "João"
print(nome)

#02
a = 5
b = 10
soma = a + b
print(a + b)
print(a - b)
print(a * b)
print(a / b)

#03
preco = 50
desconto = 10
resultado = preco - desconto
print(resultado)

#04
resultado = 10 + 5 * 2
print(resultado)

#05
texto = "150"
texto = int(texto)
resultado = texto * 2
print(resultado)

#07
a = input("Digite um número:")
b = input("Digite outro número:")
print(a + b)


#08
x = int(input("Digite um número:"))
y = int(input("Digite outro número:"))
print(x//y)

#09
num1 = input("Digite um número:")
num2 = input("Digite outro número:")
print("O primeiro número é maior que o segundo?", num1 > num2)

#10
idade = int(input("Digite sua idade:"))
dias = idade * 365
print("Você viveu", dias, "dias")


#11
base = int(input("Digite a base:"))
expoente = int(input("Digite o expoente:"))
potencia = base ** expoente
print(potencia)


#12
preco = float(input("Digite o preço: "))
resultado = "O preço é: " + str(preco)
print(resultado)


#13
raio = float(input("Digite o valor do raio: "))
area = 3.14 * raio**2
print("A área do círculo é:", area)


#14
a = input("Digite um número:")
b = input("Digite outro número:")
a, b = b, a
print(a, b)


#15
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
p1 = 2
p2 = 3
p3 = 5
mediapond = (nota1*p1 + nota2*p2 + nota3*p3) / (p1 + p2 + p3)
print("A média ponderada é:", mediapond)


#desafio
x1 = float(input("Digite a coordenada de x1:"))
y1 = float(input("Digite a coordenada de y1:"))
x2 = float(input("Digite a coordenada de x2:"))
y2 = float(input("Digite a coordenada de y2:"))
euclidiana = ((x2-x1)**2 + (y2-y1)**2)**0.5
print(euclidiana)
'''
