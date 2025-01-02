import networkx as nx
import matplotlib.pyplot as plt

# a. Depict the original graph
def depict_original_graph():
    edges = [
        ('A', 'B', 1), ('B', 'D', 3), ('D', 'F', 1), ('F', 'Z', 6),
        ('Z', 'E', 1), ('E', 'C', 6), ('C', 'D', 8), ('A', 'G', 10),
        ('A', 'C', 5), ('G', 'E', 3), ('C', 'Z', 9)
    ]
    graph = nx.Graph()
    for u, v, weight in edges:
        graph.add_edge(u, v, weight=weight)
    return graph, edges

def show_graph(graph, title):
    pos = nx.spring_layout(graph)  # Automatically position nodes
    nx.draw(graph, pos, with_labels=True, node_size=700, font_size=10)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.title(title)
    plt.show()

# b. State which MST algorithm we are following
print("Using Kruskal's Algorithm to find the Minimum Spanning Tree (MST)")

# c. Show the creation of the MST step by step
def kruskal_mst(edges, nodes):
    # Sort edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[2])
    mst = nx.Graph()
    mst.add_nodes_from(nodes)
    parent = {node: node for node in nodes}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            parent[root2] = root1

    print("\nStep-by-step MST Creation:")
    for edge in sorted_edges:
        u, v, weight = edge
        if find(u) != find(v):
            mst.add_edge(u, v, weight=weight)
            union(u, v)
            print(f"Added edge: {u}-{v} with weight {weight}")
            show_graph(mst, f"Step: Added edge {u}-{v} with weight {weight}")
    return mst

# d. Depict the final MST
def main():
    # Original graph and edges
    original_graph, edges = depict_original_graph()
    nodes = original_graph.nodes()
    
    # Step 1: Depict the original graph
    show_graph(original_graph, "Original Graph")
    
    # Step 2: Create MST using Kruskal's algorithm
    mst = kruskal_mst(edges, nodes)
    
    # Step 3: Depict the final MST
    show_graph(mst, "Final Minimum Spanning Tree")

main()
