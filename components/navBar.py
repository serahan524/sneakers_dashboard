import dash_bootstrap_components as dbc


# Build Componenets
# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# Create navigation bar
links = [
    {"id": "page-1-link", "href": "/", "link-text": "Sneakers Tracker"},
    {"id": "page-2-link", "href": "/compare", "link-text": "Compare"},
    {"id": "page-3-link", "href": "/explore", "link-text": "Explore"},
]

navbar = dbc.Navbar(
            dbc.Container(
                [
                    dbc.Row([
                        dbc.Col([
                            dbc.Nav([
                                dbc.NavItem(dbc.NavLink(link["link-text"], 
                                                        href=link["href"], 
                                                        id=link["id"], 
                                                        active="exact",
                                                        className="nav-link", 
                                                        external_link=True)
                                )
                                for link in links                                
                            ],
                            pills=True,
                            )
                        ],
                        width={"size":"auto"}),
                    ],
                    align="center"),                    
                ],
            fluid=True
            ),
    color="#FFFFFF",
)


# # Call back
# @app.callback(
#     [Output(link["id"], "active") for link in links],
#     Input("url", "pathname"),
    
# )

# # Call navbar function
# def display_page(pathname):
#     actives_list = [False for link in links]

#     if pathname == "/":
#         return actives_list

#     actives_list[int(pathname[-1]) - 1] = True
#     print (actives_list)
#     return actives_list


