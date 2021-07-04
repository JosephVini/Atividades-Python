"""
# Questão 1
def dobro(num):
    return num * 2


numero = int(input('Digite um numero: '))
print(f'O dobro de {numero} é {dobro(numero)}')

# Questão 2

def data(dia, mes, ano):
    if 0 < dia <= 31:
        if mes == 1:
            print(f'{dia} de janeiro de {ano}.')
        elif mes == 2:
            if dia <= 29:
                print(f'{dia} de fervereiro de {ano}.')
            else:
                print('dia invalido.')
        elif mes == 3:
            print(f'{dia} de março de {ano}.')
        elif mes == 4:
            print(f'{dia} de abril de {ano}.')
        elif mes == 5:
            print(f'{dia} de maio de {ano}.')
        elif mes == 6:
            print(f'{dia} de junho de {ano}.')
        elif mes == 7:
            print(f'{dia} de julho de {ano}.')
        elif mes == 8:
            print(f'{dia} de agosto de {ano}.')
        elif mes == 9:
            print(f'{dia} de setembro de {ano}.')
        elif mes == 10:
            print(f'{dia} de outubro de {ano}.')
        elif mes == 11:
            print(f'{dia} de novembro de {ano}.')
        elif mes == 12:
            print(f'{dia} de dezembro de {ano}.')
        else:
            print('Mês invalido.')
    else:
        print('Dia invalido.')


num_dia = int(input('Digite o dia: '))
num_mes = int(input('Digite o mês: '))
num_ano = int(input('Digite o ano: '))
data(num_dia, num_mes, num_ano)

# Questão 3

def negativo(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0


numero = int(input('Digite um numero: '))
print(f'O numero é {negativo(numero)}')

# Questão 4

def quadrado_perfeito(numero):
    raiz = int(numero ** (1 / 2))
    if raiz ** 2 == numero:
        print(f'O numero {numero} é um quadrado perfeito de {raiz}.')
    else:
        print(f'O numero {numero} não é um quadrado perfeito.')


num = int(input('Digite um numero para saber se é um quadrado perfeito: '))
quadrado_perfeito(num)

# Questão 5
import math


def volume_esfera(raio):
    volume = 4/3 * math.pi * raio**3
    return volume


raio_esfera = float(input('Digite o valor do raio da esfera: '))
print(f'O volume da esfera é igual á: {volume_esfera(raio_esfera):.2f} m³')

# Questão 6


def segundos(hora, minutos, segundo):
    minutos += hora * 60
    segundo += minutos * 60
    return segundo


horas = int(input('Digite as horas: '))
minuto = int(input('Digite os minutos: '))
segundo = int(input('Digite os segundos: '))
print(f'O total de segundos são: {segundos(horas, minuto, segundo)} s.')

# Questão 7

def fare(temperatura):
    tempfare = temperatura * (9 / 5) + 32
    return tempfare


celcius = float(input("Digite a temperatura em Celsius: "))
print(f'A temperatura em Fahrenheit é: {fare(celcius)}.')

# Questão 8

def hipoternusa(cateto1, cateto2):
    hipo = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
    return hipo


cate1 = float(input("Digite o valor do cateto 'a': "))
cate2 = float(input("Digite o valor do cateto 'b': "))
print(f'O valor da hipoternusa é {hipoternusa(cate1,cate2)}.')

# Questão 9

def volume_cilindro(altura, raio):
    raio_quadrado = raio ** 2
    volume = 3.141592 * raio_quadrado * altura
    return volume


altura_cilindro = float(input('Digite a altura do cilindro: '))
raio_cilindro = float(input('Digite o raio do cilindro: '))
print(f'O volume do cilindro é igual á: {volume_cilindro(altura_cilindro,raio_cilindro)}.')

# Questão 10

def maior():
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite outro numero: '))
    if num1 > num2:
        return num1
    else:
        return num2


print(f'O maior numero entre os dois digitados é {maior()}')

"""
# Questão 11


def media(nota1, nota2, nota3, opcao):
    if opcao == 'A':
        media_aritmetica = (nota1 + nota2 + nota3) / 3
        return media_aritmetica
    elif opcao == 'P':
        media_ponderada = nota1 * 5 + nota2 * 3 + nota3 * 2
        return media_ponderada
    else:
        print('A opção digitada é invalida')