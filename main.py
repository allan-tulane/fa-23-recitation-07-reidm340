from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
        
    count = 0
    while len(frontier) != 0:
        tmp = result

        for i in frontier:
            result.update(graph[i])
            frontier.update(graph[i])
            current_node = i
            break

        frontier.remove(current_node)

        if (tmp == result) and (count > 10):
            break
        count += 1
    
    return result


def connected(graph):
    reachable(graph, next(iter(graph)))
    return len(graph) == len(reachable(graph,next(iter(graph))))


def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    i = set()
    
    for j in graph:
        k = reachable(graph, next(iter(j)))
        i.add(len(k))

    if (len(graph)) in i:
        return 1
    else:
        return len(i)
