class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        links = []
        city_size = len(isConnected)
        for i in range(city_size): # transformando a lista em grafo
            links.append([])
            for j in range(city_size):
                if isConnected[i][j] == 1:
                    links[i].append(j)
        provinces = []
        auxList = []
        for node in links: # pegando as conecções e transformando em itens únicos
            if node not in provinces:
                auxList.append(connected_city(links, links.index(node), []))
        print(auxList)
        for i in range(len(auxList)): # contando as provincias
            j = i + 1
            while(j < len(auxList)):
                if intersection(auxList[i], auxList[j]):
                    auxList.insert(i, auxList.pop(j) + auxList.pop(i))
                    j -= 1
                j +=1
        provinces = auxList
        return len(provinces)


def connected_city(graph, i, listaux): # checa se há conecções entre as cidades
    connected = listaux + [i]
    for node in graph[i]:
        if node not in connected:
            connected = connected_city(graph, node, connected)
    return connected
    pass


def intersection(list1, list2): # checa se há interseções entre listas( usado pra checar as cidades indiretamente conectadas
    aux = [value for value in list1 if value in list2]
    if len(aux) > 0:
        return 1
    return 0

