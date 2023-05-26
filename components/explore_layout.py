from dash import html, dcc

import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import pandas as pd                      # pip install pandas




#print(df3['gender'].unique())

# Import data
df1 = pd.read_csv("StockX_2019.csv",parse_dates=['Order Date','Release Date'], date_parser=pd.to_datetime, skipinitialspace = True)
df2 = pd.read_csv("sneakers.csv")
df3 = pd.read_csv("jordan_data.csv")

df1['Brand'].str.strip()

brand_list = df1['Brand'].unique()
brand_choices = [{'label':name, 'value':name} for name in brand_list]
brand_choices.insert(0,{'label':'All', 'value':'All'})





shoe_df = df1['Shoe Size']
shoe_sizes = sorted(shoe_df.unique())
shoe_sizes_drop = [{'label':float(s), 'value':s} for s in shoe_sizes]
shoe_sizes_drop.insert(0,{'label':'All', 'value':-1})
default = shoe_sizes[7:21]













#defne the heatmap card here:
heatmap_card = dbc.Card([
                dbc.CardBody([
                    html.Div([
                        #html.H5('Number of Sales by Day of Week'),
                        dcc.Graph(id='heatmap'),
                        # html.Div(id='test-output')
                    ], style={'textAlign':'center'})

                ])
            ], style={'height': 500 })

#define the filtering options card here
filter_card = dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.H5('Filtering Options')
                    ], style={'textAlign':'center'}),
                    dbc.Col([
                        html.Label([
                        html.H6('Filter by Brand')
                    ], style={'textAlign': 'left'}),
                        dcc.Dropdown(
                            id="brand-input",
                            options=brand_choices,
                            value='All'
                        ),
                        html.Label([
                        html.H6('Filter by Size')
                        ], style={'textAlign': 'left'}),
                        dcc.Checklist(
                            id="size-input",
                            options=shoe_sizes,
                            value=default,
                            labelStyle={"display": "inline-block"}

                        )

                    ])
                    


                ])
            ], style={'height': 350})

#define choropleth map here:
choropleth_card = dbc.Card([
                dbc.CardBody([
                    html.Div([
                        dcc.Graph(id='choropleth'),
                    ], style={'textAlign':'center'})

                ])
            ], style={'height': 500})

#define choropleth options here:
choropleth_filter_card =  dbc.Card([
                dbc.CardBody([
                    dbc.Col([
                        html.Div([
                            html.H5('Filtering Choropleth Options')
                            ], style={'textAlign':'center'})]),
                        html.H6('Filter by Size'),
                        dcc.Dropdown(
                            id="size-choro-input",
                            options=shoe_sizes_drop,
                            value=-1,
                        ),
                        
                        

                ])
            ], style={'height': 350})




layout = dbc.Container([
    dbc.Row([
        dbc.Col(heatmap_card),
        dbc.Col(choropleth_card),
    ]),
    dbc.Row([
        dbc.Col(filter_card),
        dbc.Col(choropleth_filter_card),
    ])
   


])


    
