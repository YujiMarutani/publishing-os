import networkx as nx

def verify_dag(nodes):
    G = nx.DiGraph()
    for node in nodes:
        cid = node["concept_id"]
        G.add_node(cid)
        for dep in node.get("dependency", []):
            G.add_edge(dep, cid)
    
    if not nx.is_directed_acyclic_graph(G):
        cycles = list(nx.simple_cycles(G))
        raise ValueError(f"Topological Violation: Circular dependency detected in DAG -> {cycles}")
    return True
