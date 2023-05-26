import dash
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from dash import html, Output, Input, State, dcc, MATCH, ALL
from dash.exceptions import PreventUpdate


# Import data
df1 = pd.read_csv("StockX_2019.csv")
df1 = pd.DataFrame(df1)
df2 = pd.read_csv("sneakers.csv")
df2 = pd.DataFrame(df2)

print(df2.dtypes)

# dff1 = df1[["Sneaker Name","Sale Price"]]
# print(dff1),
#
# dff2 = (dff1["Sale Price"]==1097)
# dff3 = (dff1["Sneaker Name"] == "Adidas Yeezy Boost 350 Low V2 Beluga")
# print(dff3)
# dff4 = dff1[dff3]
# print(dff4)
# dff5 = dff4.groupby(["Sneaker Name"]).mean()
# dff5.reset_index(inplace=True)
# print(dff5)
# #filt = (dff1['Sneaker Name']. == 'Adidas Yeezy Boost 350 Low V2 Beluga')
# dff2 = (df1[['Sneaker Name']=="Adidas Yeezy Boost 350 V2 Core Black Red"])
# print(dff2)