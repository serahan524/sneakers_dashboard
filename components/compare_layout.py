<<<<<<< HEAD
from dash import html, dcc

import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import pandas as pd                      # pip install pandas
=======
from dash import Dash, html, dcc
from dash.dependencies import Output, Input

from dash_extensions import Lottie       # pip install dash-extensions
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import plotly.express as px              # pip install plotly
import pandas as pd                      # pip install pandas
from wordcloud import WordCloud          # pip install wordcloud
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93
import dash_html_components as html

df1 = pd.read_csv("StockX_2019.csv")
df2 = pd.read_csv("sneakers.csv")

compare_layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div(children=[
                        html.Div([
                            html.Label(['Brand']),
                            dcc.Dropdown(
                                id='compare_option_1_brand',
                                clearable=False,
                            ),
                        ], style={"width": "33%", "margin-left": "10px", "font-size": "75%"}),
                        html.Div([
                            html.Label(['Model']),
                            dcc.Dropdown(
                                id='compare_option_1_model',
                                clearable=False,
                                disabled=False
                            ),
                        ], style={"width": "65%", "margin-left": "20px", "font-size": "75%"}),
                        html.Div([

                            dbc.Button("SEARCH",color='success', className="ne-1",id="search-op1",n_clicks=0),
                        ], style={"width": "33%", "margin-left": "70px", "font-size": "85%"})
                    ], style=dict(display='flex')),
                ]),
            ]),
            dbc.Card([
                dbc.CardBody([
                    html.Div(id="option-1-graph-model",children=["Model"]),
                    dcc.Graph(
                        id='op1-line-chart',
                        figure={
                            "layout" : {
                            "height": 130,
                        }},
<<<<<<< HEAD
                        style={"maxHeight": "350px", "overflow-y": "scroll"},
                        ),
                ])
            ], style={"height": 400}),
=======
                        style={"maxHeight": "130px", "overflow-y": "scroll"},
                        ),
                ])
            ], style={"height": 230}),
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93
            html.Br(),
        ]),
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Div(children=[

                            html.Div([
                                html.Label(['Brand']),
                                dcc.Dropdown(
                                    id='compare_option_2_brand',
                                    clearable=False,
                                ),
                            ], style={"width": "33%", "margin-left": "10px", "font-size": "75%"}),
                            html.Div([
                                html.Label(['Model']),
                                dcc.Dropdown(
                                    id='compare_option_2_model',
                                    clearable=False,
                                    disabled=False
                                ),
                            ], style={"width": "65%", "margin-left": "20px", "font-size": "75%"}),
                            html.Div([

                                dbc.Button("SEARCH", color='success', className="ne-1", id="search-op2"),
                                 ], style={"width": "33%", "margin-left": "70px", "font-size": "55%"})
                            ], style=dict(display='flex')),

                            ]),
                    ]),
            dbc.Card([
                html.Div(id="option-2-graph-model",children=["Model"]),
                dbc.CardBody([
                    dcc.Graph(
                        id='op2-line-chart',
                        figure={
                            "layout": {
                                "height": 130,
                            }},
<<<<<<< HEAD
                        style={"maxHeight": "350px", "overflow-y": "scroll"},
                    ),
                ])
            ], style={"height": 400}),
=======
                        style={"maxHeight": "130px", "overflow-y": "scroll"},
                    ),
                ])
            ], style={"height": 230}),
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93
            html.Br(),
        ])
    ]),

    dbc.Row([
        #selected type statistic
<<<<<<< HEAD
        #dbc.Col([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Label('Price $'),
                        html.Div(id="op1-price", children=["0"]),
                    ])
                ], style={"width":"80%"}),
                dbc.Card([
                    dbc.CardBody([
                        html.Label('Retail Price $'),
                        html.Div(id="op1-Retail",children=["0"]),
                    ])
                ], style={"width":"80%"}),
            ]),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
=======
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Label('Price $'),
                    html.Div(id="op1-price", children=["0"]),
                ])
            ], style={"width":"80%"}),
            dbc.Card([
                dbc.CardBody([
                    html.Label('Retail Price $'),
                    html.Div(id="op1-Retail",children=["0"]),
                ])
            ], style={"width":"80%"}),
            dbc.Card([
                dbc.CardBody([
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93
                    html.Label('Mean Volatility'),
                    html.Div(id="op1-volati",children=["0"]),
                ])
            ], style={"width":"80%"}),
            dbc.Card([
                dbc.CardBody([
                    html.Label('Total Increase $'),
                    html.Div(id="op1-inc",children=["0"]),
                ])
            ], style={"width":"80%"}),
