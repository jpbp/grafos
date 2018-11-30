from Estruturas.MatrizAdjacencia import MatrizAdjacencia
from Estruturas.ListaAdjacencia import ListaAdjacencia
from Busca.BuscaProfundidade import BuscaProfundidade
from ExportaArqGraph import ArquivoGraph

def main():
    matriz = MatrizAdjacencia()

    entrada = ""
    while(entrada != "fim"):
        entrada = input()
        if(entrada != "fim"):
            matriz.adicionaVertice(entrada)

    entrada = ""
    saida = ""
    while(entrada != "fim"):
        entrada = input().split()

        if(entrada[0] != "fim"):
            matriz.adicionaAresta(entrada[0], entrada[1], "Chefe")
        else:
            entrada = entrada[0]
    print("Grafo de entrada\n", matriz)
    dfs = BuscaProfundidade()
    dfs.buscaProfundidade(matriz)

    lista = dfs.listaTopologica

    calculaAnteriores(lista)

    imprimeResultados(matriz)


    mat = criaNovaMatrizAdj(lista)

    arq = ArquivoGraph("teste")
    arq.escreveGrafoDirecionado(mat)
    arq.close()

def calculaAnteriores(lista):
    for i in range(len(lista) - 1):
        if(lista[i].anterior == None):
            j = i + 1
            while((j < len(lista)) and (lista[j].tempoAbertura != lista[i].tempoFechamento + 1)):
                j += 1
            lista[i].anterior = lista[j]

def imprimeResultados(grafo):
    vertices = grafo.vertices
    for vertice in vertices:
        if(vertices[vertice].anterior != None):
            print(str(vertice) + " (" + str(vertices[vertice].anterior.nome) + ")")
        else:
            print(str(vertice) + " (Presidente)")


def criaNovaMatrizAdj(lista):
    matriz = MatrizAdjacencia()
    for elemento in lista:
        matriz.adicionaVertice(elemento.nome)
    
    for elemento in lista:
        if(elemento.anterior != None):
            matriz.adicionaAresta(elemento.anterior.nome, elemento.nome, "Chefe")
    return matriz

main()