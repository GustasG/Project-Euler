'''
Adj. list data structure for algorithm
'''
class Edge:
    def __init__(self, src: int, dest: int, weight: int):
        self.src = src
        self.dest = dest
        self.weight = weight


def find(parent: list, x: int) -> int:
    while x != parent[x]:
        x = parent[x]

    return x


def union(parent: list, rank: list, edge: Edge):
    rx = find(parent, edge.src)
    ry = find(parent, edge.dest)

    if rx == ry:
        return

    if rank[rx] > rank[ry]:
        parent[ry] = rx
    else:
        parent[rx] = ry

        if rank[rx] == rank[ry]:
            rank[ry] += 1


'''
takes graph as adj. list array and number of vertices in that graph
returns MST as adj. list
'''
def kruskal(graph: list, vertices: int) -> list:
    parent = [i for i in range(vertices + 1)]
    rank = [0 for i in range(vertices + 1)]

    graph = sorted(graph, key=lambda item: item.weight)

    A = []

    for edge in graph:
        if find(parent, edge.src) != find(parent, edge.dest):
          A.append(edge)
          union(parent, rank, edge)

    return A


def parse_file(file_name: str) -> list:
    file_data = open(file_name, 'r').read().split('\n')

    graph = []

    for i in range(len(file_data)):
        line = file_data[i]
        weights = line.split(',')

        for j in range(len(weights)):
            weight = weights[j]

            if weight != '-' and weight != '':
                graph.append(Edge(i, j, int(weight)))
    
    return graph


def find_max_saving(file_name: str, num_verticies: int) -> int:
    graph = parse_file(file_name)
    tree = kruskal(graph, num_verticies)

    start_weight = sum(edge.weight for edge in graph) // 2
    final_weight = sum(edge.weight for edge in tree)

    return start_weight - final_weight



def main():
    file_name = 'problem_107_network.txt'
    num_verticies = 40


    print(find_max_saving(file_name, num_verticies)) 


if __name__ == "__main__":
    main()