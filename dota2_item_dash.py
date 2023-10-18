import pandas as pd
from dash import Dash, html
import dash_cytoscape as cyto

df = pd.read_csv("./dota2_7.33_item.csv")

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
        layout={'name': 'cose'}, #circle , concentric , breadthfirst 
        style={'width': '100%', 'height': '1000px'},
        elements=elements,
        stylesheet=[{
            'selector': 'edge',
                'style': {
                    'curve-style': 'bezier',
                    'target-arrow-color': 'grey',
                    'target-arrow-shape': 'vee',
                    'line-color': 'grey'
                }
        },
        {
                'selector': 'node',
                'style': {
                    'label': 'data(label)'
                }
            },
            {
                'selector': '[category *= "basic_attributes"]',
                'style': {
                    'background-color': '#fb4b4b'
                    #'shape': 'rectangle'
                }
            },
            {
                'selector': '[category *= "basic_equipment"]',
                'style': {
                    'background-color': '#fb874b'
                    #'shape': 'rectangle'
                }
            },
            {
                'selector': '[category *= "basic_miscellaneous"]',
                'style': {
                   'background-color': '#fbc34b'
                    #'shape': 'rectangle'
                }
            },
            {
                'selector': '[category *= "basic_secretshop"]',
                'style': {
                    'background-color': '#fbed4b'
                    #'shape': 'rectangle'
                }
            },
            {
                'selector': '[category *= "upgrades_accessories"]',
                'style': {
                    'background-color': '#a2fb4b'
                    #'shape': 'rectangle'
                }
            },
            {
                'selector': '[category *= "upgrades_support"]',
                'style': {
                    'background-color': '#4bfb80'
                    #'shape': 'rectangle'
                }
            },
            {
                'selector': '[category *= "upgrades_magical"]',
                'style': {
                    'background-color': '#4bfbf5'
                    #'shape': 'rectangle'
                }
            },
            {
                'selector': '[category *= "upgrades_armor"]',
                'style': {
                    'background-color': '#4ba6fb'
                    #'shape': 'rectangle'
                }
            },
            {
                'selector': '[category *= "upgrades_weapons"]',
                'style': {
                    'background-color': '#4b67fb'
                    #'shape': 'rectangle'
                }
            },
{
                'selector': '[category *= "upgrades_artifacts"]',
                'style': {
                    'background-color': '#142ffd'
                    #'shape': 'rectangle'
                }
            },                    
            ]
    )
])

if __name__ == '__main__':
    app.run(debug=True)
