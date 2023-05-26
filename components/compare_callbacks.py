<<<<<<< HEAD
import plotly.express as px
import pandas as pd

from dash import Output, Input, State

=======
import dash
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from dash import html, Output, Input, State, dcc, MATCH, ALL
from dash.exceptions import PreventUpdate
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93

df1 = pd.read_csv("StockX_2019.csv")
df1 = pd.DataFrame(df1)
df1["Order Date"] = pd.to_datetime(df1["Order Date"])
df2 = pd.read_csv("sneakers.csv")
df2 = pd.DataFrame(df2)

def get_callbacks(app):


    # Dropdowns options

    option = df1[["Brand", "Sneaker Name", "Shoe Size"]].copy()
    val_all = []
    val_all.insert(0, {"Brand": "Select", "Sneaker Name": "Select", "Shoe Size": "Select"})
    option = pd.concat([pd.DataFrame(val_all), option], ignore_index=True)

    brands = option["Brand"].unique()
    s_names = option["Sneaker Name"].unique()
    sizes = option["Shoe Size"].unique()


    # Dropdown for first compare Brand
    @app.callback(
        Output("compare_option_1_brand", "options"),
        Output("compare_option_1_brand", "value"),
<<<<<<< HEAD
        Input("compare_option_1_brand", "n_clicks"),
=======
        Input("compare_option_1_brand", "search_value"),
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93
    )

    def update_options_first(search_value):
        return [{"label": i, "value": i} for i in brands], "Select"

    # Dropdown for first compare Model
    @app.callback(
        Output("compare_option_1_model", "options"),
        Output("compare_option_1_model", "value"),
<<<<<<< HEAD
        Input("compare_option_1_model", "n_clicks"),
=======
        Input("compare_option_1_model", "search_value"),
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93
        Input("compare_option_1_brand","value")
    )
    def update_options_second(search_value,value):
        if value == "Select":
            return [{"label": i, "value": i} for i in s_names], "Select"

<<<<<<< HEAD
        elif value == "Adidas":
            filt = option["Brand"]=="Adidas"
=======
        elif value == " Yeezy":
            filt = option["Brand"]==" Yeezy"
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93
            opt1 = option[filt]

            s_name = opt1["Sneaker Name"].unique()
            #print("Yeezy")
            #print(s_name)
            return [{"label": i, "value": i} for i in s_name], "Select"

        else:
<<<<<<< HEAD
            filt = option["Brand"] == "Nike"
=======
            filt = option["Brand"] == "Off-White"
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93
            opt1 = option[filt]
            s_name = opt1["Sneaker Name"].unique()
            #print(s_name)
            return [{"label": i, "value": i} for i in s_name], "Select"

    # Dropdown for second compare Model
    @app.callback(
        Output("compare_option_2_model", "options"),
        Output("compare_option_2_model", "value"),
<<<<<<< HEAD
        Input("compare_option_2_model", "n_clicks"),
=======
        Input("compare_option_2_model", "search_value"),
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93
        Input("compare_option_2_brand","value")
        )

    def update_options_third(search_value,value):
        if value == "Select":
            return [{"label": i, "value": i} for i in s_names], "Select"

<<<<<<< HEAD
        elif value == "Adidas":
            filt = option["Brand"]=="Adidas"
=======
        elif value == " Yeezy":
            filt = option["Brand"]==" Yeezy"
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93
            opt1 = option[filt]

            s_name = opt1["Sneaker Name"].unique()
            #print("Yeezy")
            #print(s_name)
            return [{"label": i, "value": i} for i in s_name], "Select"

        else:
<<<<<<< HEAD
            filt = option["Brand"] == "Nike"
