import pandas as pd
import networkx as nx
from pyvis.network import Network

df = pd.read_csv("./dota2_7.33_item.csv")

print(df)

net = Network(notebook=False,directed=True,height='800px',select_menu=True,filter_menu=True)
df_nodes = df[['item', 'category']].drop_duplicates()
color_dict = {"basic_attributes": "#fb4b4b", 
              "basic_equipment": "#fb874b", 
              "basic_miscellaneous": "#fbc34b", 
              "basic_secretshop": "#fbed4b",
              "upgrades_accessories":'#a2fb4b',
              "upgrades_support":'#4bfb80',
              "upgrades_magical":'#4bfbf5',
              "upgrades_armor":'#4ba6fb',
              "upgrades_weapons":'#4b67fb',
              "upgrades_artifacts":'#142ffd'}
df_nodes['color'] = df_nodes.apply(lambda x: color_dict[x['category']], axis=1)

net.add_nodes(list(df_nodes['item']), color=list(df_nodes['color']))

df_edge = df.dropna()[['item', 'next']]

edge_list = list(df_edge.itertuples(index=False, name=None))

net.add_edges(edge_list)

neighbor_map = net.get_adj_list()

# add neighbor data to node hover data
for node in net.nodes:
                node["title"] = node["label"]
                node["title"] += " Neighbors:\n" + "\n".join(neighbor_map[node["id"]])
                node["value"] = len(neighbor_map[node["id"]])
                node["group"] = df_nodes.loc[df_nodes['item'] == node["label"]]['category'].values[0]
                node["level"] = node["group"].split('_')[0]

net.barnes_hut()
net.show_buttons(filter_=['physics'])
net.show("example.html", notebook=False)