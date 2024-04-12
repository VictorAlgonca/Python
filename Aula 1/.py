a = 4
b = -20
c = 24

delta = (b**2) - (4 * a * c)

x1 = (- b + (delta** 0.5))/ (2 * a)

x2 = (- b - (delta ** 0.5))/ (2 * a)

print("as raizes são" ,x1, "e" , x2)


a = 1.500

promocao = (15/100) * a

final = a + promocao

print("O aumento de 15 % no final é de " , final)


a1 = 10

a1, b1 = 3 *a1 , a1

print(a1, b1)

#colocar a em b e b em a
# metodo nao recomendado
a2 = 10
b2 = 20

a2, b2 = b2 , a2
print(a2, b2)

#metodo recomendado

a3 = 45
b3 = 30
aux = a3
a3 = b3
b3 = aux
print(a3, b3)

seuNome = input("Digite seu nome")
suaidade = input("Digite sua idade")
print("Olá, meu nome é",seuNome, "e tenho", suaidade, "anos")

dias1 = int(input("quantidade de dias"))
horas1 = int(input("quantidade de horas"))
minutos1 = int(input("quantidade de minutos"))
segundos1 = int(input("quantidade de segundos"))

segundos_totais = dias1*24*6060 + horas1 *60*60 + minutos1*60 + segundos1
print('a quantidade de segundos é ', segundos_totais)

v = int(input("Velocidade que o carro estava "))
v1 = int(input("Valor que não pode passar "))
multa = 100
acrescimo = (v - v1) * 5
if v > v1:
    print("Você tomou uma multa")
    print("a multa é de ", multa , "e tem um acrescimo de ", acrescimo)
else:
    print("Você nao tomou multa")

valorA = int(input("Diga o primeiro valor"))

valorB = int(input("Diga o segundo valor"))

if valorA > valorB:
    print(valorA)
else:
    print(valorB)

valor2 = int(input("Escreva o valor que quer verificar"))

if valor2 % 2 == 0 :
    print("Esse numero é par")