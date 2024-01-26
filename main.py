def triang(matriz):
    n = len(matriz)
    p = 1
    for k in range(n-1):
        if matriz[k][k] == 0:
            for j in range(k+1, n):
                if matriz[j][k] != 0:
                    for o in range(n):
                        matriz[j][o], matriz[k][o] = matriz[k][o], matriz[j][o]
                    p = p * (-1)
                    break
        if matriz[k][k] == 0:
            return 0
        for m in range(k+1, n):
            F = (-1) * (matriz[m][k]/matriz[k][k])
            for l in range(k, n):
                matriz[m][l] = int(matriz[m][l] + (F * matriz[k][l]))
    return matriz

def transposta(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    transposta = [[0 for _ in range(colunas)] for _ in range(linhas)]
    for i in range(linhas):
        for j in range(colunas):
            transposta[i][j] = matriz[j][i]
    return transposta

def calcula_det(matriz):
    det = 1
    for i in range(len(matriz)):
        det = det * matriz[i][i]
    return det

def verifica_det(matriz):
    if triang(matriz) != 0:
        if calcula_det(matriz) != 0:
            return True
        else:
            return False
    else:
        return False


def printa_matriz(matriz):
    for i in range(len(matriz)):
        print()
        for j in range(len(matriz)):
            print(str(matriz[i][j]) + " ", end="")
    print()

matriz = [[1,1,1],
          [2,2,2],
          [1,2,3]]

def simplex():
    print("Insira a quantidade de equacoes: ")
    qtd_equacoes = int(input())
    print("Insira a quantidade de i de X que o problema possui (Xi): ")
    qtd_x = int(input())
    
    equacoes = [["-" for _ in range(qtd_x)] for _ in range(qtd_equacoes + 1)]

    # Pegar a funcao objetivo tambem

    for j in range(qtd_equacoes):
        for i in range(qtd_x-1):
            print("Equacao " + str(j) + ": Insira o valor correspondente ao X" + str(i) + ": ")
            equacoes[j][i] = int(input())
        print("Equacao " + str(j) + ": Insira o valor correspondente à igualdade: ")
        equacoes[j][qtd_x-1] = int(input())

    print(equacoes)

    print("Problema fornecido: ")
    #Funcao objetivo
    for i in range(len(equacoes)):
        print()
        for j in range(len(equacoes[0])):
            print(str(equacoes[i][j]) + "X" + str(j) + " ", end="")

    algoritmo_simplex(qtd_equacoes, qtd_x, equacoes)


def algoritmo_simplex(qtd_equacoes, qtd_x, equacoes):
    fase1()
    fase2()

def fase1():
    pass

def fase2():
    def passo1():
        pass
    def passo2():
        pass
    def passo3():
        pass
    def passo4():
        pass
    def passo5():
        pass
    def passo6():
        pass

simplex()