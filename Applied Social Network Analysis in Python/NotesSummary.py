# Bipartite Graphs
# Use Graph(), DiGraph(), MultiGraph()
# Use from networkx.algrithoms import bipartite for bipartite related algrithoms
# (Many algrithoms only work on Graph())

import networkx as nx
from networkx.algrithoms import bipartite

# Check if B is bipartite
nx.bipartite.is_bipartite(B)
# Check if node set X is a bipartition
bipartite.is_bipartite_node_set(B, X)
# Get each set of nodes of bipartite graph B
bipartite.sets(B)
# Get the bipartite projection of node set X
bipartite.projected_graph(B, X)
