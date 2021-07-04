"""
# Questão 1
for multiplo in range(3, 16, 3):
    print(multiplo)

# Questão 2 (Faltou o do while)
for vezes in range(3):
    for numero in range(1, 101):
        print(numero, '- ', end='')
    print(f'numero de vezes é {vezes + 1}')

for vezes in range(3):
    num = 1
    while num < 101:
        print(num, '- ', end='')
        num = num + 1
    print('Numero de vezes do while', vezes + 1)

# Questão 3
num = 10
while num > -1:
    print(num)
    num = num - 1
print('FIM')

# Questão 4
num = 0
while num < 100_100:
    print(num)
    num = num + 1000

# Questão 5
valor = 0
for vezes in range(10):
    num = int(input('Digite um valor: '))
    valor = valor + num
print('A soma dos valores é igual á', valor)

# Questão 6
valor = 0
for i in range(10):
    num = int(input('Digite um numero inteiro: '))
    valor = num + valor
media = valor / 10
print(f'\nA média das notas é igual á {media}\n')

# Questão 7
valor = 0
cont = 0
for i in range(10):
    num = int(input('Digite um numero inteiro: '))
    if num > 0:
        valor = num + valor
        cont = cont + 1
media = valor / cont
print(f'\nA média dos valores é igual á {media}')

# Questão 8
num = int(input('Digite um valor: '))
valorMenor = num
valorMaior = num
for vezes in range(9):
    num = int(input('Digite outro valor: '))
    if valorMaior < num:
        valorMaior = num
    elif valorMenor > num:
        valorMenor = num
print(f'\n O menor valor digitado é {valorMenor} e o maior valor digitdo é {valorMaior}\n')

# Questão 9
num = int(input('Digite um valor: '))
impar = 1
for i in range(num):
    print(impar)
    impar = impar + 2

# Questão 10
par = 0
for i in range(50):
    par = par + 2
print('A soma dos 50 primeiros numeros pares é', par)

# Questão 11
num = int(input('Digite um numero maior que 0: '))
if num <= 0:
    print('valor invalido')
else:
    for i in range(num + 1):
        print(i, ' ', end='')

# Questão 13
num = int(input('Digite um numero maior que 0 e que seja par: '))
if num % 2 != 0:
    print('valor invalido')
else:
    for i in range(num + 1):
        if i % 2 == 0:
            print(i, ' ', end='')

# Questão 14
num = int(input('Digite um numero maior que 0 e que seja par: '))
lista = []
if num % 2 != 0:
    print('valor invalido')
else:
    for i in range(num + 1):
        if i % 2 == 0:
            lista.append(i)
    print(lista[::-1])

# Questão 15
num = int(input('Digite um numero maior que 0 e que seja impar: '))
lista = []
if num % 2 == 0:
    print('valor invalido')
else:
    for i in range(num + 1):
        if i % 2 != 0:
            lista.append(i)
    print(lista)

# Questão 16
num = int(input('Digite um numero maior que 0 e que seja impar: '))
lista = []
if num % 2 == 0:
    print('valor invalido')
else:
    for i in range(num + 1):
        if i % 2 != 0:
            lista.append(i)
    print(lista[::-1])

# Questão 17
n = int(input('Digite um numero para N: '))
soma = 0
for i in range(n):
    soma = soma + i
print(f'A soma dos {n} primeiros numeros é igual á {soma}')

# Questão 18
numeros = int(input('Digite a quantidades de numeros a serem lidos: '))
cont = 0
num = 0
for vezes in range(numeros):
    outro = int(input('Digite um numero: '))
    if outro > num:
        num = outro
        cont = 1
    elif num == outro:
        cont += 1
print(f'O maior numero digitado foi {num} e ele foi digitado {cont} vezes.')

# Questão 19
numero = int(input('Digite um numero entre 100 e 999: '))
if numero < 100 or numero > 999:
    print('Numero invalido')
while numero > 0:
    alg = numero % 10
    numero = numero // 10
    print(f'O numero é composto pelos algarismo {alg}')

# Questão 20
 não sei fazer

# Questão 21
num1 = int(input('Digite o primeiro valor a ser calculado: '))
num2 = int(input('Digite o segundo valor a ser calculado: '))
listapar = []
listaimpar = []
for numero in range(num1, num2+1):
    if numero % 2 == 0:
        listapar.append(numero)
    elif numero % 2 != 0:
        listaimpar.append(numero)
multi = 1
for numero in listaimpar:
    multi *= numero

print(f'A soma dos numeros pares deste invervalo é: {sum(listapar)}')
print(f'A multiplicação dos numeros impares é: {multi}')

# Questão 22
num = int(input('Digite um valor dentro do intervalo de 10 a 20: '))
cont = 1
media = 0 + num
while 10 < num < 20:
    num = int(input('Digite outro valor dentro do intervalo de 10 a 20: '))
    if 10 < num < 20:
        media += num
        cont += 1
media = media / cont
print(f'A media das notas é {media}')

# Questão 23
num = int(input('Digite um numero maior que 1: '))
divisor = 2
elevado = 0
if num < 0:
    print('Numero invalido.')
else:
    while num > 1:
        while num % divisor == 0:
            elevado += 1
            num = num / divisor
        if elevado > 0:
            print(f'O divisor é igual á: {divisor} elevado á {elevado}.')
        while num % divisor != 0:
            if num == 1:
                break
            divisor += 1
            elevado = 0

# Questão 24
num = int(input('Digite um numero maior que 1: '))
divisor = 1
lista = []
if num < 0:
    print('Numero invalido.')
else:
    while num != divisor:
        while num % divisor == 0:
            if divisor != num:
                lista.append(divisor)
                divisor += 1
        while num % divisor != 0:
            divisor += 1
print(f'Os numero divisores são {lista} e a soma destes numeros são {sum(lista)}')

# Questão 25
num = 0
soma = 0
while num < 1000:
    if num % 3 == 0:
        soma += num
        num += 1
    elif num % 5 == 0:
        soma += num
        num += 1
    else:
        num += 1
print(f'A soma dos numeros multiplos de 3 e 5 abaixo de 1000 é {soma}')

# Questão 26
num = int(input('Digite um numero maior que 0: '))
multi = 0
while num != 0:
    if num % 11 == 0:
        print(f'O primeiro numero multiplo de 11 é {num}')
        break
    elif num % 13 == 0:
        print(f'O primeiro numero multiplo de 13 é {num}')
        break
    elif num % 17 == 0:
        print(f'O primeiro multiplo de 17 é {num}')
        break
    else:
        num += 1

# Questão 27
num = int(input('Digite um numero inteiro positivo: '))
harmonica = 0
for H in range(1, num + 1):
    harmonica += 1 / H
print(f'A soma da série harmonica é {harmonica}')

# Questão 28
num = int(input('Digite um numero inteiro e positivo: '))
resultado = 0
fatorial = 1
for N in range(1, num + 1):
    fatorial *= N
    resultado += 1 / fatorial
print(f'O resultado final é {resultado}')

# Questão 29
num = 5
resultado = 0
fatorial = 1
for N in range(1, num + 1):
    fatorial *= N
    resultado += N / fatorial
print(f'O resultado é {resultado}')

# Questão 30
Não sei

# Questão 31
resultado = 1
cima = 1
baixo = 1
for i in range(49):
    cima += 2
    baixo += 1
    resultado += cima / baixo
print(f'O valor de S é igual á: {resultado}')

# Questão 32
from random import randint
vezes = int(input('Digite quantas vezes vai jogar o dado: '))
for i in range(vezes):
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    if d1 > d2:
        print(f'O resultado do dado 1 é {d1} é maior que o dado 2 que é {d2} na {i + 1}º vez.')
    elif d1 < d2:
        print(f'O resultado do dado 1 é {d1} que é menor do que do dado 2 que é {d2} na {i + 1}º vez.')
    else:
        print(f'A saida do dado 1 que é {d1} é igual á do dado 2 que é {d2} na {i + 1}º vez.')

# Questão 33
n = int(input('Digite um numero para N: '))
i = int(input("Digite um numero maior que 0 para 'i': "))
j = int(input("Digite um numero maior que 0 para 'j': "))
numeros = 0
multiplos = []
while len(multiplos) < n:
    if numeros % i == 0 or numeros % j == 0:
        multiplos.append(numeros)
    numeros += 1
print(f'Os {n} multiplos de {i} e {j} são {multiplos}')

# Questão 34
não sei

# Questão 35
inicial = int(input('Digite o valor inicial do intervalo: '))
final = int(input('Digite o valor final do intervalo: '))
soma = 0
if inicial > final:
    print('Intervalo dos valores invalidos.')
else:
    for intervalo in range(inicial, final + 1):
        if intervalo % 2 != 0:
            soma += intervalo
    print(f'A soma dos valores impares neste intervalo é {soma}')

# Questão 36
soma_dos_quadrados = 0
quadrado_da_soma = 0
for i in range(1, 101):
    soma_dos_quadrados += i ** 2
    quadrado_da_soma += i
quadrado_da_soma = quadrado_da_soma ** 2
diferenca = quadrado_da_soma - soma_dos_quadrados
print(f'A diferença entre a soma dos quadrados e o quadrado da soma é: {diferenca}')

# Questão 37
numeros = []
for i in range(1_000, 10_000):
    soma = 0
    soma += i % 100
    num = i // 100
    soma += num
    quadrado = soma ** 2
    if quadrado == i:
        numeros.append(i)
print(f'Os numero que possuem essa propriedade são: {numeros}')

# Questão 38
não sei

# Questão 39
base = float(input('Digite o numero da base do triângulo: '))
altura = float(input('Digite a altura do triângulo: '))
if altura <=0 or base <=0:
    print('Dados invalidos.')
else:
    area = base * altura
    area = area / 2
    print(f'A área do triângulo é {area}')

# Questão 40
lista = []
num = 0
while num >= 0:
    num = int(input('Digite um numero: '))
    if num >= 0:
        lista.append(num)
print(f'O maior numero é {max(lista)} e o menor numero é {min(lista)}')

# Questão 41
resultado = True
while resultado != 0:
    resistor1 = float(input('Digite um valor para o resistor 1: '))
    resistor2 = float(input('Digite um valor para o resistor 2: '))
    resultado = (resistor1 * resistor2) / (resistor1 + resistor2)

# Questão 42


def quadrado(numero):
    return numero ** 2


def cubo(numero):
    return numero ** 3


def raiz(numero):
    return numero ** 0.5


lista_quadrada = []
lista_cubo = []
lista_raiz = []
valor = True
while valor > 0:
    valor = int(input('Digite um numero: '))
    if valor > 0:
        lista_quadrada.append(quadrado(valor))
        lista_cubo.append(cubo(valor))
        lista_raiz.append(raiz(valor))
print(f' A lista dos numero ao quadrado: {lista_quadrada}')
print(f' A lista dos numeros ao cubo: {lista_cubo}')
print(f' A lista das raizes quadradas dos numeros: {lista_raiz} ')

# Questão 43
idades = []
idade = True
while idade > 0:
    idade = int(input('Digite a sua idade: '))
    if idade > 0:
        idades.append(idade)
media = sum(idades) / len(idades)
print(f'A média das idades é: {media}')

# Questão 44
fibonace = 0
ultimo = 1
penultimo = 0
numero = int(input('Digite um numero: '))
print(fibonace)
while fibonace < numero:
    fibonace = ultimo + penultimo
    penultimo = ultimo
    ultimo = fibonace
    print(fibonace)
print(fibonace)

# Questão 45
opcao = True
while opcao == 1 or opcao == 2:
    print('Converter para kilometros por Hora - 1')
    print('Converter para Metros por Segundo - 2')
    print('Finalizar - 0')
    print()
    opcao = int(input('Digite o numero da operação desejada: '))
    if opcao == 1:
        metros_por_segundo = float(input('Digite a velocidade em m/s: '))
        kilometros_por_hora = metros_por_segundo * 3.6
        print(f'A velocidade é {kilometros_por_hora} Km/H')
        print()
    elif opcao == 2:
        kilometros_por_hora = float(input('Digite a velocidade em km/h: '))
        metros_por_segundo = kilometros_por_hora / 3.6
        print(f'A velocidade é {metros_por_segundo} m/s')
        print()

# Questão 46
from random import randint
numero_aleatorio = randint(1, 1000)
usuario = True
vezes = 0
nummaior = 1000
nummenor = 1
while usuario != numero_aleatorio:
    usuario = int(input(f'Digite um numero entre {nummenor} e {nummaior}: '))
    if usuario == numero_aleatorio:
        vezes += 1
        print('Parábens você acertou o numero aleátorio.')
    elif usuario < numero_aleatorio:
        vezes += 1
        print('Você errou tente de novo.')
        nummenor = usuario
    elif usuario > numero_aleatorio:
        vezes += 1
        print('Você errou tente de novo.')
        nummaior = usuario
print(f'A quantidade de tentativas foi {vezes}')

# Questão 47
opcao = True
while opcao < 5:
    print('adição (opção 1)')
    print('subtração (opção 2)')
    print('multiplicação (opção 3)')
    print('divisão (opção 4)')
    print('saida (opção 5)')
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite outro numero: '))
        print(f'A soma dos numeros é {num1 + num2}')
        print()
    elif opcao == 2:
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite outro numero: '))
        print(f'A subtração dos numeros é {num1 - num2}')
        print()
    elif opcao == 3:
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite outro numero: '))
        print(f'A multiplicação dos numeros é {num1 * num2}')
        print()
    elif opcao == 4:
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite outro numero: '))
        print(f'A divisão dos numeros é {num1 / num2}')
        print()

# Questão 48  (Não sei se ta certo)
fibonace = 0
ultimo = 1
penultimo = 0
numero = 4_000_000
soma = 0
while fibonace < numero:
    print(fibonace)
    fibonace = ultimo + penultimo
    penultimo = ultimo
    ultimo = fibonace
    if fibonace % 2 == 0:
        soma += fibonace
print(f'A soma dos valores pares é {soma}')

# Questão 49
não sei

# Questão 50
chico = 1.50
ze = 1.10
anos = 0
while ze < chico:
    chico += 0.2
    ze += 0.3
    anos += 1
print(f'Levará {anos} anos para que Zé fique maior do que Chico, com Zé tendo {ze:.2f} metros e Chico com {chico:.2f} '
      f'metros.')

# Questão 51 (Não sei se estar certo)
salario = 2000
ano = 1996
porcentagem = 1.5 / 100
aumento = 0
while ano < 2021:
    if ano == 1996:
        aumento = porcentagem * salario
        salario += aumento
        ano += 1
    elif ano >= 1997:
        aumento *= 2
        salario += aumento
print(f'O salario atual será de R${salario:.2f} no ano de {ano}')

# Questão 52
valor = int(input('Digite o valor que quer sacar: '))
if valor < 0:
    print('Valor digitado invalido.')
else:
    notas100 = int(valor / 100)
    if notas100 > 0:
        print(notas100, 'notas de R$100,00')
    valor = valor % 100
    notas50 = int(valor / 50)
    if notas50 > 0:
        print(notas50, 'notas de R$50,00')
    valor = valor % 50
    notas20 = int(valor / 20)
    if notas20 > 0:
        print(notas20, 'notas de R$20,00')
    valor = valor % 20
    notas10 = int(valor / 10)
    if notas10 > 0:
        print(notas10, 'notas de R$10,00')
    valor = valor % 10
    notas5 = int(valor / 5)
    if notas5 > 0:
        print(notas5, 'notas de R$5,00')
    valor = valor % 5
    notas2 = int(valor / 2)
    if notas2 > 0:
        print(notas2, 'notas de R$2,00')
    valor = valor % 2
    notas1 = int(valor / 1)
    if notas1 > 0:
        print(notas1, 'notas de R$1,00')
"""
# Questão 53