<<<<<<< HEAD
        ]),
        #], width=2, style={"height": '100%'}),

        #shoe first example card of first choice
        # dbc.Col([
        #     dbc.Card([
        #         dbc.CardImg(src="/assets/X_Gray_Digital_RGB.png",
        #                     top=True,
        #                     className="img-fluid rounded-start",
        #                     style={'height': '40%', 'width': '100%', 'display': 'block', 'margin-left': 5,
        #                            'margin-right': 5}
        #                     ),
        #         dbc.CardBody([
        #             # dcc.Graph(
        #             #     id='op1-line-chart',
        #             #     figure={
        #             #         "layout": {
        #             #             "height": 290,
        #             #         }
        #             #     }
        #             # ),
        #         ], style={"padding-top": 0, "padding-bottom": 0}, )
        #     ], id="compare-card-1", style={"height": 300, "width": 200,"margin-left":"1px"}),
        # ]),
        #     dbc.Col([
        #     dbc.Card([
        #         dbc.CardImg(src="/assets/X_Gray_Digital_RGB.png",
        #                     top=True,
        #                     className="img-fluid rounded-start",
        #                     style={'height': '40%', 'width': '100%', 'display': 'block', 'margin-left': 5,
        #                            'margin-right': 5}
        #                     ),
        #         dbc.CardBody([
        #             # dcc.Graph(
        #             #     id={
        #             #         'type': 'line-chart',
        #             #         'index': "1"
        #             #     },
        #             #     figure={
        #             #         "layout": {
        #             #             "height": 195,
        #             #         }
        #             #     },
        #             #     config={'displayModeBar': False},
        #             # ),
        #         ], style={"padding-top": 0, "padding-bottom": 0}, )
        #     ], id="compare-card-2", style={"height": 300, "width": 200})
        #
        # ]),
=======

        ], width=2, style={"height": '100%'}),

        #shoe first example card of first choice
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src="/assets/X_Gray_Digital_RGB.png",
                            top=True,
                            className="img-fluid rounded-start",
                            style={'height': '40%', 'width': '100%', 'display': 'block', 'margin-left': 5,
                                   'margin-right': 5}
                            ),
                dbc.CardBody([
                    # dcc.Graph(
                    #     id='op1-line-chart',
                    #     figure={
                    #         "layout": {
                    #             "height": 290,
                    #         }
                    #     }
                    # ),
                ], style={"padding-top": 0, "padding-bottom": 0}, )
            ], id="compare-card-1", style={"height": 300, "width": 200,"margin-left":"1px"}),
        ]),
            dbc.Col([
            dbc.Card([
                dbc.CardImg(src="/assets/X_Gray_Digital_RGB.png",
                            top=True,
                            className="img-fluid rounded-start",
                            style={'height': '40%', 'width': '100%', 'display': 'block', 'margin-left': 5,
                                   'margin-right': 5}
                            ),
                dbc.CardBody([
                    # dcc.Graph(
                    #     id={
                    #         'type': 'line-chart',
                    #         'index': "1"
                    #     },
                    #     figure={
                    #         "layout": {
                    #             "height": 195,
                    #         }
                    #     },
                    #     config={'displayModeBar': False},
                    # ),
                ], style={"padding-top": 0, "padding-bottom": 0}, )
            ], id="compare-card-2", style={"height": 300, "width": 200})

        ]),
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93

        #second example for the first choice
        #dbc.Col([]),

        # selected type statistic
<<<<<<< HEAD
        #dbc.Col([
=======
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Label('Price $'),
                    html.Div(id="op2-price", children=["0"]),
                ])
            ], style={"width":"80%"}),
            dbc.Card([
                dbc.CardBody([
                    html.Label('Retail Price $'),
                    html.Div(id="op2-Retail",children=["0"]),
                ])
            ], style={"width":"80%"}),
