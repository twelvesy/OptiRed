from collections import deque

#---Modulo para el recorrido BFS
def bfs(grafo, inicio):
    visitados = set([inicio]) #---Marca el nodo inicial como visitado
    cola = deque([inicio]) #---Cola para recorrer por niveles
    recorrido = [] #---Guarda el orden de visita

    while cola:
        nodo = cola.popleft() #---Extrae el primer nodo de la cola
        recorrido.append(nodo) #---Registra el nodo visitado

        for vecino in grafo[nodo]: #---Recorre los vecinos del nodo
            if vecino not in visitados:
                visitados.add(vecino) #---Marca el vecino como visitado
                cola.append(vecino) #---Lo agrega a la cola

    return recorrido #---Devuelve el recorrido BFS

#---Modulo para el recorrido DFS
def dfs(grafo, inicio):
    visitados = set() #---Conjunto de nodos visitados
    recorrido = [] #---Guarda el orden de visita

    def visitar(nodo):
        visitados.add(nodo) #---Marca el nodo como visitado
        recorrido.append(nodo) #---Registra el nodo visitado

        for vecino in grafo[nodo]: #---Recorre los vecinos
            if vecino not in visitados:
                visitar(vecino) #---Llamada recursiva al vecino

    visitar(inicio) #---Inicia el recorrido DFS
    return recorrido #---Devuelve el recorrido DFS