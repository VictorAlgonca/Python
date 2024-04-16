print(52*'*')
print(5*'*','OlÃ¡, seja muito bem-vindo a Frutaria ES!',5*'*')
print(52*'*')
print()
# Input do usuÃ¡rio

nome = input('Para comeÃ§armos, por favor, diga o seu nome: ')
endereco = input(f'{nome}, diga o seu endereÃ§o: ')
ano = int(input(f'{nome}, diga o ano do seu nascimento: '))
idade = 2024 - ano
# Mostrar o cardÃ¡pio de frutas

#msg='''
#---------------------
#|Fruta     | R$/kg  |
#---------------------
#|Banana    |  10.50 |
#|Uva       |   3.50 |
#|MaÃ§Ã£      |   8.50 |
#|Melancia  |  20.50 |
#|Kiwi      |  35.40 |
#---------------------
#'''
banana = 10.5
uva = 3.5
maca = 8.5
melancia = 20.5
kiwi = 35.40

print()
print(f'{nome}, as opÃ§Ãµes de fruta do dia, sÃ£o: ')

print(42*'-')
print('|', 'Id','|', f'{"Fruta":15s}', '|', f'{"R$/kg":15s}','|')
print(42*'-')
print('|',' 1', '|', f'{"Banana":15s}', '|', f'{banana:15.2f}','|')
print('|',' 2','|', f'{"Uva":15s}', '|', f'{uva:15.2f}','|')
print('|',' 3','|', f'{"MaÃ§Ã£":15s}', '|', f'{maca:15.2f}','|')
print('|',' 4','|', f'{"Melancia":15s}', '|', f'{melancia:15.2f}','|')
print('|',' 5','|', f'{"Kiwi":15s}', '|', f'{kiwi:15.2f}','|')
print(42*'-')

id = input('Escolha o Id da fruta que vocÃª deseja: ')
peso = float(input('Qual Ã© a quantidade (em kg) que vocÃª deseja? '))

var = True
if id == '1':
    valor = peso*banana
elif id == '2':
    valor = peso*uva
elif id == '3':
    valor = peso*maca
elif id == '4':
    valor = peso*melancia
elif id == '5':
    valor = peso*kiwi
else:
    print('Escolha invÃ¡lida!')
    var = False


if var == True:
    frete = 4
    if valor < 15:
        valor = valor + frete
    else:
        print(f'{nome}, vocÃª estÃ¡ isento(a) do frete!')


    #print(valor)

    if idade > 60:
        print(f'{nome}, o(a) Sr(a), tem um desconto de 5%.')
        valor = valor * 0.95

    print()
    print(f'Muito obrigado, {nome}, sua compra ficou no valor de R${valor:.2f} e serÃ¡ entregue no enderÃ§o: {endereco}.')