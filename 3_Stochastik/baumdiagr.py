import networkx as nx
import matplotlib.pyplot as plt

edge_list = [(0,1), (0,2),(1,3),(1,4),(2,5),(2,6)]

 
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
pos = {0: (0,0), 1:(0.5,1), 2:(0.5,-1), 3:(1,1.5), 4:(1,0.5), 5:(1,-0.5), 6:(1,-1.5)}
#pos=nx.spring_layout(G)

# set edge labels
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
    "node_size": 2000,
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