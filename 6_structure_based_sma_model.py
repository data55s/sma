# Auto-install
try:
    import pandas as pd, networkx as nx, matplotlib.pyplot as plt, community as louvain
except:
    import os; os.system("pip install pandas networkx matplotlib python-louvain")
    import pandas as pd, networkx as nx, matplotlib.pyplot as plt, community as louvain

# Data & Graph
df=pd.DataFrame({'s':['A','A','B','B','C','C','D','E','F','G','H','D','B'],
                 't':['B','C','C','D','D','E','E','F','G','H','A','G','H']})
G=nx.from_pandas_edgelist(df,'s','t')

# Analysis
part=louvain.best_partition(G)
rank=nx.pagerank(G)

# Visual (clear layout)
pos=nx.spring_layout(G)
nx.draw(G,pos,with_labels=True,node_color=list(part.values()),cmap=plt.cm.Set3,node_size=800,font_size=10)
plt.title("Social Network Graph (Communities Highlighted)")
plt.show()

# Clear Output
print("\n--- Community Groups ---")
for k,v in part.items(): print(f"User {k} → Community {v}")

print("\n--- Influence Ranking (Top User) ---")
top=max(rank,key=rank.get)
print(f"Top Influential User: {top}")
