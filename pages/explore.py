from dash import html
from components import explore_layout,navBar
import dash

dash.register_page(__name__,path='/explore')

layout = html.Div(className="body", children=[
    navBar.navbar,
    explore_layout.layout,
])