=======
            filt = option["Brand"] == "Off-White"
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93
            opt1 = option[filt]
            s_name = opt1["Sneaker Name"].unique()
            #print(s_name)
            return [{"label": i, "value": i} for i in s_name], "Select"

    # Dropdown for second compare Brand
    @app.callback(
        Output("compare_option_2_brand", "options"),
        Output("compare_option_2_brand", "value"),
<<<<<<< HEAD
        Input("compare_option_2_brand", "n_clicks"),
=======
        Input("compare_option_2_brand", "search_value"),
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93
        )
    def update_options_forth(search_value):
        return [{"label": i, "value": i} for i in brands], "Select"

    @app.callback(
        Output("option-1-graph-model","children"),
        Input("search-op1","n_clicks"),
        State("compare_option_1_model","value"),
    )
    def update_comp1_tile(n,serach_value):
        return serach_value

    @app.callback(
        Output("option-2-graph-model", "children"),
        Input("search-op2", "n_clicks"),
        State("compare_option_2_model", "value"),
    )
    def update_comp2_tile(n, serach_value):
        return serach_value

    @app.callback(
        Output("op1-price","children"),
        Input("search-op1","n_clicks"),
        State("compare_option_1_model","value"),
    )
    def update_op1_price(n,search_value):
        if search_value =="Select" or search_value==None:
            return "0"
        else:
            dff1 = df1[["Sneaker Name","Sale Price"]]
            filt = (dff1["Sneaker Name"]==search_value)
            dff2 = dff1[filt]
            dff3 = dff2.groupby(["Sneaker Name"]).mean()
            #print(dff3["Sale Price"].iat[0])
            return (dff3["Sale Price"].iat[0]).round(2)
    @app.callback(
        Output("op1-Retail","children"),
        Input("search-op1","n_clicks"),
        State("compare_option_1_model","value"),
    )
    def update_op1_retail(n,value):
        if value == "Select" or value == None:
            return "0"
        else:
            dff1 = df1[["Sneaker Name","Retail Price"]]
            filt = (dff1["Sneaker Name"]==value)
            dff2 = dff1[filt]
            dff3 = dff2["Retail Price"].iat[0]
            return dff3
    @app.callback(
        Output("op1-volati","children"),
        Input("search-op1","n_clicks"),
        State("compare_option_1_model","value")
    )
    def update_op1_volati(n,value):
        if value =="Select" or value == None:
            return "0"
        else:
            dff1 = df2[["item","volatility"]]
            #print(dff1)
            filt = dff1["item"]==value
            dff2 = dff1[filt]
            print(len(dff2))
            if len(dff2) > 0:
                dff3 = dff2.groupby(["item"]).mean()
                return dff3["volatility"].iat[0]
            else:
                return "0"
            # return "100"
    @app.callback(
        Output("op1-inc","children"),
        Input("search-op1","n_clicks"),
        State("compare_option_1_model","value"),
    )
    def update_op1_inc(n,value):
        if value =="Select" or value == None:
            return 0
        else:
            rp1 = df1[["Sneaker Name", "Retail Price"]]
            filt = (rp1["Sneaker Name"] == value)
            rp2 = rp1[filt]
            rp3 = rp2["Retail Price"].iat[0]
            #print(rp3)

            p1 = df1[["Sneaker Name", "Sale Price"]]
            filt = (p1["Sneaker Name"] == value)
            p2 = p1[filt]
            p3 = p2.groupby(["Sneaker Name"]).mean()
            #print(p3["Sale Price"].iat[0])
            #print((p3["Sale Price"].iat[0])-rp3)

            price = ((p3["Sale Price"].iat[0])-rp3).round(2)
            return price
    @app.callback(
            Output("op2-price", "children"),
            Input("search-op2", "n_clicks"),
            State("compare_option_2_model", "value"),
        )
    def update_op2_price(n, search_value):
            if search_value == "Select" or search_value == None:
                return "0"
            else:
                dff1 = df1[["Sneaker Name", "Sale Price"]]
                filt = (dff1["Sneaker Name"] == search_value)
                dff2 = dff1[filt]
                dff3 = dff2.groupby(["Sneaker Name"]).mean()
                # print(dff3["Sale Price"].iat[0])
                return (dff3["Sale Price"].iat[0]).round(2)

    @app.callback(
            Output("op2-Retail", "children"),
            Input("search-op2", "n_clicks"),
            State("compare_option_2_model", "value"),
        )
    def update_op2_retail(n, value):
            if value == "Select" or value == None:
                return "0"
            else:
                dff1 = df1[["Sneaker Name", "Retail Price"]]
                filt = (dff1["Sneaker Name"] == value)
                dff2 = dff1[filt]
                dff3 = dff2["Retail Price"].iat[0]
                return dff3

    @app.callback(
            Output("op2-volati", "children"),
            Input("search-op2", "n_clicks"),
            State("compare_option_2_model", "value")
        )
    def update_op2_volati(n, value):
            if value == "Select" or value == None:
                return "0"
            else:
                dff1 = df2[["item", "volatility"]]
                # print(dff1)
                filt = dff1["item"] == value
                dff2 = dff1[filt]
                print(len(dff2))
                if len(dff2) > 0:
                    dff3 = dff2.groupby(["item"]).mean()
                    return dff3["volatility"].iat[0]
                else:
                    return "0"
                # return "100"

    @app.callback(
            Output("op2-inc", "children"),
            Input("search-op2", "n_clicks"),
            State("compare_option_2_model", "value"),
        )
    def update_op2_inc(n, value):
            if value == "Select" or value == None:
                return 0
            else:
                rp1 = df1[["Sneaker Name", "Retail Price"]]
                filt = (rp1["Sneaker Name"] == value)
                rp2 = rp1[filt]
                rp3 = rp2["Retail Price"].iat[0]
                # print(rp3)

                p1 = df1[["Sneaker Name", "Sale Price"]]
                filt = (p1["Sneaker Name"] == value)
                p2 = p1[filt]
                p3 = p2.groupby(["Sneaker Name"]).mean()
                # print(p3["Sale Price"].iat[0])
                # print((p3["Sale Price"].iat[0])-rp3)

                price = ((p3["Sale Price"].iat[0]) - rp3).round(2)
                return price
    @app.callback(
        Output("op1-line-chart","figure"),
        Input("search-op1","n_clicks"),
        State("compare_option_1_model","value"),
    )
    def update_op1_chart(n,value):

        if value =="Select" or value == None:
            fig_line = ""
            filt = df1["Sneaker Name"] == value
            dfm = df1[filt]
            print(dfm)
        else:
            filt = df1["Sneaker Name"] == value
            dfm = df1[filt]
            print(dfm)
            fig_line = px.line(dfm,
                               x="Order Date",
                               y="Sale Price",
                               )
