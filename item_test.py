import pandas as pd
import networkx as nx

#data = [['item1','item2', 'a'],['item3','item2', 'b'],['item2','item4', 'c'], ['item4','', 'c'], ['item5','item4', 'b']]
#df = pd.DataFrame(data,columns=['item','next','category'])

df = pd.read_excel("C:\\Users\\slu\\OneDrive - Millennium Insurance Corp\\Documents\\item_test.xlsx")

print(df)
G = nx.from_pandas_edgelist(df,
                           source='item',
                           target='next')

from pyvis.network import Network
net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white", notebook=False)
net.from_nx(G)
net.show("example.html", notebook=False)