"""
# Questão 1
vetorA = [1, 0, 5, -2, -5, 7]
soma = vetorA[0] + vetorA[1] + vetorA[5]
print(soma)
vetorA[4] = 100
for numero in vetorA:
    print(numero)

# Questão 2
lista = []
for i in range(6):
    valor = int(input('Digite um valor: '))
    lista.append(valor)
print(lista)

# Questão 3
lista1 = []
lista2 = []
for i in range(10):
    num = float(input('Digite um numero: '))
    lista1.append(num)
for i in range(10):
    quadrado = lista1[i] * lista1[i]
    lista2.append(quadrado)
print(lista1)
print(lista2)

# Questão 4
lista = list(range(1, 9))
posicaX = int(input('Digite a posição X: '))
posicaY = int(input('Digite a posição Y: '))
soma = lista[posicaX] + lista[posicaY]
print(f'A soma das posições {lista[posicaX]} + {lista[posicaY]} é igual á: {soma}')

# Questão 5
vetor = list(range(10))
cont = 0
for numero in vetor:
    if numero % 2 == 0:
        cont += 1
print(f'Existe {cont} valores pares.')

# Questão 6
lista = []
for i in range(10):
    num = int(input('Digite um valor: '))
    lista.append(num)
print(f'O menor elemento da lista é {min(lista)}')
print(f'O maior elemento da lista é {max(lista)}')

# Questão 7
lista = []
for i in range(10):
    num = int(input('Digite um numero: '))
    lista.append(num)
print(lista)
print(f'O maior numero é {max(lista)} e esta na posição {lista.index(max(lista))}')

# Questão 8
vetor = []
for i in range(6):
    num = int(input('Digite um numero: '))
    vetor.append(num)
print(vetor[::-1])

# Questão 9
lista = []
while len(lista) < 6:
    num = int(input('Digite um numero par: '))
    if num % 2 != 0:
        print('Numero não é par.')
    else:
        lista.append(num)
print(lista[::-1])

# Questão 10
notas = []
soma = 0
for i in range(15):
    num = float(input('Digite a nota de um aluno: '))
    notas.append(num)
media = sum(notas) / len(notas)
print(f'As notas digitadas foram {notas} e a média delas é {media}')

# Questão 11
vetor = []
soma = 0
cont = 0
for i in range(10):
    num = float(input('Digite um numero: '))
    vetor.append(num)
    if num > 0:
        soma += num
    else:
        cont += 1
print(f'A soma dos numeros positivos é {soma} e o vetor tem {cont} numeros negativos.')

# Questão 12
valores = list(range(1, 6))
print(f'Os valores são {valores} o maior numero é {max(valores)} e o menor numero é {min(valores)} e a média destes'
      f'valores é {sum(valores) / len(valores)}')

# Questão 13
valores = list(range(1, 6))
print(f'O maior valor se encontra na posição {valores.index(max(valores))} e o menor está na posião '
      f' {valores.index(min(valores))}')

# Questão 14
vetor = []
repetidos = []
for i in range(5):
    vetor.append(int(input('Digite um numero: ')))
for valor in vetor:
    if vetor.count(valor) > 1 and valor not in repetidos:
        print(f'O valor {valor} repete na lista {vetor.count(valor)} vezes')
        repetidos.append(valor)

# Questão 15
vetor = []
for i in range(20):
    numero = int(input('Digite um numero: '))
    if numero not in vetor:
        vetor.append(numero)
print(vetor)

# Questão 16
vetor = []
for i in range(5):
    vetor.append(float(input('Digite um numero: ')))
code = True
print('1 - Ordem direta')
print('2 - Ordem inversa')
print('0 - Finalizar')
while code != 0:
    code = int(input('Digite o código do processo: '))
    if code == 1:
        print(vetor)
    elif code == 2:
        print(vetor[::-1])
    elif code == 0:
        break
    elif code != 1 or code != 2:
        print('Código invalido.')

# Questão 17
vetor = []
for i in range(10):
    numero = int(input('Digite um numero: '))
    if numero > 0:
        vetor.append(numero)
    else:
        vetor.append(0)
print(vetor)

# Questão 18
vetor = []
for i in range(10):
    vetor.append(int(input('Digite um numero: ')))
numero = int(input('Digite um numero para verificar os seus multiplos no vetor: '))
multiplo = 0
multiplos = []
for i in range(10):
    if vetor[i] % numero == 0:
        multiplo += 1
        multiplos.append(vetor[i])
print(f'O numero {numero} tem {multiplo} multiplos e são {multiplos}')

# Questão 19
vetor = []
for i in range(50):
    vetor.append((i + 5 * i) %(i + 1))
print(vetor)

# Questão 20
vetor = []
impar = []
for i in range(10):
    numero = int(input('Digite um numero no intervalo de 0 a 50: '))
    if 0 < numero < 50:
        vetor.append(numero)
    if numero % 2 != 0:
        impar.append(numero)
contador = 0
while contador < 10:
    print(f'O vetor é {vetor[contador:contador + 2]}')
    contador += 2
contador = 0
while contador < len(impar):
    print(f'O veotr impar é {impar[contador:contador + 2]}')
    contador += 2

# Questão 21
vetorA = []
vetorB = []
vetorC = []
for i in range(10):
    vetorA.append(int(input('Digite um numero para o vetor A: ')))
for i in range(10):
    vetorB.append(int(input('Digite um numero para o vetor B: ')))
for i in range(10):
    vetorC.append(vetorA[i] - vetorB[i])
print(vetorC)

# Questão 22
vetorA = []
vetorB = []
vetorC = []
for i in range(10):
    vetorA.append(int(input('Digite um numero para o vetor A: ')))
for i in range(10):
    vetorB.append(int(input('Digite um numero para o vetor B: ')))
cont1 = 0
cont2 = 0
for i in range(20):
    if i % 2 == 0:
        vetorC.append(vetorA[cont1])
        cont1 += 1
    else:
        vetorC.append(vetorB[cont2])
        cont2 += 1
print(vetorC)

# Questão 23
conjunto1 = []
conjunto2 = []
escalar = 0
for i in range(5):
    numero = float(input('Digite um numero para o conjunto 1:'))
    conjunto1.append(numero)
for i in range(5):
    numero = float(input('Digite um numero para o conjunto 2:'))
    conjunto2.append(numero)
for i in range(5):
    escalar += conjunto1[i] * conjunto2[i]
print(conjunto1)
print(conjunto2)
print(escalar)

# Questão 24 (Não sei terminar)
nAluno = set({})
altura = set({})
num_min = 0
num_max = 0
for i in range(3):
    numero = int(input('Digite o numero do aluno: '))
    nAluno.add(numero)
    alturaH = float(input('Digite a altura do aluno: '))
    altura.add(alturaH)
    if alturaH < min(altura):
        num_min = numero
    if alturaH > max(altura):
        num_max = numero

print(f'O aluno mais baixo é o de numero {num_min} com altura de {min(altura)} m')
print(f'O aluno mais alto é o de numero {num_max} com altura de {max(altura)} m')

"""
