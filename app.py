import dash
import dash_bootstrap_components as dbc
from dash import html

<<<<<<< HEAD
=======
from dash import html, Output, Input, State, dcc 
from dash.exceptions import PreventUpdate

>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93
from components import home_callbacks,compare_callbacks,explore_callbacks


app = dash.Dash(__name__,use_pages=True,external_stylesheets=[dbc.themes.UNITED, dbc.icons.BOOTSTRAP],suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div(children=[
    dash.page_container
])

home_callbacks.get_callbacks(app)
compare_callbacks.get_callbacks(app)
<<<<<<< HEAD
explore_callbacks.get_callbacks(app)
=======
#explore_callbacks.get_callbacks(app)
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93

if __name__ == "__main__":
    app.run_server( port=8051)