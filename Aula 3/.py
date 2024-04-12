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