from dash import html
from components import home_layout, navBar
import dash

dash.register_page(__name__,path='/')

layout = html.Div(className="body", children=[
    navBar.navbar,
    home_layout.layout,
    
])