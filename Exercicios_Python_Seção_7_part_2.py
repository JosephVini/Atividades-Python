"""
# Questão 1
ordem = 4
cont = 0
lista = []

matriz = []
for i in range(ordem):
    matriz.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        numero = int(input('Digite um numero: '))
        matriz[i][j] = numero
        if numero > 10:
            cont += 1
            lista.append(numero)

print(f'Tem {cont} valores maiores que 10 e são: {lista}')

# Questão 2
ordem = 5

matriz = []
for i in range(ordem):
    matriz.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        if matriz[i] == matriz[j]:
            matriz[i][j] = 1
        else:
            matriz[i][j] = 0

for i in range(ordem):
    for j in range(ordem):
        print(matriz[i][j], ' ', end='')
    print()

# Questão 3
ordem = 4
listalin = []
listacol = []
matriz = []

for i in range(ordem):
    matriz.append([0] * ordem)

for i in range(ordem):
    listalin.append(int(input('Digite um numero para a linha: ')))
for i in range(ordem):
    listacol.append(int(input('Digite um numero para coluna: ')))

for i in range(ordem):
    for j in range(ordem):
        matriz[i][j] = listalin[i] * listacol[j]

for i in range(ordem):
    for j in range(ordem):
        print(matriz[i][j], ' ', end='')
    print()

# Questão 4
ordem = 4
matriz = []
lin = 0
col = 0

for i in range(ordem):
    matriz.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        print(f'Posição da matriz[{i}][{j}]')
        matriz[i][j] = int(input('Digite um numero: '))

maior = matriz[0][0]
for i in range(ordem):
    for j in range(ordem):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            lin = i
            col = j

for i in range(ordem):
    for j in range(ordem):
        print(matriz[i][j], ' ', end='')
    print()

print(f'O maior valor da matriz esta na localização: matriz[{lin}][{col}]')

# Questão 5
ordem = 5
matriz = []
lin = None
col = None
encontrado = None

for i in range(ordem):
    matriz.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        print(f'Posição da matriz[{i}][{j}]')
        matriz[i][j] = int(input('Digite um numero: '))

valorx = int(input('Digite o valor X: '))

for i in range(ordem):
    for j in range(ordem):
        if matriz[i][j] == valorx:
            encontrado = True
            lin = i
            col = j

if encontrado:
    print(f'O valor X está na posição: [{lin}][{col}]')
else:
    print('O valor não foi encontrado.')

# Questão 6
ordem = 4
matriz1 = []
matriz2 = []
matrizR = []

for i in range(ordem):
    matriz1.append([0] * ordem)
    matriz2.append([0] * ordem)
    matrizR.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        print(f'Posição matriz1[{i}][{j}]')
        matriz1[i][j] = int(input('Digite um numero: '))

for i in range(ordem):
    for j in range(ordem):
        print(f'Posição matriz2[{i}][{j}]')
        matriz2[i][j] = int(input('Digite um numero: '))

for i in range(ordem):
    for j in range(ordem):
        if matriz1[i][j] >= matriz2[i][j]:
            matrizR[i][j] = matriz1[i][j]
        elif matriz2[i][j] > matriz1[i][j]:
            matrizR[i][j] = matriz2[i][j]

for i in range(ordem):
    for j in range(ordem):
        print(matrizR[i][j], ' ', end='')
    print()

# Questão 7
ordem = 10
matriz = []

for i in range(ordem):
    matriz.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        if i < j:
            matriz[i][j] = 2*i + 7*j - 2
        elif i == j:
            matriz[i][j] = (3*i)**2 - 1
        elif i > j:
            matriz[i][j] = (4*i)**3 - (5*j)**1 + 1

for i in range(ordem):
    for j in range(ordem):
        print(matriz[i][j], ' ', end='')
    print()

# Questão 8
ordem = 3
matriz = []

for i in range(ordem):
    matriz.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        print(f'Posição matriz[{i}][{j}]')
        matriz[i][j] = int(input('Digite um numero: '))

produto = 0
for i in range(ordem):
    for j in range(ordem):
        if i <= j:
            produto += matriz[i][j]

print(f'A soma dos elementos da diagonal principal é {produto}')

# Questão 9
ordem = 3
matriz = []

for i in range(ordem):
    matriz.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        print(f'Posição matriz[{i}][{j}]')
        matriz[i][j] = int(input('Digite um numero: '))

produto = 0
for i in range(ordem):
    for j in range(ordem):
        if i >= j:
            produto += matriz[i][j]

print(f'A soma dos elementos da diagonal principal é {produto}')

# Questão 10
ordem = 3
matriz = []

for i in range(ordem):
    matriz.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        print(f'Posição matriz[{i}][{j}]')
        matriz[i][j] = int(input('Digite um numero: '))

produto = 0
for i in range(ordem):
    for j in range(ordem):
        if i == j:
            produto += matriz[i][j]

print(f'A soma dos elementos da diagonal principal é {produto}')

# Questão 11
ordem = 3
matriz = []

for i in range(ordem):
    matriz.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        print(f'Posição matriz[{i}][{j}]')
        matriz[i][j] = int(input('Digite um numero: '))

produto = 0
for i in range(ordem):
    for j in range(ordem):
        if j+i == 2:
            produto += matriz[i][j]

print(f'A soma dos elementos da diagonal principal é {produto}')

# Questão 12
ordem = 3
matriz = []
matrizT = []

for i in range(ordem):
    matriz.append([0] * ordem)
    matrizT.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        print(f'Posição matriz[{i}][{j}]: ',end='')
        matriz[i][j] = int(input())

for i in range(ordem):
    for j in range(ordem):
        matrizT[j][i] = matriz[i][j]

for i in range(ordem):
    for j in range(ordem):
        print(matrizT[i][j], ' ', end='')
    print()

# Questão 13
ordem = 4
matriz = []
cont = 1

for i in range(ordem):
    matriz.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        matriz[i][j] = cont
        cont += 1

for i in range(ordem):
    for j in range(ordem):
        print(matriz[i][j], ' ', end='')
    print()

for i in range(ordem):
    for j in range(ordem):
        if i < j:
            matriz[i][j] = 0
print()
for i in range(ordem):
    for j in range(ordem):
        print(matriz[i][j], ' ', end='')
    print()

# Questão 14
import random
ordem = 5
matriz = []
aleatorio = random.sample(range(1, 100), 25)

for i in range(ordem):
    matriz.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        y = random.choice(aleatorio)
        matriz[i].insert(j, y)
        aleatorio.pop(aleatorio.index(y))

for i in range(ordem):
    for j in range(ordem):
        print(matriz[i][j], ' ', end='')
    print()

# Questão 15
alunos = 5
questoes = 10
prova = []
gabarito = ['a', 'b', 'c', 'd', 'd', 'c', 'b', 'a', 'b', 'd']
resultado = [0] * alunos

for i in range(alunos):
    prova.append([0] * questoes)

for i in range(alunos):
    for j in range(questoes):
        print(f'Aluno {i + 1} Questão {j + 1}:', end='')
        prova[i][j] = input('')

contador = 0
for i in range(alunos):
    for j in range(questoes):
        if prova[i][j] == gabarito[j]:
            contador += 1
    resultado.insert(i, contador)
    contador = 0

for i in range(alunos):
    print(f'O aluno {i + 1} acertou {resultado[i]} questões.')

# Questão 16
alunos = 3
questoes = 10
prova = []
gabarito = []
resultado = [0] * alunos

for i in range(questoes):
    gabarito.append(str(input(f'Digite o gabarito da questão {i+1}: ')))

for i in range(alunos):
    prova.append([0] * questoes)

for i in range(alunos):
    for j in range(questoes):
        print(f'Aluno {i + 1} Questão {j + 1}:', end='')
        prova[i][j] = input('')

contador = 0
for i in range(alunos):
    for j in range(questoes):
        if prova[i][j] == gabarito[j]:
            contador += 1
    resultado.insert(i, contador)
    contador = 0

for i in range(alunos):
    if resultado[i] >= 7:
        print(f'O aluno {i + 1} teve pontuação {resultado[i]} pontos. então ele foi aprovado.')
        print(f'A suas respostas foram: {prova[i]}')
    else:
        print(f'O aluno {i + 1} teve pontuação {resultado[i]} pontos. então ele foi reprovado.')
        print(f'A suas respostas foram: {prova[i]}')

# Questão 17 - Não sei fazer
lin = 10
col = 3
matriz = []

for i in range(lin):
    matriz.append([0] * col)

# Questão 18
ordem = 3
matriz = []
soma = [0] * ordem

for i in range(ordem):
    matriz.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        print(f'Posição matriz[{i + 1}][{j + 1}]:',end='')
        matriz[i][j] = int(input())

for i in range(ordem):
    for j in range(ordem):
        if j == 0:
            soma[0] += matriz[i][j]
        elif j == 1:
            soma[1] += matriz[i][j]
        elif j == 2:
            soma[2] += matriz[i][j]

for i in range(ordem):
    for j in range(ordem):
        print(matriz[i][j], ' ', end='')
    print()

print(f'O vetor soma é: {soma}')

# Questão 19
lin = 5
col = 4
matriz = []

for i in range(lin):
    matriz.append([0] * col)

for i in range(lin):
    for j in range(col):
        if j == 0:
            print(f'O numero da matricula do aluno {i +1}: ', end='')
            matriz[i][j] = int(input())
        elif j == 1:
            print(f'Digite a média das provas do aluno {i + 1}: ', end='')
            matriz[i][j] = float(input())
        elif j == 2:
            print(f'Digite a média dos trabalhos do aluno {i + 1}: ', end='')
            matriz[i][j] = float(input())
        elif j == 3:
            matriz[i][j] = (matriz[i][1] + matriz[i][2]) / 2

maior_nota = 0
matricula = 0
for i in range(lin):
    for j in range(col):
        if matriz[i][3] > maior_nota:
            maior_nota = matriz[i][3]
            matricula = matriz[i][0]

print(f'A maior nota é do aluno com matricula {matricula} com a nota {maior_nota}')

media = 0
for i in range(lin):
    media += matriz[i][3]

print(f'A média aritmética das notas finais é: {media / lin}')

# Questão 20
lin = 3
col = 6
matriz = []

for i in range(lin):
    matriz.append([0] * col)

for i in range(lin):
    for j in range(col):
        print(f'Matriz[{i+1}][{j+1}]: ', end='')
        matriz[i][j] = float(input())

soma = 0
media = 0
for i in range(lin):
    for j in range(col):
        if j % 2 !=0:
            soma += matriz[i][j]
        if j == 1 or j == 3:
            media += matriz[i][j]
        if j == 5:
            matriz[i][5] = matriz[i][1] + matriz[i][2]

print(f'A soma de todos os elementos com as colunas impares é igual á: {soma}')
print(f'A média aritmética da segunda e quarta coluna é {media / col}')
print('A matriz modificada:')
for i in range(lin):
    for j in range(col):
        print(matriz[i][j], ' ', end='')
    print()

# Questão 21 - Não terminada
ordem = 2
matriz1 = []
matriz2 = []
matrizR = []

for i in range(ordem):
    matriz1.append([0] * ordem)
    matriz2.append([0] * ordem)
    matrizR.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        print(f'Matriz1[{i+1}][{j+1}]: ', end='')
        matriz1[i][j] = float(input())
for i in range(ordem):
    for k in range(ordem):
        print(f'Matriz2[{i + 1}][{k + 1}]: ', end='')
        matriz2[i][k] = float(input())

print(f'Escolha uma das opções: ')
print('1 - somar as duas matrizes.')
print('2 - subtrair a primeira matriz da segunda.')
print('3 - adicionar uma constante ás duas matrizes.')
print('4 - imprimir as duas matrizes.')
print('5 - encerrar')
opcao = int(input('Digite uma das opções acima: '))

while opcao != 5:
    if opcao == 1:
        for i in range(ordem):
            for j in range(ordem):
                matrizR[i][j] = matriz1[i][j] + matriz2[i][j]
    elif opcao == 2:
        for i in range(ordem):
            for j in range(ordem):
                matrizR[i][j] = matriz2[i][j] - matriz1[i][j]
    elif opcao == 3:
        print('Não sei o que fazer na opção 3.')
    elif opcao == 4:
        print('matriz 1:')
        for i in range(ordem):
            for j in range(ordem):
                print(matriz1[i][j], ' ', end='')
            print()
        print('matriz 2:')
        for i in range(ordem):
            for j in range(ordem):
                print(matriz2[i][j], ' ', end='')
            print()
        print('matriz 3:')
        for i in range(ordem):
            for j in range(ordem):
                print(matrizR[i][j], ' ', end='')
            print()
    opcao = int(input('Digite uma das opções acima: '))

# Questão 22
ordem = 3
matrizA = []
matrizB = []
matrizC = []

for i in range(ordem):
    for j in range(ordem):
        matrizA.append([0] * ordem)
        matrizB.append([0] * ordem)
        matrizC.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        print(f'MatrizA[{i+1}][{j+1}]: ', end='')
        matrizA[i][j] = int(input())

for i in range(ordem):
    for j in range(ordem):
        print(f'MatrizB[{i+1}][{j+1}]: ', end='')
        matrizB[i][j] = int(input())

for i in range(ordem):
    for j in range(ordem):
        matrizC[i][j] = matrizA[i][j] * matrizB[i][j]

for i in range(ordem):
    for j in range(ordem):
        print(matrizC[i][j], ' ', end='')
    print()

# Questão 23
ordem = 3
matrizA = []
matrizB = []

for i in range(ordem):
    for j in range(ordem):
        matrizA.append([0] * ordem)
        matrizB.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        print(f'MatrizA[{i+1}][{j+1}]: ', end='')
        matrizA[i][j] = int(input())
        matrizB[i][j] = matrizA[i][j] ** 2

for i in range(ordem):
    for j in range(ordem):
        print(matrizB[i][j], ' ', end='')
    print()

# Questão 24 por Fazer


# Questão 25
ordem = 3
jogo_velha = []
vez = 0

for i in range(ordem):
    for j in range(ordem):
        jogo_velha.append([0] * ordem)

while vez <= 9:
    if vez % 2 == 0:
        print(f'Vez do Jogador 1')
        lin = int(input('Digite a lina: '))
        col = int(input('Digite a coluna: '))
        jogo_velha[lin][col] = -1
        vez += 1
        for i in range(ordem):
            for j in range(ordem):
                print(jogo_velha[i][j], ' ', end='')
            print()
    else:
        print(f'Vez do Jogador 2')
        lin = int(input('Digite a linha: '))
        col = int(input('Digite a coluna: '))
        jogo_velha[lin][col] = 1
        vez += 1
        for i in range(ordem):
            for j in range(ordem):
                print(jogo_velha[i][j], ' ', end='')
            print()
"""