<<<<<<< HEAD
            fig_line.update_yaxes(title='Sale Price')
            fig_line.update_xaxes(title='Order Date')
            fig_line.update_layout(font=dict(size=10), height=400)
            fig_line.update_traces(line_color="#006340")
=======
            fig_line.update_yaxes(title='')
            fig_line.update_xaxes(title='')
            fig_line.update_layout(font=dict(size=10))
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93

            # fig = px.line(dfm, x="Order Date",
            #               y="Sale Price",
            #               labels={"Sale Price": "Sale Price ($)"})
        return fig_line

    @app.callback(
        Output("op2-line-chart","figure"),
        Input("search-op2","n_clicks"),
        State("compare_option_2_model","value")
    )
    def update_op2_char(n,value):
        if value == "Select" or value == None:
            fig_line = ""
            filt = df1["Sneaker Name"] == value
            dfm = df1[filt]
            print(dfm)
        else:
            filt = df1["Sneaker Name"] == value
            dfm = df1[filt]
            print(dfm)
            fig_line = px.line(dfm,
                               x="Order Date",
                               y="Sale Price",
                               )
<<<<<<< HEAD
            fig_line.update_yaxes(title='Sale Price')
            fig_line.update_xaxes(title='Order Date')
            fig_line.update_layout(font=dict(size=10),height = 400)
            fig_line.update_traces(line_color="#006340")
=======
            fig_line.update_yaxes(title='')
            fig_line.update_xaxes(title='')
            fig_line.update_layout(font=dict(size=10))
>>>>>>> 2c4385f44b679830def5d47fe0d55447d8545c93

            # fig = px.line(dfm, x="Order Date",
            #               y="Sale Price",
            #               labels={"Sale Price": "Sale Price ($)"})
        return fig_line