from dash import html
from components import navBar, compare_layout
import dash


dash.register_page(__name__,path='/compare')

layout = html.Div(className="body", children=[
    navBar.navbar,
    compare_layout.compare_layout,
    #html.H3(children="Compare page"),

])