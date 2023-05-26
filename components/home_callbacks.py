import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd  
import os.path
from dash import Output, Input, State, dcc, MATCH



# Import data
df1 = pd.read_csv("StockX_2019.csv")
df2 = pd.read_csv("sneakers.csv")


def get_callbacks(app):

    # Bar Graph
    @app.callback(
        Output('bar-chart','figure'),
        Input('pandas-dropdown-1', 'value'),
    )
    def update_bar(value):
        dff1 = df1.copy()
        dff2 = df2.copy()
        if value == 'Price':
            dff1.sort_values(by=['Sale Price'], inplace=True, ascending=True)
            dff1 = dff1.drop_duplicates(subset=['Sneaker Name'])
            fig_bar = px.bar(dff1,
                        x="Sale Price",
                        y="Sneaker Name",
                        orientation='h',
                        height=1500,
            )
            fig_bar.update_traces(marker_color='#006340')
            fig_bar.update_layout(plot_bgcolor="white")
            fig_bar.update_xaxes(
                showgrid=True,
                gridcolor='#e2ede9',
            )
            fig_bar.update_yaxes(
                showgrid=True,
                gridcolor='#e2ede9',
            )

        elif value == 'Volatility':
            dff2.sort_values(by=['volatility'], inplace=True, ascending=True)
            fig_bar = px.bar(dff2,
                        x="volatility",
                        y="item",
                        orientation='h',
                        height=1500,
            )
            fig_bar.update_traces(marker_color='#006340')
            fig_bar.update_layout(plot_bgcolor="white")
            fig_bar.update_xaxes(
                showgrid=True,
                gridcolor='#e2ede9'
            )
            fig_bar.update_yaxes(
                showgrid=True,
                gridcolor='#e2ede9'
            )
        return fig_bar

    
    # Dropdowns in bottom area
    option = df1[["Brand", "Sneaker Name", "Shoe Size"]].copy()
    val_all = []
    val_all.insert(0, {"Brand": "All", "Sneaker Name": "All", "Shoe Size": "All"})
    option = pd.concat([pd.DataFrame(val_all), option], ignore_index=True)

    brands = option["Brand"].unique()
    s_names = option["Sneaker Name"].unique()
    sizes = option["Shoe Size"].unique()

    # Calling multiple cards 
    def make_card(n_add):
        card = []

        
        for n in range(0, n_add-1):
            card.append(dbc.Card([   
                dbc.CardImg(
                        id={
                            'type': 'image', 
                            'index' : n
                        },
                        top=True,
                        className="img-fluid rounded-start",
                        style={'height':'40%', 'width':'100%', 'display': 'block', 'margin-left': 5, 'margin-right': 5}
                ),
                   
                dbc.CardBody([
                    #html.Div(s_names[n]+"\n\nSize: "+str(size[n]), style={"margin-top": -10}),
                    dcc.Graph(
                        id={
                            'type': 'line-chart', 
                            'index' : n
                        },
                        figure={
                            "layout" : {
                            "height": 195,
                            }
                        }, 
                        config={'displayModeBar': False},
                ),
                ], style={"margin-top": -20, "padding-bottom": 0, "padding-left": 0, "margin-left": 0},)
            ], id="card-"+str(n), style={"height": 350, "width": 250, "margin-right": "5px", "margin-bottom": "5px"},
            ),)
        return card

    # Dropdown #1 
    @app.callback(
        Output("pandas-dropdown-2", "options"),
        Output("pandas-dropdown-2", "value"),
        Input("pandas-dropdown-2", "n_clicks"),
    )
    def update_options_first(n):
        return [{"label": i, "value": i} for i in brands], "All"

    # Dropdown #2
    @app.callback(
        [Output("pandas-dropdown-3", "options"),
        Output("pandas-dropdown-3", "value")],
        [Input("pandas-dropdown-2", "value")],
    )
    def update_options_second(value):
        if value == "All" or value == None:
            return [{"label": i, "value": i} for i in s_names], "All"
        else:
            sneakers = option[option['Brand'] == value]
            sneakers.sort_values(by="Brand")
            return [{"label": i, "value": i} for i in sneakers["Sneaker Name"].unique()], "All"

    # Dropdown #3
    @app.callback(
        [Output("pandas-dropdown-4", "options"),
        Output("pandas-dropdown-4", "value")],
        [Input("pandas-dropdown-2", "value"),
        Input("pandas-dropdown-3", "value")],
    )
    def update_options_third(valueB, valueM):
        if valueB == "All" and valueM == "All":
            return [{"label": i, "value": i} for i in sizes], "All"
        elif valueB == "All" and valueM != "All": 
            sneakers2 = option[option['Sneaker Name'] == valueM]
            sneakers2 = sneakers2.sort_values(by="Sneaker Name")
            return [{"label": i, "value": i} for i in sneakers2["Shoe Size"].unique()], "All" 
        else:
            sneakers3 = option[option['Sneaker Name'] == valueM]
            sneakers3 = sneakers3.sort_values(by="Shoe Size")
            return [{"label": i, "value": i} for i in sneakers3["Shoe Size"].unique()], "All"
    
    #Create multiple cards
    @app.callback(
        Output("output", "children"),
        Output("total-count", 'children'),
        Output("part-count", 'children'),
        Output("price-retail", 'children'),
        Output("mean-vola", 'children'),
        Output("total-inc", 'children'),
        [Input("pandas-dropdown-2", "value"),
        Input("pandas-dropdown-3", "value"),
        Input("pandas-dropdown-4", "value")],
        State("output", "children")
    )

    def create_cards(valueB, valueM, valueS, children):
        
        dff1 = df1.copy()
        dff2 = df2.copy()

        sneakers = dff1.groupby(['Sneaker Name', 'Shoe Size']).size().reset_index()
        total_count = "/" + str(len(sneakers))
        
        if (valueB == "All" and valueM == "All" and valueS == "All"):
            
            # Little cards       
            #children = (make_card(len(sneakers), sneakers["Sneaker Name"], sneakers["Shoe Size"]) )            
            children = (make_card(25))

            # statistics boxes 
            part_count = str(len(sneakers))
            price_retail = round(dff1['Retail Price'].mean(), 2)
            
            mean_vol = dff2['volatility'].mean()
            mean_vol = round(mean_vol * 100, 2)
            mean_vol = str(mean_vol) + '%'
            
            total_inc = round((df1['Sale Price'].mean() - df1['Retail Price'].mean()),2)
            total_inc = '$' + str(total_inc)
           
        if valueB != "All" and valueM == "All" and valueS == "All":
            # Little cards
            sneakersB = dff1[dff1["Brand"].str.contains(valueB)]
            sneakersBU = sneakersB.groupby(['Sneaker Name', 'Shoe Size']).size().reset_index()
            #children = (make_card(len(sneakersBU)+1, sneakersBU["Sneaker Name"], sneakersBU["Shoe Size"])) 
            children = (make_card(20)) 

            # statistics boxes 
            part_count = str(len(sneakersBU))
            price_retail = sneakersB['Retail Price'].mean().round(2)
            price_retail = '$' + str(price_retail)

            dff2['brand'] = dff2['brand'].astype(pd.StringDtype())
            sneakersBV = dff2[dff2["brand"].str.contains(valueB)]
            
            mean_vol = sneakersBV['volatility'].mean()
            mean_vol = round((mean_vol * 100), 2)
            mean_vol = str(mean_vol) + '%'

            total_inc = round((sneakersB['Sale Price'].mean() - sneakersB['Retail Price'].mean()),2)
            total_inc = '$' + str(total_inc)

        # brand and model have changed or only brand has changed 
        if (
            valueB != "All" and valueM != "All" and valueS == "All") or (
            valueB == "All" and valueM != "All" and valueS == "All"):
           
            sneakersM = dff1[dff1["Sneaker Name"].str.contains(valueM)]
            sneakersMU = sneakersM.groupby(['Sneaker Name', 'Shoe Size']).size().reset_index()
            children = (make_card(len(sneakersMU)+1))
            #children = (make_card(20, sneakersMU["Sneaker Name"], sneakersMU["Shoe Size"])) 

            # statistics boxes 
            part_count = str(len(sneakersMU))
            price_retail = round((sneakersM['Retail Price'].mean()), 2)
            price_retail = '$' + str(price_retail)

            sneakersMV = dff2[dff2["item"].str.upper().str.contains(valueM.upper())]

            if (sneakersMV.empty):
                mean_vol = 'Not Available'
            else:
                mean_vol = sneakersMV['volatility'].mean()
                mean_vol = round((mean_vol * 100), 2)
                mean_vol = str(mean_vol) + '%'

            total_inc = round((sneakersM['Sale Price'].mean() - sneakersM['Retail Price'].mean()),2)
            total_inc = '$' + str(total_inc)
        
        # All dropdown changed or model and size are changed 
        if  (
            valueB != "All" and valueM != "All" and valueS != "All") or (
            valueB == "All" and valueM != "All" and valueS != "All"):

            sneakersS = dff1[dff1["Shoe Size"] == valueS]
            sneakersS = sneakersS[sneakersS["Sneaker Name"] == valueM]
            sneakersSU = sneakersS.groupby(['Sneaker Name', 'Shoe Size']).size().reset_index()
            
            children = (make_card(len(sneakersSU)+1)) 

            # statistics boxes 
            part_count = str(len(sneakersSU))
            price_retail = round((sneakersS['Retail Price'].mean()), 2)
            price_retail = '$' + str(price_retail)

            sneakersSV = dff2[dff2["item"].str.upper().str.contains(valueM.upper())]

            if (sneakersSV.empty):
                mean_vol = 'Not Available'
            else:
                mean_vol = sneakersSV['volatility'].mean()
                mean_vol = round((mean_vol * 100), 2)
                mean_vol = str(mean_vol) + '%'

            total_inc = round((sneakersS['Sale Price'].mean() - sneakersS['Retail Price'].mean()),2)
            total_inc = '$' + str(total_inc)

        # Only Size dropdown was changed 
        if valueB == "All" and valueM == "All" and valueS != "All":
            
            sneakersS = dff1[dff1["Shoe Size"] == valueS]
            sneakersSU = sneakersS.groupby(['Sneaker Name', 'Shoe Size']).size().reset_index()
            
            #children = (make_card(len(sneakersSU)+1, sneakersSU["Sneaker Name"], sneakersSU["Shoe Size"])) 
            children = (make_card(25)) 

            # statistics boxes 
            part_count = str(len(sneakersSU))
            price_retail = round((sneakersS['Retail Price'].mean()), 2)
            price_retail = '$' + str(price_retail)

            mean_vol = 'Not Available'

            total_inc = round((sneakersS['Sale Price'].mean() - sneakersS['Retail Price'].mean()),2)
            total_inc = '$' + str(total_inc)
        
        # sliders 
        # if sliderP[0] !=0 and sliderP[1] != 4100:
        #     n = 25
        #     sliderF = dff1[dff1["Sale Price"] < sliderP[1]]
        #     sliderF = dff1[dff1["Sale Price"] > sliderP[0]]

        #     sliderG = sliderF.groupby(['Sneaker Name']).size().reset_index()
        #     if n < len(sliderG):
        #         n = len(sliderG)
        #     children = (make_card(n))

        #     part_count = str(len(sliderG))
        #     price_retail = round(sliderF['Retail Price'].mean(), 2)
            
        #     sliderV = dff2[dff2["lastSale"] < sliderP[1]]
        #     sliderV = dff2[dff2["lastSale"] > sliderP[0]]
        #     if (sliderV.empty):
        #         mean_vol = 'Not Available'
        #     else: 
        #         mean_vol = sliderV['volatility'].mean()
        #         mean_vol = round(mean_vol * 100, 2)
        #         mean_vol = str(mean_vol) + '%'
            
        #     total_inc = round((sliderF['Sale Price'].mean() - sliderF['Retail Price'].mean()),2)
        #     total_inc = '$' + str(total_inc)

        # if sliderI[0] !=-50 and sliderI[1] != 4000:
        #     n = 25
        #     inc = 
        #     sliderF = dff1[dff1["Sale Price"] < sliderP[1]]
        #     sliderF = dff1[dff1["Sale Price"] > sliderP[0]]

        #     sliderG = sliderF.groupby(['Sneaker Name']).size().reset_index()
        #     if n < len(sliderG):
        #         n = len(sliderG)
        #     children = (make_card(n))

        #     part_count = str(len(sliderG))
        #     price_retail = round(sliderF['Retail Price'].mean(), 2)
            
        #     sliderV = dff2[dff2["lastSale"] < sliderP[1]]
        #     sliderV = dff2[dff2["lastSale"] > sliderP[0]]
        #     if (sliderV.empty):
        #         mean_vol = 'Not Available'
        #     else: 
        #         mean_vol = sliderV['volatility'].mean()
        #         mean_vol = round(mean_vol * 100, 2)
        #         mean_vol = str(mean_vol) + '%'
            
        #     total_inc = round((sliderF['Sale Price'].mean() - sliderF['Retail Price'].mean()),2)
        #     total_inc = '$' + str(total_inc)

        return children, total_count, part_count, price_retail, mean_vol, total_inc
    
    
 
    @app.callback(
        Output({'type': 'line-chart', 'index': MATCH}, "figure"), 
        Output({'type': 'image', 'index': MATCH}, "src"), 
        Input({'type': 'line-chart', 'index': MATCH}, "id"),
        [Input("pandas-dropdown-2", "value"),
        Input("pandas-dropdown-3", "value"),
        Input("pandas-dropdown-4", "value")],  
    )
    def update_line(id, valueB, valueM, valueS):
        dff1 = df1.copy()
        dff2 = df2.copy()

        index = (id.get('index'))
        if valueB == "All" and valueM == "All" and valueS == "All":
        
            chart = dff1[dff1["Sneaker Name"]== s_names[index+1]]

            fig_line = px.line(chart,
                        x="Order Date",
                        y="Sale Price",
                        title=s_names[index+1],                        
            )
            #os.path.exists('/assets/'+s_names[index+1].lower()+'.jpg'):
            if os.path.exists('assets/'+s_names[index+1].lower()+'.jpg'):
                imgs = '/assets/'+s_names[index+1].lower()+'.jpg'
            else: 
                imgs = '/assets/X_Gray_Digital_RGB.png'
            
           
        if valueB != "All" and valueM == "All" and valueS =="All": 
            sneakersB = dff1[dff1["Brand"].str.contains(valueB)]
            sneakersBU = sneakersB.groupby(['Sneaker Name']).size().reset_index()
            # sneakersB = option[option['Brand'] == valueB]
            #sneakersBU = sneakersB.groupby(['Sneaker Name', 'Shoe Size']).size().reset_index()
            # sneakers = sneakers.drop_duplicates(subset=['Sneaker Name'])
            chart = sneakersB[sneakersB["Sneaker Name"]== sneakersBU["Sneaker Name"][index+1]]
            title_text = (sneakersBU["Sneaker Name"][index+1])

            fig_line = px.line(chart,
                        x="Order Date",
                        y="Sale Price",
                        title=title_text
            )
            if os.path.exists('assets/'+sneakersBU["Sneaker Name"][index+1].lower()+'.jpg'):
                imgs = '/assets/'+sneakersBU["Sneaker Name"][index+1].lower()+'.jpg'
            else: 
                imgs = '/assets/X_Gray_Digital_RGB.png'

        if (
            valueB != "All" and valueM != "All" and valueS == "All") or (
            valueB == "All" and valueM != "All" and valueS == "All"):

            sneakersM = dff1[dff1["Sneaker Name"].str.contains(valueM)]
            #sneakersM = dff1[dff1["Sneaker Name"]==(valueM)]
            sneakersMU = sneakersM.groupby(['Sneaker Name', 'Shoe Size']).size().reset_index()
            chart = dff1[dff1["Sneaker Name"] == sneakersMU["Sneaker Name"][index]]
            chart = chart[chart["Shoe Size"] == sneakersMU["Shoe Size"][index]]
            
            title_text = (sneakersMU["Sneaker Name"][index]+'<br>'+(" Size-"+str(sneakersMU["Shoe Size"][index])))
            fig_line = px.line(chart,
                    x="Order Date",
                    y="Sale Price",
                    title= title_text       
            )
            if os.path.exists('assets/'+sneakersMU["Sneaker Name"][index].lower()+'.jpg'):
                imgs = '/assets/'+sneakersMU["Sneaker Name"][index].lower()+'.jpg'
            else: 
                imgs = '/assets/X_Gray_Digital_RGB.png'

        if(
            valueB != "All" and valueM != "All" and valueS != "All") or (
            valueB == "All" and valueM != "All" and valueS != "All"):

            sneakersS = dff1[dff1["Shoe Size"] == valueS]
            sneakersS = sneakersS[sneakersS["Sneaker Name"] == valueM]
            sneakersSU = sneakersS.groupby(['Sneaker Name', 'Shoe Size']).size().reset_index() 
            chart = sneakersS[sneakersS["Sneaker Name"] == sneakersSU["Sneaker Name"][index]]
            chart = chart[chart["Shoe Size"] == sneakersSU["Shoe Size"][index]]
            print(chart)
            
            title_text = (sneakersSU["Sneaker Name"][index]+'<br>'+(" Size-"+str(sneakersSU["Shoe Size"][index])))
            fig_line = px.line(chart,
                    x="Order Date",
                    y="Sale Price",
                    title= title_text
            )  
            if os.path.exists('assets/'+sneakersSU["Sneaker Name"][index].lower()+'.jpg'):
                imgs = '/assets/'+sneakersSU["Sneaker Name"][index].lower()+'.jpg'
            else: 
                imgs = '/assets/X_Gray_Digital_RGB.png'

        if valueB == "All" and valueM == "All" and valueS != "All":
            
            sneakersS = dff1[dff1["Shoe Size"] == valueS]
            sneakersSU = sneakersS.groupby(['Sneaker Name', 'Shoe Size']).size().reset_index() 
            chart = sneakersS[sneakersS["Sneaker Name"] == sneakersSU["Sneaker Name"][index]]
            chart = chart[chart["Shoe Size"] == sneakersSU["Shoe Size"][index]]
            title_text = (sneakersSU["Sneaker Name"][index]+'<br>'+(" Size-"+str(sneakersSU["Shoe Size"][index])))
            fig_line = px.line(chart,
                    x="Order Date",
                    y="Sale Price",
                    title= title_text
            ) 
            if os.path.exists('assets/'+sneakersSU["Sneaker Name"][index].lower()+'.jpg'):
                imgs = '/assets/'+sneakersSU["Sneaker Name"][index].lower()+'.jpg'
            else: 
                imgs = '/assets/X_Gray_Digital_RGB.png'
            
        fig_line.update_traces(line_color='#006340')
        fig_line.update_layout(
            autosize=False, 
            width=220, 
            height=200, 
            margin=dict(l=0, r=0, t=30, b=0),
            title_x=0.5,
            font=dict(size=6.5),
            plot_bgcolor="white")
        fig_line.update_yaxes(
            title='',
            showgrid=True,
            gridcolor='#e2ede9')
        fig_line.update_xaxes(
            title='',
            showgrid=True,
            gridcolor='#e2ede9') 
        
    
        return fig_line, imgs
    
