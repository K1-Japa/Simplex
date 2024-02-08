import numpy as np

def entrada():
    print("Insira a quantidade de variaveis do problema: ")
    variaveis_qtd = int(input())

    print("Insira a quantidade de equacoes do problema: ")
    equacoes_qtd = int(input())

    completa = []

    for i in range(equacoes_qtd+1):
        aux = []
        for j in range(variaveis_qtd):
            if i == 0:
                print("Insira o valor correspondente a x" + str(j) + " na funcao objetivo")
                entrada = int(input())
                aux.append(entrada)
            else:
                print("Insira o valor correspondente a x" + str(j) + " na equacao " + str(i))
                entrada = int(input())
                aux.append(entrada)

        if i != 0:
            print("Insira o resultado da equacao " + str(i))
            entrada = int(input())
            aux.append(entrada)

        completa.append(aux)
        print(completa[len(completa)-1])
        print()
    
    for i in range(len(completa)):
        for j in completa[i]:
            print(j, end=" ")
        print()

    indexBase = []
    for i in range(equacoes_qtd):
        print("Escolha a " + str(i+1) + "a variavel da base")
        entrada = int(input())
        indexBase.append(entrada)

    indexNaoBase = []
    for i in range(equacoes_qtd):
        if not(i in indexBase):
            indexNaoBase.append(i)
        
    return completa, indexBase, indexNaoBase

def simplex(completa, indexBase, indexNaoBase):
    valorVariaveis = []
    for i in range(len(completa)):
        valorVariaveis.append([])
        for j in range(len(completa[0])):
            valorVariaveis[i].append(completa[i][j])

    b = []
    for i in range(1, len(completa)):
        b.append([completa[i][len(completa[1])-1]])

    base = []
    for i in range(1, len(completa)):
        base.append([])
        for j in range(len(indexBase)):
            base[i-1].append(completa[i][indexBase[j]])

    naoBase = []
    for i in range(1, len(completa)):
        naoBase.append([])
        for j in range(len(indexNaoBase)):
            naoBase[i-1].append(completa[i][indexNaoBase[j]])

    CTB = []
    for i in indexBase:
        CTB.append(completa[0][i])

    CTN = []
    for i in indexNaoBase:
        CTN.append(completa[0][i])

    iteracao = 1
    while True:
        print("\n\n" + str(iteracao) + "a iteracao")

        baseInversa = np.linalg.inv(base)

        solucaoBasica = passo1(baseInversa, b)

        menor, index = passo2(CTB, CTN, baseInversa, indexNaoBase, valorVariaveis)

        var = passo3(menor, solucaoBasica, index, valorVariaveis, baseInversa)

        if var == "SEM SOLUCAO":
            return False
        elif var == "SOLUCAO OTIMA":
            print("\nSolucao Otima: ")

            solucao = []
            for _ in range(len(valorVariaveis[0])):
                solucao.append(0)
            
            for i in range(len(valorVariaveis[0])):
                for j in range(len(indexBase)):
                    if i == indexBase[j]:
                        solucao[indexBase[j]] = solucaoBasica[j][0]
            
            for i in range(len(solucao)):
                print("|x" + str(i) + " = " + str(solucao[i]))
                    
            return False
        
        else:
            indexBase, base, CTB, indexNaoBase, naoBase, CTN = passo6(indexBase, indexNaoBase, index, var, base, naoBase, valorVariaveis)
            iteracao = iteracao + 1
        

#Passo 1 -> Cálculo da Solução Básica
def passo1(baseInversa, b):
    print("\nPasso 1:")
    print(baseInversa)
    print()
    print(b)
    solucaoBasica = np.dot(baseInversa, b)
    print("Solucao Basica:\n" + str(solucaoBasica))
    return solucaoBasica

#Passo 2 -> Cálculo dos custos relativos
def passo2(CTB, CTN, baseInversa, indexNaoBase, valorVariaveis):
    print("\nPasso 2:")
    #i
    lambdaT = np.dot(CTB, baseInversa)
    print("LambdaT: " + str(lambdaT))

    #ii
    CN = []
    for i in range(len(indexNaoBase)):
        AN = []
        for j in range(1, len(valorVariaveis)):
            AN.append([(valorVariaveis[j][indexNaoBase[i]])])
        aux = np.dot(lambdaT, AN)
        aux = CTN[i] - aux[0]
        CN.append(aux)
    
    print("\nC^N: " + str(CN))

    #iii
    menor = np.inf
    for i in range(len(indexNaoBase)):
        if CN[i] < menor:
            menor = CN[i]
            index = i

    print("\nCNK: " + str(menor))
    print("\nK: " + str(indexNaoBase[index]))
    print("A variavel que vai entrar na base eh x" + str(indexNaoBase[index]))
    return menor, index

#Passo 3 -> Teste de Otimilidade
def passo3(menor, solucaoBasica, index, valorVariaveis, baseInversa):
    print("\nPasso 3:")
    if menor < 0:
        print(str(menor) + " eh menor que zero. Algoritmo continua")
        return passo5(solucaoBasica, index, valorVariaveis, baseInversa)
    else:
        print(str(menor) + " nao eh menor que zero. Solucao atual eh otima")
        return "SOLUCAO OTIMA"

#Passo 4 ->  Cálculo da Solução Simplex
def passo4(index, valorVariaveis, baseInversa):
    print("\nPasso 4:")
    ANK = []
    for j in range(1, len(valorVariaveis)):
        ANK.append([(valorVariaveis[j][index])])
    return np.dot(baseInversa, ANK)

#Passo 5 -> Determinação do passo e variável a sair da base
def passo5(solucaoBasica, index, valorVariaveis, baseInversa):
    aux = 0
    y = passo4(index, valorVariaveis, baseInversa)
    print("A solucao Simplex eh:\n" + str(y))
    print("\nPasso 5:")

    menor = np.inf
    var = 1
    for i in range(len(y)):
        if y[i] > 0:
            aux = 1
            if (solucaoBasica[i][0]/y[i]) < menor:
                menor = solucaoBasica[i][0]/y[i]
                var = i
    
    if aux == 0:
        print("Sem solução!")
        return "SEM SOLUCAO"
    else:
        print("A variavel que sai da base eh: ab" + str(var))
        return var

#Passo 6 -> Atualização!
def passo6(indexBase, indexNaoBase, index, var, base, naoBase, valorVariaveis):
    print("\nPasso 6:")
    indexBase[var], indexNaoBase[index] = indexNaoBase[index], indexBase[var]
    
    for i in range(len(base[0])):
        base[i][var], naoBase[i][index] = naoBase[i][index], base[i][var]

    CTB = []
    for i in range(len(indexBase)):
        CTB.append(valorVariaveis[0][indexBase[i]])
    
    CTN = []
    for i in range(len(indexNaoBase)):
        CTN.append(valorVariaveis[0][indexNaoBase[i]])

    print("Nova base: " + str(indexBase))
    print(base)
    print("CTB: " + str(CTB))

    print("\nNova nao base: " + str(indexNaoBase))
    print(naoBase)
    print("CTN: " + str(CTN))

    return indexBase, base, CTB, indexNaoBase, naoBase, CTN

completa, indexBase, indexNaoBase = entrada()
simplex(completa, indexBase, indexNaoBase)