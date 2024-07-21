import networkx as nx
import matplotlib.pyplot as plt

edge_list = [(0,1), (0,2),(0,3),(1,4),(1,5),(1,6),(2,7),(2,8),(2,9),(3,10),(3,11),(3,12)]

 
G = nx.Graph()
G.add_edges_from(edge_list)

# set node labels
labels={}
labels[0]=""
labels[1]="K"
labels[2]="Z"
labels[3]="K"
labels[4]="Z"
labels[5]="K"
labels[6]="Z"

# set node positions
node_group_1 = [0]
node_group_2 = [1, 2,3]
node_group_3 = [4, 5, 6, 7,8,9,10,11,12]

# set the position according to column (x-coord)
pos = {n: (0, i) for i, n in enumerate(node_group_1)}
pos.update({n: (1, 24-24*i) for i, n in enumerate(node_group_2)})
pos.update({n: (2, 36-9*i) for i, n in enumerate(node_group_3)})


# set edge labels
a=2
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={(0,1): r"$\frac{1}{2}$", 
                 (0,2): r"$\frac{1}{2}$", 
                 (1,3): r"$\frac{1}{4}$",
                 (1,4): r"$\frac{1}{4}$",
                 (2,5): r"$\frac{1}{4}$",
                 (2,6): r"$\frac{1}{4}$",
    },
    font_size= 14,
    rotate= False
)

# set options
options = {
    "font_size": 12,
    "node_size": 1000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 1,
    "width" : 1,
    "with_labels": False
}

nx.draw_networkx(G,pos, **options)
nx.draw_networkx_labels(G, pos, labels, font_size=12, font_family="sans_serif", alpha= 1.0)
plt.tight_layout()
plt.axis("off")
plt.show()