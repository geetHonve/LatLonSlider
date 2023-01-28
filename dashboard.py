from dash import Dash, dcc, html, Output, Input
import plotly.express as px
import pandas as pd
import math




df = pd.read_csv("/Users/deekshitha/Desktop/Shipping Project/2018-01-03.csv")

rangeslider_marks = {-90: '90 S', -80 : '80 S', -70 : '70 S', -60 : '60 S', -50 : '50 S', -40 : '40 S', -30 : '30 S', -20 : '20 S', -10 : '10 S', 0 : '0', 10: '10 N', 20 : '20 N', 30 : '30 N', 40 : '40 N', 50 : '50 N', 60 : '60 N', 70 : '70 N', 80 : '80 N', 90 : '90 N'}

app = Dash(__name__)
server = app.server
app.layout = html.Div(
    [
        html.H1("AIS Fishing Effort Analysis in the USA", style={'textAlign': 'center'}),

        html.Label("Latitude"),
        dcc.RangeSlider(min=df['cell_ll_lat'].min(),
                   max=df['cell_ll_lat'].max(),
                   step=1,
                  # value=13,
                  marks=rangeslider_marks,
                  value=[0,10],
                   tooltip={"placement": "bottom", "always_visible": True},
                   updatemode='drag',
                  # persistence=True,
                   # persistence_type='session', # 'memory' or 'local'
                   id="my-rangeslider"
        ),

        
        html.Label("Longitude"),
        dcc.RangeSlider(min=df['cell_ll_lon'].min(),
                        max=df['cell_ll_lon'].max(),
                        step=1,
                        marks=rangeslider_marks,
                        value=[0,10],
                        tooltip={"placement": "bottom", "always_visible": True},
                        updatemode='drag',
                        id="my-rangeslider"
        ),

        
        
        

        dcc.Graph(id='my-graph')
    ],
    
    style={"margin": 30}
)


@app.callback(
    Output('my-graph', 'figure'),
    Input('my-slider', 'value'),
    Input('my-rangeslider', 'value')
)
def update_graph():
    bool_series = df['cell_ll_lat']
    df_filtered = df[bool_series]
    fig = px.bar(data_frame=df_filtered,
                 x='Year',
                 y='latidute',
                 range_y=[df['cell_ll_lat'].min(), df['cell_ll_lat'].max()],
                 range_x=[df['hour'].min()-1, df['hour'].max()+1])

    '''

    bool_series2 = df['cell_ll_lon']
    filtered_year = df[bool_series2]['hour'].values
    fig["data"][0]["marker"]["color"] = ["orange" if c in filtered_year else "blue" for c in fig["data"][0]["x"]]

    '''

    return fig


if __name__ == "__main__":
    #app.run(debug=True)
    app.run_server(debug=True)