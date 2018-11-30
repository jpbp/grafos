from Estruturas.MatrizAdjacencia import MatrizAdjacencia
from Estruturas.ListaAdjacencia import ListaAdjacencia
from Busca import BuscaProfundidade
from Busca import BuscaLargura
from ExportaArqGraph import ArquivoGraph
def main():

    lista = ListaAdjacencia()
    lista.adicionaVertice("A")
    lista.adicionaVertice("Q")
    lista.adicionaVertice("P")
    lista.adicionaVertice("0")
    lista.adicionaVertice("1")
    lista.adicionaVertice("2")
    lista.adicionaVertice("3")
    lista.adicionaVertice("4")
    lista.adicionaVertice("5")
    lista.adicionaVertice("6")
    lista.adicionaVertice("7")
    lista.adicionaVertice("8")
    lista.adicionaVertice("9")
    lista.adicionaVertice("s")
    lista.adicionaVertice("t")
    lista.adicionaAresta("A", "0", "1","0")
    lista.adicionaAresta("A", "1", "1","0")
    lista.adicionaAresta("A", "2", "1","0")
    lista.adicionaAresta("A", "3", "1","0")
    lista.adicionaAresta("A", "4", "1","0")
    lista.adicionaAresta("Q", "5", "1","0")
    lista.adicionaAresta("P", "5", "1","0")
    lista.adicionaAresta("P", "6", "1","0")
    lista.adicionaAresta("P", "7", "1","0")
    lista.adicionaAresta("P", "8", "1","0")
    lista.adicionaAresta("P", "9", "1","0")
    lista.adicionaAresta("s", "A", "4","0")
    lista.adicionaAresta("s", "Q", "1","0")
    lista.adicionaAresta("s", "P", "4","0")
    lista.adicionaAresta("t", "0", "1","0")
    lista.adicionaAresta("t", "1", "1","0")
    lista.adicionaAresta("t", "2", "1","0")
    lista.adicionaAresta("t", "3", "1","0")
    lista.adicionaAresta("t", "4", "1","0")
    lista.adicionaAresta("t", "5", "1","0")
    lista.adicionaAresta("t", "6", "1","0")
    lista.adicionaAresta("t", "7", "1","0")
    lista.adicionaAresta("t", "8", "1","0")
    lista.adicionaAresta("t", "9", "1","0")
    
    
    print("------------------------")
    print("Lista adj:\n")
    print(lista)
    #~ print("------------------------")
    #~ print("Busca em profundidade:\n")
    #~ BuscaProfundidade.buscaProfundidade(lista)
    #~ print("------------------------")
    #~ print("Busca em largura:\n")
    #~ BuscaLargura.buscaLargura(lista)

    #~ arq = ArquivoGraph("teste")
    #~ arq.escreveGrafo(lista)
    #~ arq.close()


    

main()
