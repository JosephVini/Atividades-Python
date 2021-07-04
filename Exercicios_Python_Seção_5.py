"""
# Questão 1
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > num2:
    print(num1, 'É o maior numero')
else:
    print(num2, 'É o maior numero')

# Questão 2
num = float(input('Digite um numero: '))
if num > 0:
    raiz = num ** 0.5
    print(f'\nA raiz quadrada de {num} é {raiz}\n')
else:
    print('Numero digitado é invalido.')

# Questão 3
num = float(input('Digite um numero: '))
if num > 0:
    raiz = num ** 0.5
    print(f'\nA raiz quadrada de {num} é {raiz}\n')
else:
    print(f'\nO numero elevado ao quadrado é {num ** 2}.\n')

# Questão 4
num = float(input('Digite um numero: '))
if num > 0:
    print(f'\nO numero elevado ao quadrado é {num ** 2}.\n')
    print(f'\n a raiz quadrada de {num} é {num ** 0.5}\n')

# Questão 5
num = int(input('Digite um numero:'))
if num % 2 == 0:
    print(f'\n o numero {num} é par.')
elif num % 2 == 1:
    print(f'\n o numero {num} é impar')

# Questão 6
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > num2:
    print(f'\n o numero {num1} é maior que {num2} e a diferença deles é {num1 - num2}\n')
else:
    print(f'\n o numero {num2} é maior que {num1} e a diferença deles é {num2 - num1}\n')

# Questão 7
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > num2:
    print(f'\n O numero {num1} é maior que {num2}.\n')
elif num1 == num2:
    print('O numeros são iguais.')
else:
    print(f'\nO numero {num2} é maior que {num1}\n')

# Questão 8
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
if 0 > nota1 or nota1 > 10:
    print('Uma das notas é invalida.')
elif 0 > nota2 or nota2 > 10:
    print('Uma das notas é invalida.')
else:
    print(f"\n A media das duas notas é: {(nota1 + nota2) / 2}\n")

# Questão 9
salario = float(input('Digite o valor do salario: '))
parcela = float(input('Digite o valor das parcelas: '))
porcetentagem = salario * 20 / 100
if parcela > porcetentagem:
    print('Emprestimo não concedido')
else:
    print('Emprestimo concedido')

# Questão 10
altura = float(input('Digite a sua altura: '))
sexo = str(input('Digite o seu sexo: ').title())
if sexo == "Homem":
    print(f'\n O seu peso ideal é {(72.7 * altura) - 58} kg.')
elif sexo == "Mulher":
    print(f'\n O seu peso ideal é {(62.1 * altura) - 44.7} kg.')

# Questão 11
num = int(input('Digite o um numero maior que zero: '))
soma = 0
if num <= 0:
    print('Numero invalido.')
while num > 0:
    soma += num % 10
    num = num // 10
print(f'\n A soma dos algorismos é igual a {soma}\n')

# Questão 12
import math
base = 10
num = int(input('Digite um numero: '))
if num < 0:
    print('Numero inválido')
else:
    log = math.log(num, base)
    print(f'\nO logaritimo de {num} é igual a {log}\n')

# Questão 13
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
media = nota1 * 1 + nota2 * 1 + nota3 * 2
media = media / 1+1+2
print(f'A média do aluno é {media}.')
if media >= 6.0:
    print('O aluno foi aprovado.')
else:
    print('O aluno foi reprovado')

# Questão 14
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
if nota1 < 0 or nota2 < 0 or nota3 < 0:
    print('O valor de uma das notas é invalida.')
elif nota1 > 10 or nota2 > 10 or nota3 > 10:
    print('O valor de uma das notas é invalida.')
else:
    media = nota1 * 2 + nota2 * 3 + nota3 * 5
    media = media / (2 + 3 + 5)
    print(f'A média do aluno é {media}.')
    if media < 3:
        print('O aluno foi reprovado.')
    elif media < 5:
        print('O aluno esta em recuperção.')
    else:
        print('O aluno foi aprovado.')

# Questão 15
num = int(input('Digite um numero de 1 a 7 para saber o dia da semana: '))
if num == 1:
    print('Domingo')
elif num == 2:
    print('Segunda-Feira')
elif num == 3:
    print('Terça-Feira')
elif num == 4:
    print('Quarta-Feira')
elif num == 5:
    print('Quinta-Feira')
elif num == 6:
    print('Sexta-Feira')
elif num == 7:
    print('Sabado')
else:
    print('Numero invalido')

# Questão 16
num = int(input('Digite um numero de 1 a 12 para saber o mês: '))
if num == 1:
    print('Janeiro')
elif num == 2:
    print('Fevereiro')
elif num == 3:
    print('Março')
elif num == 4:
    print('Abril')
elif num == 5:
    print('Maio')
elif num == 6:
    print('Junho')
elif num == 7:
    print('Julho')
elif num == 8:
    print('Agosto')
elif num == 9:
    print('Setembro')
elif num == 10:
    print('Outubro')
elif num == 11:
    print('Novembro')
elif num == 12:
    print('Dezembro')
else:
    print('Numero invalido')

# Questão 17
basemaior = float(input('Digite o valor da base maior do trapezio: '))
basemenor = float(input('Digite o valor da base menor do trapezio: '))
altura = float(input('Digite o valor da altura do trapezio: '))
if basemaior <= 0 or basemenor <= 0:
    print('Um das bases tem um valor invalido')
area = (basemaior + basemenor) * altura
area = area / 2
print(f'O valor da área do trapezio é igual á {area}')

# Questão 18
operacao = input('Digite o nome da operação basica que quer fazer: ')
num1 = float(input('Digite o primeiro valor da operação: '))
num2 = float(input('Digite o segundo valor da operação: '))
if operacao == 'soma':
    valor = num1 + num2
    print(f'O valor da operação de soma é igual á {valor}')
elif operacao == 'subtração' or operacao == 'diferença':
    valor = num1 - num2
    print(f'O valor da operação de subtração é igual á {valor}')
elif operacao == 'multiplicação':
    valor = num1 * num2
    print(f'O valor da operação de multiplicação é igual á {valor}')
elif operacao == 'divisão':
    valor = num1 / num2
    print(f'O valor da operação de divisão é igual á {valor}')
else:
    print('Valor digitado em operação invalido.')

# Questão 19
num = int(input('Digite um numero: '))
if num % 3 == 0 and num % 5 == 0:
    print('Numero divisivel por 5 e por 3.')
elif num % 3 == 0:
    print('Numero divisivel por 3.')
elif num % 5 == 0:
    print('Numero divisivel por 5.')
else:
    print('Numero não divisivel nem por 5 e nem por 3.')

# Questão 20
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))
if valor1 > valor2 + valor3:
    print('Não é um triangulo.')
elif valor2 > valor1 + valor3:
    print('Não é um triangulo.')
elif valor3 > valor2 + valor1:
    print('Não é um triangulo.')
else:
    if valor1 == valor2 and valor1 == valor3:
        print('É um triangulo equilatero.')
    elif valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
        print('É um triangulo isóceles.')
    elif valor1 != valor2 and valor1 != valor3 and valor2 != valor3:
        print('É um triangulo escaleno.')

# Questão 21
print('1 - Soma de dois valores.')
print('2 - Diferença entre dois numeros.')
print('3 - Produto entre dois numeros.')
print('4 - Divisão entre dois numeros.')
opcao = int(input('Digite um numero de 1 a 4 para escolher as opções: '))
if opcao == 1:
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    soma = valor1 + valor2
    print(f'A soma dos dois valores é {soma}')
elif opcao == 2:
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    if valor1 > valor2:
        subt = valor1 - valor2
    else:
        subt = valor2 - valor1
    print(f'A subtração dos valores é {subt}')
elif opcao == 3:
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    produto = valor1 * valor2
    print(f'O produto entre os dois valores é {produto}')
elif opcao == 4:
    valor1 = float(input('Digite o valor do numerador valor: '))
    valor2 = float(input('Digite o valor do denominador valor: '))
    if valor2 == 0:
        print('O denominador tem valor 0. valor invalido')
    else:
        divisao = valor1 / valor2
        print(f'O resultado da divisão é igual á {divisao}')
else:
    print('Valor da opção invalido.')

# Questão 22
idade = int(input('Digite a idade que você tem: '))
tempoServico = int(input('Digite o tempo de serviço que você tem: '))
if idade >= 65 or tempoServico >= 30:
    print('Você já pode se aposentar.')
elif idade >= 60 and tempoServico >= 25:
    print('Você já pode se aposentar.')
else:
    print('Você ainda não pode se aposentar.')

# Questão 23
ano = int(input('Digite o ano para saber se ele é bissexto ou não: '))
if ano % 4 == 0 and ano % 100 != 0:
    print('É um ano bissexto.')
elif ano % 400 == 0 and ano % 100 != 0:
    print('É um ano bissexto.')
else:
    print('Não é um ano bissexto.')

# Questão 24
estado = input('Digite a sigla para o estado de destino: ').upper()
valor = float(input('Digite o valor para o produto: '))
valorfinal = 0
if estado == 'MG':
    valorfinal = valor * 7 / 100
    valorfinal = valorfinal + valor
elif estado == 'SP':
    valorfinal = valor * 12 / 100
    valorfinal = valorfinal + valor
elif estado == 'RJ':
    valorfinal = valor * 15 / 100
    valorfinal = valorfinal + valor
elif estado == 'MS':
    valorfinal = valor * 8 / 100
    valorfinal = valorfinal + valor
else:
    print('ERRO. A sigla digitada não corresponde aos Estados disponiveis.')
print(f'O valor final do produto no estado {estado} é igual á {valorfinal}')

# Questão 25
a = int(input("Digite o valor de 'a': "))
b = int(input("Digite o valor de 'b': "))
c = int(input("Digite o valor de 'c': "))
if a == 0:
    print('Não é uma equação do segundo grau.')
else:
    delta = b*b - 4 * a * c
    if delta < 0:
        print('Não existe real.')
    elif delta == 0:
        x = -b + delta ** 0.5
        x = x / 2 * a
        print(f'Raiz unica: {x}')
    elif delta >= 0:
        x1 = -b + delta ** 0.5
        x1 = x1 / 2 * a
        x2 = -b - delta ** 0.5
        x2 = x2 / 2 * a
        print(f'Existem duas Raizes: x1 = {x1} e x2 = {x2}.')

# Questão 26
km = float(input('Digite quantos kilometros foram percorridos: '))
litros = float(input('Digite a quantidade de gasilina que foi gasta: '))
if km / litros < 8:
    print('Venda o carro')
elif 8 < km / litros > 14:
    print('Econômico.')
elif km / litros > 12:
    print('Super econômico.')

# Questão 27
idade = int(input('Digite a idade do nadador: '))
if 5 <= idade <= 7:
    print('Infantil A')
elif 8 <= idade <= 10:
    print('Infantil B')
elif 11 <= idade <= 13:
    print('Juvenil A')
elif 14 <= idade <= 17:
    print('Juvenil B')
elif idade > 18:
    print('Sênior')

# Questão 28
print('a - Geométrica')
print('b - Ponderada')
print('c - Harmônica')
print('d - Aritmética')
letra = input("Escolha uma letra de 'a' a 'd' para escolher uma das medias: ")
valorx = int(input("Digite um valor para 'x': "))
valory = int(input("Digite um valor para 'y': "))
valorz = int(input("Digite um valor para 'z': "))
resultado = 0
if letra == 'a':
    resultado = valorx * valory * valorz
    resultado = resultado ** (1/3)
    print(f'O resultado da média Geométrica é {resultado}')
elif letra == 'b':
    resultado = valorx + 2 * valory + 3 * valorz
    resultado = resultado / 6
    print(f'O resultado da média Ponderada é {resultado}')
elif letra == 'c':
    resultado = 1/valorx + 1/valory + 1/valorz
    resultado = 1 / resultado
    print(f'O resultado da média Harmônica é {resultado}')
elif letra == 'd':
    resultado = valorx + valory + valorz
    resultado = resultado / 3
    print(f'O resultado da média Aritmética é {resultado}')
else:
    print('Opção invalida, por favor selecione outra letra.')

# Questão 29
import random
acertos = 0
for perguntas in range(5):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    resposta = int(input(f'Qual é a resposta da soma entre {a} + {b}: '))
    if resposta == a + b:
        acertos += 1
    print(f' A resposta entre a soma de {a} e {b} é {a + b}')
print(f'Você acertou {acertos}')

# Questão 30
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite outro numero: '))
maior = 0
medio = 0
minimo = 0
if num2 < num1 > num3:
    maior = num1
    if num2 > num3:
        medio = num2
        minimo = num3
    elif num3 > num2:
        medio = num3
        minimo = num2
elif num1 < num2 > num3:
    maior = num2
    if num1 > num3:
        medio = num1
        minimo = num3
    elif num3 > num1:
        maior = num3
        minimo = num1
else:
    maior = num3
    if num1 > num2:
        medio = num1
        minimo = num2
    elif num2 > num1:
        medio = num2
        minimo = num1
print(f'A ordem crescente destes valores é: {minimo}, {medio} e {maior} ')

# Questão 31
altura = int(input('Digite a sua altura em centimetro: '))
peso = float(input('Digite o seu peso: '))
if altura <= 120 and peso <= 60:
    print("A sua classificação é: A")
elif 120 < altura <= 170 and peso <= 60:
    print('A sua classificação é: B')
elif altura > 170 and peso <= 60:
    print('A sua classificação é: C')
elif altura < 120 and 60 < peso <= 90:
    print('A sua classificação é: D')
elif 120 < altura <= 170 and 60 < peso <= 90:
    print('A sua classificação é: E')
elif altura > 170 and 60 < peso <= 90:
    print('A sua classificação é: F')
elif altura < 120 and peso > 90:
    print('A sua classificação é: G')
elif 120 < altura <= 170 and peso > 90:
    print('A sua classificação é: H')
elif altura > 170 and peso > 90:
    print('A sua classificação é: I')

# Questão 32
print('Especificações - Código - Preço')
print('Cachorro Quente - 100 - R$ 1.20')
print('Bauru Simples - 101 - R$ 1.30')
print('Bauru com Ovo - 102 - R$ 1.50')
print('Hamburguer - 103 - R$ 1.20')
print('Cheeseburguer - 104 - R$ 1.70')
print('Suco - 105 - R$ 2.20')
print('Refrigerante - 106 - R$ 1.00')
print('Digite 0 para finalizar o pedido.')
pedido = True
calcular = 0
while pedido != 0:
    pedido = int(input('Digite o código do pedido: '))
    if pedido == 100:
        quantidade = int(input('Digite a quantidade do pedido: '))
        calcular += 1.20 * quantidade
    elif pedido == 101:
        quantidade = int(input('Digite a quantidade do pedido: '))
        calcular += 1.30 * quantidade
    elif pedido == 102:
        quantidade = int(input('Digite a quantidade do pedido: '))
        calcular += 1.50 * quantidade
    elif pedido == 103:
        quantidade = int(input('Digite a quantidade do pedido: '))
        calcular += 1.20 * quantidade
    elif pedido == 104:
        quantidade = int(input('Digite a quantidade do pedido: '))
        calcular += 1.70 * quantidade
    elif pedido == 105:
        quantidade = int(input('Digite a quantidade do pedido: '))
        calcular += 2.20 * quantidade
    elif pedido == 106:
        quantidade = int(input('Digite a quantidade do pedido: '))
        calcular += 1.00 * quantidade
    elif pedido == 0:
        break
print(f'O valor final do pedido é R$ {float(calcular):.2f} ')

# Questão 33
preco_antigo = float(input('Digite o PREÇO ANTIGO: '))
preco_novo = 0
if preco_antigo <= 50.00:
    preco_novo = preco_antigo * 5 / 100
    preco_novo = preco_novo + preco_antigo
elif preco_antigo <= 100:
    preco_novo = preco_antigo * 10 / 100
    preco_novo = preco_novo + preco_antigo
elif preco_antigo > 100:
    preco_novo = preco_antigo * 15 / 100
    preco_novo = preco_novo + preco_antigo

if preco_novo <= 80:
    print('Barato')
elif preco_novo <= 120:
    print('Normal')
elif preco_novo <= 200:
    print('Caro')
elif preco_novo > 200:
    print('Muito Caro')

# Questão 34
nota = float(input('Digite a nota do aluno: '))
faltas = int(input('Digite o numero de faltas do aluno: '))
if 9.0 <= nota <= 10.0 and faltas <= 20:
    print('O conceito deste aluno é: A')
elif 9.0 <= nota <= 10.0 and faltas >= 20:
    print('O conceito deste aluno é: B')
elif 7.5 <= nota <= 8.9 and faltas <= 20:
    print('O conceito deste aluno é: B')
elif 7.5 <= nota <= 8.9 and faltas >= 20:
    print('O conceito deste aluno é: C')
elif 5.0 <= nota <= 7.4 and faltas <= 20:
    print('O conceito deste aluno é: C')
elif 5.0 <= nota <= 7.4 and faltas >= 20:
    print('O conceito deste aluno é: D')
elif 4 <= nota <= 4.9 and faltas <= 20:
    print('O conceito deste aluno é: D')
elif 4 <= nota <= 4.9 and faltas >= 20:
    print('O conceito deste aluno é: E')
elif nota <= 3.9 and faltas <= 20:
    print('O conceito deste aluno é: E')
elif nota <= 3.9 and faltas >= 20:
    print('O conceito deste aluno é: E')

# Questão 1
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > num2:
    print(num1, 'É o maior numero')
else:
    print(num2, 'É o maior numero')

# Questão 2
num = float(input('Digite um numero: '))
if num > 0:
    raiz = num ** 0.5
    print(f'\nA raiz quadrada de {num} é {raiz}\n')
else:
    print('Numero digitado é invalido.')

# Questão 3
num = float(input('Digite um numero: '))
if num > 0:
    raiz = num ** 0.5
    print(f'\nA raiz quadrada de {num} é {raiz}\n')
else:
    print(f'\nO numero elevado ao quadrado é {num ** 2}.\n')

# Questão 4
num = float(input('Digite um numero: '))
if num > 0:
    print(f'\nO numero elevado ao quadrado é {num ** 2}.\n')
    print(f'\n a raiz quadrada de {num} é {num ** 0.5}\n')

# Questão 5
num = int(input('Digite um numero:'))
if num % 2 == 0:
    print(f'\n o numero {num} é par.')
elif num % 2 == 1:
    print(f'\n o numero {num} é impar')

# Questão 6
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > num2:
    print(f'\n o numero {num1} é maior que {num2} e a diferença deles é {num1 - num2}\n')
else:
    print(f'\n o numero {num2} é maior que {num1} e a diferença deles é {num2 - num1}\n')

# Questão 7
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > num2:
    print(f'\n O numero {num1} é maior que {num2}.\n')
elif num1 == num2:
    print('O numeros são iguais.')
else:
    print(f'\nO numero {num2} é maior que {num1}\n')

# Questão 8
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
if 0 > nota1 or nota1 > 10:
    print('Uma das notas é invalida.')
elif 0 > nota2 or nota2 > 10:
    print('Uma das notas é invalida.')
else:
    print(f"\n A media das duas notas é: {(nota1 + nota2) / 2}\n")

# Questão 9
salario = float(input('Digite o valor do salario: '))
parcela = float(input('Digite o valor das parcelas: '))
porcetentagem = salario * 20 / 100
if parcela > porcetentagem:
    print('Emprestimo não concedido')
else:
    print('Emprestimo concedido')

# Questão 10
altura = float(input('Digite a sua altura: '))
sexo = str(input('Digite o seu sexo: ').title())
if sexo == "Homem":
    print(f'\n O seu peso ideal é {(72.7 * altura) - 58} kg.')
elif sexo == "Mulher":
    print(f'\n O seu peso ideal é {(62.1 * altura) - 44.7} kg.')

# Questão 11
num = int(input('Digite o um numero maior que zero: '))
soma = 0
if num <= 0:
    print('Numero invalido.')
while num > 0:
    soma += num % 10
    num = num // 10
print(f'\n A soma dos algorismos é igual a {soma}\n')

# Questão 12
import math
base = 10
num = int(input('Digite um numero: '))
if num < 0:
    print('Numero inválido')
else:
    log = math.log(num, base)
    print(f'\nO logaritimo de {num} é igual a {log}\n')

# Questão 13
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
media = nota1 * 1 + nota2 * 1 + nota3 * 2
media = media / 1+1+2
print(f'A média do aluno é {media}.')
if media >= 6.0:
    print('O aluno foi aprovado.')
else:
    print('O aluno foi reprovado')

# Questão 14
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
if nota1 < 0 or nota2 < 0 or nota3 < 0:
    print('O valor de uma das notas é invalida.')
elif nota1 > 10 or nota2 > 10 or nota3 > 10:
    print('O valor de uma das notas é invalida.')
else:
    media = nota1 * 2 + nota2 * 3 + nota3 * 5
    media = media / (2 + 3 + 5)
    print(f'A média do aluno é {media}.')
    if media < 3:
        print('O aluno foi reprovado.')
    elif media < 5:
        print('O aluno esta em recuperção.')
    else:
        print('O aluno foi aprovado.')

# Questão 15
num = int(input('Digite um numero de 1 a 7 para saber o dia da semana: '))
if num == 1:
    print('Domingo')
elif num == 2:
    print('Segunda-Feira')
elif num == 3:
    print('Terça-Feira')
elif num == 4:
    print('Quarta-Feira')
elif num == 5:
    print('Quinta-Feira')
elif num == 6:
    print('Sexta-Feira')
elif num == 7:
    print('Sabado')
else:
    print('Numero invalido')

# Questão 16
num = int(input('Digite um numero de 1 a 12 para saber o mês: '))
if num == 1:
    print('Janeiro')
elif num == 2:
    print('Fevereiro')
elif num == 3:
    print('Março')
elif num == 4:
    print('Abril')
elif num == 5:
    print('Maio')
elif num == 6:
    print('Junho')
elif num == 7:
    print('Julho')
elif num == 8:
    print('Agosto')
elif num == 9:
    print('Setembro')
elif num == 10:
    print('Outubro')
elif num == 11:
    print('Novembro')
elif num == 12:
    print('Dezembro')
else:
    print('Numero invalido')

# Questão 17
basemaior = float(input('Digite o valor da base maior do trapezio: '))
basemenor = float(input('Digite o valor da base menor do trapezio: '))
altura = float(input('Digite o valor da altura do trapezio: '))
if basemaior <= 0 or basemenor <= 0:
    print('Um das bases tem um valor invalido')
area = (basemaior + basemenor) * altura
area = area / 2
print(f'O valor da área do trapezio é igual á {area}')

# Questão 18
operacao = input('Digite o nome da operação basica que quer fazer: ')
num1 = float(input('Digite o primeiro valor da operação: '))
num2 = float(input('Digite o segundo valor da operação: '))
if operacao == 'soma':
    valor = num1 + num2
    print(f'O valor da operação de soma é igual á {valor}')
elif operacao == 'subtração' or operacao == 'diferença':
    valor = num1 - num2
    print(f'O valor da operação de subtração é igual á {valor}')
elif operacao == 'multiplicação':
    valor = num1 * num2
    print(f'O valor da operação de multiplicação é igual á {valor}')
elif operacao == 'divisão':
    valor = num1 / num2
    print(f'O valor da operação de divisão é igual á {valor}')
else:
    print('Valor digitado em operação invalido.')

# Questão 19
num = int(input('Digite um numero: '))
if num % 3 == 0 and num % 5 == 0:
    print('Numero divisivel por 5 e por 3.')
elif num % 3 == 0:
    print('Numero divisivel por 3.')
elif num % 5 == 0:
    print('Numero divisivel por 5.')
else:
    print('Numero não divisivel nem por 5 e nem por 3.')

# Questão 20
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))
if valor1 > valor2 + valor3:
    print('Não é um triangulo.')
elif valor2 > valor1 + valor3:
    print('Não é um triangulo.')
elif valor3 > valor2 + valor1:
    print('Não é um triangulo.')
else:
    if valor1 == valor2 and valor1 == valor3:
        print('É um triangulo equilatero.')
    elif valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
        print('É um triangulo isóceles.')
    elif valor1 != valor2 and valor1 != valor3 and valor2 != valor3:
        print('É um triangulo escaleno.')

# Questão 21
print('1 - Soma de dois valores.')
print('2 - Diferença entre dois numeros.')
print('3 - Produto entre dois numeros.')
print('4 - Divisão entre dois numeros.')
opcao = int(input('Digite um numero de 1 a 4 para escolher as opções: '))
if opcao == 1:
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    soma = valor1 + valor2
    print(f'A soma dos dois valores é {soma}')
elif opcao == 2:
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    if valor1 > valor2:
        subt = valor1 - valor2
    else:
        subt = valor2 - valor1
    print(f'A subtração dos valores é {subt}')
elif opcao == 3:
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    produto = valor1 * valor2
    print(f'O produto entre os dois valores é {produto}')
elif opcao == 4:
    valor1 = float(input('Digite o valor do numerador valor: '))
    valor2 = float(input('Digite o valor do denominador valor: '))
    if valor2 == 0:
        print('O denominador tem valor 0. valor invalido')
    else:
        divisao = valor1 / valor2
        print(f'O resultado da divisão é igual á {divisao}')
else:
    print('Valor da opção invalido.')

# Questão 22
idade = int(input('Digite a idade que você tem: '))
tempoServico = int(input('Digite o tempo de serviço que você tem: '))
if idade >= 65 or tempoServico >= 30:
    print('Você já pode se aposentar.')
elif idade >= 60 and tempoServico >= 25:
    print('Você já pode se aposentar.')
else:
    print('Você ainda não pode se aposentar.')

# Questão 23
ano = int(input('Digite o ano para saber se ele é bissexto ou não: '))
if ano % 4 == 0 and ano % 100 != 0:
    print('É um ano bissexto.')
elif ano % 400 == 0 and ano % 100 != 0:
    print('É um ano bissexto.')
else:
    print('Não é um ano bissexto.')

# Questão 24
estado = input('Digite a sigla para o estado de destino: ').upper()
valor = float(input('Digite o valor para o produto: '))
valorfinal = 0
if estado == 'MG':
    valorfinal = valor * 7 / 100
    valorfinal = valorfinal + valor
elif estado == 'SP':
    valorfinal = valor * 12 / 100
    valorfinal = valorfinal + valor
elif estado == 'RJ':
    valorfinal = valor * 15 / 100
    valorfinal = valorfinal + valor
elif estado == 'MS':
    valorfinal = valor * 8 / 100
    valorfinal = valorfinal + valor
else:
    print('ERRO. A sigla digitada não corresponde aos Estados disponiveis.')
print(f'O valor final do produto no estado {estado} é igual á {valorfinal}')

# Questão 25
a = int(input("Digite o valor de 'a': "))
b = int(input("Digite o valor de 'b': "))
c = int(input("Digite o valor de 'c': "))
if a == 0:
    print('Não é uma equação do segundo grau.')
else:
    delta = b*b - 4 * a * c
    if delta < 0:
        print('Não existe real.')
    elif delta == 0:
        x = -b + delta ** 0.5
        x = x / 2 * a
        print(f'Raiz unica: {x}')
    elif delta >= 0:
        x1 = -b + delta ** 0.5
        x1 = x1 / 2 * a
        x2 = -b - delta ** 0.5
        x2 = x2 / 2 * a
        print(f'Existem duas Raizes: x1 = {x1} e x2 = {x2}.')

# Questão 26
km = float(input('Digite quantos kilometros foram percorridos: '))
litros = float(input('Digite a quantidade de gasilina que foi gasta: '))
if km / litros < 8:
    print('Venda o carro')
elif 8 < km / litros > 14:
    print('Econômico.')
elif km / litros > 12:
    print('Super econômico.')

# Questão 27
idade = int(input('Digite a idade do nadador: '))
if 5 <= idade <= 7:
    print('Infantil A')
elif 8 <= idade <= 10:
    print('Infantil B')
elif 11 <= idade <= 13:
    print('Juvenil A')
elif 14 <= idade <= 17:
    print('Juvenil B')
elif idade > 18:
    print('Sênior')

# Questão 28
print('a - Geométrica')
print('b - Ponderada')
print('c - Harmônica')
print('d - Aritmética')
letra = input("Escolha uma letra de 'a' a 'd' para escolher uma das medias: ")
valorx = int(input("Digite um valor para 'x': "))
valory = int(input("Digite um valor para 'y': "))
valorz = int(input("Digite um valor para 'z': "))
resultado = 0
if letra == 'a':
    resultado = valorx * valory * valorz
    resultado = resultado ** (1/3)
    print(f'O resultado da média Geométrica é {resultado}')
elif letra == 'b':
    resultado = valorx + 2 * valory + 3 * valorz
    resultado = resultado / 6
    print(f'O resultado da média Ponderada é {resultado}')
elif letra == 'c':
    resultado = 1/valorx + 1/valory + 1/valorz
    resultado = 1 / resultado
    print(f'O resultado da média Harmônica é {resultado}')
elif letra == 'd':
    resultado = valorx + valory + valorz
    resultado = resultado / 3
    print(f'O resultado da média Aritmética é {resultado}')
else:
    print('Opção invalida, por favor selecione outra letra.')

# Questão 29
import random
acertos = 0
for perguntas in range(5):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    resposta = int(input(f'Qual é a resposta da soma entre {a} + {b}: '))
    if resposta == a + b:
        acertos += 1
    print(f' A resposta entre a soma de {a} e {b} é {a + b}')
print(f'Você acertou {acertos}')

# Questão 30
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite outro numero: '))
maior = 0
medio = 0
minimo = 0
if num2 < num1 > num3:
    maior = num1
    if num2 > num3:
        medio = num2
        minimo = num3
    elif num3 > num2:
        medio = num3
        minimo = num2
elif num1 < num2 > num3:
    maior = num2
    if num1 > num3:
        medio = num1
        minimo = num3
    elif num3 > num1:
        maior = num3
        minimo = num1
else:
    maior = num3
    if num1 > num2:
        medio = num1
        minimo = num2
    elif num2 > num1:
        medio = num2
        minimo = num1
print(f'A ordem crescente destes valores é: {minimo}, {medio} e {maior} ')

# Questão 31
altura = int(input('Digite a sua altura em centimetro: '))
peso = float(input('Digite o seu peso: '))
if altura <= 120 and peso <= 60:
    print("A sua classificação é: A")
elif 120 < altura <= 170 and peso <= 60:
    print('A sua classificação é: B')
elif altura > 170 and peso <= 60:
    print('A sua classificação é: C')
elif altura < 120 and 60 < peso <= 90:
    print('A sua classificação é: D')
elif 120 < altura <= 170 and 60 < peso <= 90:
    print('A sua classificação é: E')
elif altura > 170 and 60 < peso <= 90:
    print('A sua classificação é: F')
elif altura < 120 and peso > 90:
    print('A sua classificação é: G')
elif 120 < altura <= 170 and peso > 90:
    print('A sua classificação é: H')
elif altura > 170 and peso > 90:
    print('A sua classificação é: I')

# Questão 32
print('Especificações - Código - Preço')
print('Cachorro Quente - 100 - R$ 1.20')
print('Bauru Simples - 101 - R$ 1.30')
print('Bauru com Ovo - 102 - R$ 1.50')
print('Hamburguer - 103 - R$ 1.20')
print('Cheeseburguer - 104 - R$ 1.70')
print('Suco - 105 - R$ 2.20')
print('Refrigerante - 106 - R$ 1.00')
print('Digite 0 para finalizar o pedido.')
pedido = True
calcular = 0
while pedido != 0:
    pedido = int(input('Digite o código do pedido: '))
    if pedido == 100:
        quantidade = int(input('Digite a quantidade do pedido: '))
        calcular += 1.20 * quantidade
    elif pedido == 101:
        quantidade = int(input('Digite a quantidade do pedido: '))
        calcular += 1.30 * quantidade
    elif pedido == 102:
        quantidade = int(input('Digite a quantidade do pedido: '))
        calcular += 1.50 * quantidade
    elif pedido == 103:
        quantidade = int(input('Digite a quantidade do pedido: '))
        calcular += 1.20 * quantidade
    elif pedido == 104:
        quantidade = int(input('Digite a quantidade do pedido: '))
        calcular += 1.70 * quantidade
    elif pedido == 105:
        quantidade = int(input('Digite a quantidade do pedido: '))
        calcular += 2.20 * quantidade
    elif pedido == 106:
        quantidade = int(input('Digite a quantidade do pedido: '))
        calcular += 1.00 * quantidade
    elif pedido == 0:
        break
print(f'O valor final do pedido é R$ {float(calcular):.2f} ')

# Questão 33
preco_antigo = float(input('Digite o PREÇO ANTIGO: '))
preco_novo = 0
if preco_antigo <= 50.00:
    preco_novo = preco_antigo * 5 / 100
    preco_novo = preco_novo + preco_antigo
elif preco_antigo <= 100:
    preco_novo = preco_antigo * 10 / 100
    preco_novo = preco_novo + preco_antigo
elif preco_antigo > 100:
    preco_novo = preco_antigo * 15 / 100
    preco_novo = preco_novo + preco_antigo

if preco_novo <= 80:
    print('Barato')
elif preco_novo <= 120:
    print('Normal')
elif preco_novo <= 200:
    print('Caro')
elif preco_novo > 200:
    print('Muito Caro')

# Questão 34
nota = float(input('Digite a nota do aluno: '))
faltas = int(input('Digite o numero de faltas do aluno: '))
if 9.0 <= nota <= 10.0 and faltas <= 20:
    print('O conceito deste aluno é: A')
elif 9.0 <= nota <= 10.0 and faltas >= 20:
    print('O conceito deste aluno é: B')
elif 7.5 <= nota <= 8.9 and faltas <= 20:
    print('O conceito deste aluno é: B')
elif 7.5 <= nota <= 8.9 and faltas >= 20:
    print('O conceito deste aluno é: C')
elif 5.0 <= nota <= 7.4 and faltas <= 20:
    print('O conceito deste aluno é: C')
elif 5.0 <= nota <= 7.4 and faltas >= 20:
    print('O conceito deste aluno é: D')
elif 4 <= nota <= 4.9 and faltas <= 20:
    print('O conceito deste aluno é: D')
elif 4 <= nota <= 4.9 and faltas >= 20:
    print('O conceito deste aluno é: E')
elif nota <= 3.9 and faltas <= 20:
    print('O conceito deste aluno é: E')
elif nota <= 3.9 and faltas >= 20:
    print('O conceito deste aluno é: E')

# Questão 35
dia = int(input('Digite um numero de 1 a 31 para o dia: '))
mes = int(input('Digite um numero de 1 a 12 para o mês: '))
ano = int(input('Digite um numero para o ano: '))
valido = False
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31:
        valido = True
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30:
        valido = True
elif mes == 2:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 and ano % 100 != 0:
        if dia <= 29:
            valido = True
        elif dia <= 28:
            valido = True
if valido:
    print('Esta data é valida.')
else:
    print('Esta data não é valida.')

# Questão 36
venda = float(input('Digite o valor da venda: '))
porcentagem = 0
if venda >= 100_000:
    porcentagem = venda * 16
    porcentagem = porcentagem / 100
    comissao = porcentagem + 700
elif 80_000 <= venda < 100_000:
    porcentagem = venda * 14
    porcentagem = porcentagem / 100
    comissao = porcentagem + 650
elif 60_000 <= venda < 80_000:
    porcentagem = venda * 14
    porcentagem = porcentagem / 100
    comissao = porcentagem + 600
elif 40_000 <= venda < 60_000:
    porcentagem = venda * 14
    porcentagem = porcentagem / 100
    comissao = porcentagem + 550
elif 20_000 <= venda < 40_000:
    porcentagem = venda * 14
    porcentagem = porcentagem / 100
    comissao = porcentagem + 500
elif 20_000 > venda:
    porcentagem = venda * 14
    porcentagem = porcentagem / 100
    comissao = porcentagem + 400
print(f'A comissão do vendedor é R$ {comissao}')

# Questão 37
Não sei fazer

# Questão 38
dia = int(input('Digite um numero de 1 a 31 para o dia: '))
mes = int(input('Digite um numero de 1 a 12 para o mês: '))
ano = int(input('Digite um numero para o ano: '))
valido = False
if ano <= 2021:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia <= 31:
            valido = True
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia <= 30:
            valido = True
    elif mes == 2:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 and ano % 100 != 0:
            if dia <= 29:
                valido = True
            elif dia <= 28:
                valido = True
if valido:
    print('Esta data é valida.')
else:
    print('Esta data não é valida.')

# Questão 39
salario = float(input('Digite o valor do salario atual: '))
tempo_servico = int(input('Digite o tempo de serviço: '))
if salario <= 500 and tempo_servico < 1:
    salario_final = salario * 25
    salario_final = salario_final / 100
    salario_final = salario_final + salario
    bonus = 'Sem Bônus'
elif salario <= 1000 and tempo_servico <= 3:
    salario_final = salario * 20
    salario_final = salario_final / 100
    salario_final = salario_final + salario
    bonus = 'R$ 100'
elif salario <= 15000 and tempo_servico <= 6:
    salario_final = salario * 15
    salario_final = salario_final / 100
    salario_final = salario_final + salario
    bonus = 'R$ 200'
elif salario <= 2000 and tempo_servico <= 10:
    salario_final = salario * 10
    salario_final = salario_final / 100
    salario_final = salario_final + salario
    bonus = 'R$ 300'
elif salario > 2000 and tempo_servico > 10:
    salario_final = salario
    bonus = 'R$ 500'
print(f'O salario final é de R${salario_final} com o bonus de {bonus}')

# Questão 40
custo_fabrica = float(input('Digite o custo de fabrica do veiculo: '))
if custo_fabrica <= 12_000:
    percentual = custo_fabrica * 5
    percentual = percentual / 100
    custo_final = custo_fabrica + percentual
elif custo_fabrica <= 25_000:
    percentual = custo_fabrica * (10 + 15)
    percentual = percentual / 100
    custo_final = custo_fabrica + percentual
elif custo_fabrica > 25_000:
    percentual = custo_fabrica * (15 + 20)
    percentual = percentual / 100
    custo_final = custo_fabrica + percentual
print(f'O custo final que o consumidor pagará é de R$ {custo_final}')

# Questão 41
imc = float(input('Digite o IMC: '))
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 24.9:
    print('Saudável')
elif imc <= 29.9:
    print('Peso em excesso')
elif imc <= 34.9:
    print('Obesidade Grau 1')
elif imc <= 39.9:
    print('Obesidade Grau 2 (severa)')
elif imc > 40:
    print('Obesidade Grau 3 (mórbida)')
"""
# Questão 11
num = int(input('Digite o um numero maior que zero: '))
soma = 0
if num <= 0:
    print('Numero invalido.')
while num > 0:
    soma += num % 100
    num = num // 100
print(f'\n A soma dos algorismos é igual a {soma}\n')