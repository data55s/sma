## 6. Structure based Social Media Analysis Model
import pandas as pd, networkx as nx, matplotlib.pyplot as plt, community as louvain
# Data & Graph
df = pd.DataFrame({'s':['A','A','B','B','C','C','D','E','F','G','H','D','B'],
                   't':['B','C','C','D','D','E','E','F','G','H','A','G','H']})
G = nx.from_pandas_edgelist(df, 's', 't')
# Analysis
part = louvain.best_partition(G)
rank = nx.pagerank(G)
# Quick Visual & Output
nx.draw(G, with_labels=True, node_color=list(part.values()), cmap='Set3')
plt.show()
print("Communities:", part)
print("Top User:", max(rank, key=rank.get))
