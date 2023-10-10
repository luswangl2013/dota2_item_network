import pandas as pd
from dash import Dash, html
import dash_cytoscape as cyto

#data = [['item1','item2', 'a'],['item3','item2', 'b'],['item2','item4', 'c'], ['item4','', 'c'], ['item5','item4', 'b']]
#df = pd.DataFrame(data,columns=['item','next','category'])

df = pd.read_csv("C:\\Users\\slu\\OneDrive - Millennium Insurance Corp\\Documents\\item_test.csv")

print(df)
app = Dash(__name__)

nodes = [
    {
        'data': {'id': item, 'label': item, 'category': category}
    }
    for item, category in (
        list(df[['item', 'category']].itertuples(index=False, name=None))
    )
]
df_edge = df.dropna()[['item', 'next']]
edges = [
    {'data': {'source': item, 'target': next}}
    for item, next in (
        list(df_edge.itertuples(index=False, name=None))
    )
]
elements = nodes + edges

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-two-nodes',
        layout={'name': 'cose'},
        style={'width': '100%', 'height': '1000px'},
        elements=elements,
        stylesheet=[{
            'selector': 'edge',
                'style': {
                    'curve-style': 'bezier',
                    'target-arrow-color': 'blue',
                    'target-arrow-shape': 'vee',
                    'line-color': 'blue'
                }
        },
        {
                'selector': 'node',
                'style': {
                    'label': 'data(label)'
                }
            },
            {
                'selector': '[category *= "a"]',
                'style': {
                    'background-color': '#6495ED'
                    #'shape': 'rectangle'
                }
            },
            {
                'selector': '[category *= "b"]',
                'style': {
                    'background-color': '#FF4136'
                    #'shape': 'rectangle'
                }
            },
            {
                'selector': '[category *= "c"]',
                'style': {
                   'background-color': '#DFFF00'
                    #'shape': 'rectangle'
                }
            },
            ]
    )
])

if __name__ == '__main__':
    app.run(debug=True)