<<<<<<< HEAD
        ]),
            dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Label('Mean Volatility'),
                            html.Div(id="op2-volati",children=["0"]),
                        ])
                    ], style={"width":"80%"}),
                    dbc.Card([
                        dbc.CardBody([
                            html.Label('Total Increase $'),
                            html.Div(id="op2-inc",children=["0"]),
                        ])
                    ], style={"width":"80%"}),
                ])
        #], width=2, style={"height": '100%'}),

        #first example of second choice

            # dbc.Col([
            #
            # dbc.Card([
            #     dbc.CardImg(src="/assets/X_Gray_Digital_RGB.png",
            #                 top=True,
            #                 className="img-fluid rounded-start",
            #                 style={'height': '40%', 'width': '100%', 'display': 'block', 'margin-left': 5,
            #                        'margin-right': 5}
            #                 ),
            #     dbc.CardBody([
            #         # dcc.Graph(
            #         #     id={
            #         #         'type': 'line-chart',
            #         #         'index': "1"
            #         #     },
            #         #     figure={
            #         #         "layout": {
            #         #             "height": 195,
            #         #         }
            #         #     },
            #         #     config={'displayModeBar': False},
            #         # ),
            #     ], style={"padding-top": 0, "padding-bottom": 0}, )
            # ], id="card-1", style={"height": 300, "width": 200},className="m-0"),
            #
            # ]),
        #second example of second choice
        # dbc.Col([
        #     dbc.Card([
        #         dbc.CardImg(src="/assets/X_Gray_Digital_RGB.png",
        #                     top=True,
        #                     className="img-fluid rounded-start",
        #                     style={'height': '40%', 'width': '100%', 'display': 'block', 'margin-left': "1px",
        #                            'margin-right': "1px"}
        #                     ),
        #         dbc.CardBody([
        #             # dcc.Graph(
        #             #     id={
        #             #         'type': 'line-chart',
        #             #         'index': "1"
        #             #     },
        #             #     figure={
        #             #         "layout": {
        #             #             "height": 195,
        #             #         }
        #             #     },
        #             #     config={'displayModeBar': False},
        #             # ),
        #         ], style={"padding-top": 0, "padding-bottom": 0,"margin-left":"1px"}, )
        #     ], id="card-1", style={"height": 300, "width": 200,"margin-left":"1px"})
        #
        # ],style={'margin-right': '0px', 'margin-left': '0px'}),

    ]),
=======
            dbc.Card([
                dbc.CardBody([
                    html.Label('Mean Volatility'),
                    html.Div(id="op2-volati",children=["0"]),
                ])
            ], style={"width":"80%"}),
            dbc.Card([
                dbc.CardBody([
                    html.Label('Total Increase $'),
                    html.Div(id="op2-inc",children=["0"]),
                ])
            ], style={"width":"80%"}),
        ], width=2, style={"height": '100%'}),

        #first example of second choice

            dbc.Col([

            dbc.Card([
                dbc.CardImg(src="/assets/X_Gray_Digital_RGB.png",
                            top=True,
                            className="img-fluid rounded-start",
                            style={'height': '40%', 'width': '100%', 'display': 'block', 'margin-left': 5,
                                   'margin-right': 5}
                            ),
                dbc.CardBody([
                    # dcc.Graph(
                    #     id={
                    #         'type': 'line-chart',
                    #         'index': "1"
                    #     },
                    #     figure={
                    #         "layout": {
                    #             "height": 195,
                    #         }
                    #     },
                    #     config={'displayModeBar': False},
                    # ),
                ], style={"padding-top": 0, "padding-bottom": 0}, )
            ], id="card-1", style={"height": 300, "width": 200},className="m-0"),

            ]),
        #second example of second choice
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src="/assets/X_Gray_Digital_RGB.png",
                            top=True,
                            className="img-fluid rounded-start",
                            style={'height': '40%', 'width': '100%', 'display': 'block', 'margin-left': "1px",
                                   'margin-right': "1px"}
                            ),
                dbc.CardBody([
                    # dcc.Graph(
                    #     id={
                    #         'type': 'line-chart',
                    #         'index': "1"
                    #     },
                    #     figure={
                    #         "layout": {
                    #             "height": 195,
                    #         }
                    #     },
                    #     config={'displayModeBar': False},
                    # ),
                ], style={"padding-top": 0, "padding-bottom": 0,"margin-left":"1px"}, )
            ], id="card-1", style={"height": 300, "width": 200,"margin-left":"1px"})

        ],style={'margin-right': '0px', 'margin-left': '0px'}),

    ], className="m-0"),
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93
    ])

