import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

app = dash.Dash()

df = pd.read_csv('part2/tEOSUSD_feature_minute.csv')
df1 = pd.read_csv('part2/tBTCUSD_feature_minute.csv')
df.reset_index(inplace=True)
df.set_index("hour_minute", inplace=True)
df1.reset_index(inplace=True)
df1.set_index("hour_minute", inplace=True)
df2 = pd.read_csv('part2/tLTCUSD_feature_minute.csv')
df3 = pd.read_csv('part2/tETCUSD_feature_minute.csv')
df2.reset_index(inplace=True)
df2.set_index("hour_minute", inplace=True)
df3.reset_index(inplace=True)
df3.set_index("hour_minute", inplace=True)

app.layout = html.Div([
    
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'BTCUSD', 'value': 'BTCUSD'},
            {'label': 'EOSUSD', 'value': 'EOSUSD'},
            {'label': 'ETCUSD', 'value': 'ETCUSD'},
            {'label': 'LTCUSD', 'value': 'LTCUSD'}
        ],
        value='BTCUSD'
    ),
    dcc.Graph(
        id='EOSUSD',
        figure={
            'data': [
                {'x': df.index, 'y': df.close, 'type': 'line', 'name': 'close'},
                {'x': df.index, 'y': df.open, 'type': 'line', 'name': 'open'},
                {'x': df.index, 'y': df.high, 'type': 'line', 'name': 'high'},
                {'x': df.index, 'y': df.low, 'type': 'line', 'name': 'low'},
                {'x': df.index, 'y': df.average, 'type': 'line', 'name': 'average'}


            ],
            'layout': {
                'title': 'EOSUSD'
            }
        }
    ),
    
    dcc.Graph(
        id='LTCUSD',
        figure={
            'data': [
                {'x': df2.index, 'y': df2.close, 'type': 'line', 'name': 'close'},
                {'x': df2.index, 'y': df2.open, 'type': 'line', 'name': 'open'},
                {'x': df2.index, 'y': df2.high, 'type': 'line', 'name': 'high'},
                {'x': df2.index, 'y': df2.low, 'type': 'line', 'name': 'low'},
                {'x': df2.index, 'y': df2.average, 'type': 'line', 'name': 'average'}


            ],
            'layout': {
                'title': 'LTCUSD'
            }
        }
    ),
    
    dcc.Graph(
        id='ETCUSD',
        figure={
            'data': [
                {'x': df3.index, 'y': df3.close, 'type': 'line', 'name': 'close'},
                {'x': df3.index, 'y': df3.open, 'type': 'line', 'name': 'open'},
                {'x': df3.index, 'y': df3.high, 'type': 'line', 'name': 'high'},
                {'x': df3.index, 'y': df3.low, 'type': 'line', 'name': 'low'},
                {'x': df3.index, 'y': df3.average, 'type': 'line', 'name': 'average'}


            ],
            'layout': {
                'title': 'ETCUSD'
            }
        }
    ),
    
    
    
    dcc.Graph(
        id='BTCUSD',
        figure={
            'data': [
                {'x': df1.index, 'y': df1.close, 'type': 'line', 'name': 'close'},
                {'x': df1.index, 'y': df1.open, 'type': 'line', 'name': 'open'},
                {'x': df1.index, 'y': df1.high, 'type': 'line', 'name': 'high'},
                {'x': df1.index, 'y': df1.low, 'type': 'line', 'name': 'low'},
                {'x': df1.index, 'y': df1.average, 'type': 'line', 'name': 'average'}


            ],
            'layout': {
                'title': 'BTCUSD'
            }
        }
    ),
    html.Div(id='output-container')
])


@app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('my-dropdown', 'value')])
def update_output(value):x
    if value == 'BTCUSD':
        print ('yes')


if __name__ == '__main__':
    app.run_server(debug=True)