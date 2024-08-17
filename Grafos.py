import heapq  # Importa a biblioteca heapq para manipulação de filas de prioridade
import networkx as nx  # Importa a biblioteca NetworkX para criação e manipulação de grafos
import matplotlib.pyplot as plt  # Importa a biblioteca Matplotlib para desenhar gráficos

# Criando o grafo diretamente com as distâncias entre as cidades
graph = {
    'Santa Cruz do Piauí': {'Oeiras': 70, 'Paquetá': 50},
    'Picos': {'Oeiras': 85, 'Simplicio Mendes': 110, 'Paquetá': 55},
    'Oeiras': {'Santa Cruz do Piauí': 70, 'Picos': 85, 'Floriano': 120, 'Simplicio Mendes': 50},
    'Floriano': {'Oeiras': 120},
    'Simplicio Mendes': {'Oeiras': 50, 'Picos': 110},
    'Paquetá': {'Santa Cruz do Piauí': 50, 'Picos': 55}
}

def dijkstra(graph, start, end):
    # Inicializa a fila de prioridade com a cidade de início e distância 0
    queue = [(0, start)]
    # Inicializa as distâncias com infinito para todas as cidades
    distances = {node: float('inf') for node in graph}
    # Define a distância da cidade de início como 0
    distances[start] = 0
    # Inicializa o dicionário que armazena o caminho mais curto
    path = {}

    while queue:  # Enquanto a fila não estiver vazia
        # Extrai o nó com a menor distância
        current_distance, current_node = heapq.heappop(queue)
        if current_node == end:  # Se o nó atual for o destino, encerra o loop
            break
        # Para cada vizinho do nó atual
        for neighbor, weight in graph[current_node].items():
            # Calcula a nova distância para o vizinho
            distance = current_distance + weight
            # Se a nova distância for menor que a distância conhecida
            if distance < distances.get(neighbor, float('inf')):
                # Atualiza a menor distância
                distances[neighbor] = distance
                # Define o nó atual como o antecessor no caminho
                path[neighbor] = current_node
                # Adiciona o vizinho à fila de prioridade
                heapq.heappush(queue, (distance, neighbor))

    # Construindo a rota de trás para frente
    route, step = [], end
    while step:  # Enquanto houver nós no caminho
        route.append(step)  # Adiciona o nó à rota
        step = path.get(step)  # Move para o nó anterior no caminho
    return distances[end], route[::-1]  # Retorna a menor distância e a rota na ordem correta

def draw_graph(graph, path=None):
    # Cria um grafo do NetworkX com as arestas e pesos do dicionário
    G = nx.Graph([(u, v, {'weight': w}) for u, neighbors in graph.items() for v, w in neighbors.items()])
    # Define a posição dos nós no gráfico
    pos = nx.spring_layout(G)
    # Desenha o grafo com os rótulos dos nós
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=15, font_color='black', font_weight='bold')
    # Adiciona os rótulos das arestas (distâncias)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
    if path:  # Se houver um caminho a ser destacado
        # Destaca o caminho mais curto no grafo
        nx.draw_networkx_edges(G, pos, edgelist=list(zip(path, path[1:])), edge_color='r', width=2)
    plt.show()  # Mostra o gráfico

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    # Solicita ao usuário a cidade de destino
    end_city = input("Digite a cidade de destino a partir de Santa Cruz do Piauí: ")
    try:
        # Calcula a menor distância e a rota mais curta
        distance, route = dijkstra(graph, 'Santa Cruz do Piauí', end_city)
        print(f"Menor distância de Santa Cruz do Piauí para {end_city}: {distance}")
        print(f"Caminho mais curto: {' -> '.join(route)}")
        # Desenha o grafo com a rota destacada
        draw_graph(graph, route)
    except KeyError:
        # Informa se a cidade de destino não estiver no grafo
        print(f"A cidade '{end_city}' não está no grafo.")
