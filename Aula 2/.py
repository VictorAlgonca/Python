# 1 hora = 60 minutos ; 60 minutos = 3600 segundos ; 1 minuto = 60 segundos

tempo = int(input("Digite o numero que quer converter em horas, minutos e segundos"))
minuto = tempo// 60 % 60
hora = tempo//3600
segundos = tempo % 60
print(minuto, "minutos" , hora , "horas" , segundos , "segundos")

idade1 = 20
salario1 = 2000

a4 = idade1 >= 18 and salario1 >= 1500

print(a4)

a5 = "hoje tem aula"
print(a5)
print(a5[11])

nome1 = "Diogo"

print(nome1)

print(nome1 [3])

print(len(nome1))