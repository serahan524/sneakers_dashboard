import plotly.express as px
import pandas as pd  

from dash import Output, Input

#define the us abbrev here:
us_state_to_abbrev = {'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'}
df = pd.read_csv("StockX_2019.csv",parse_dates=['Order Date','Release Date'], date_parser=pd.to_datetime, skipinitialspace = True)

df['Brand'].str.strip()


def get_callbacks(app):
    #app callbacks:
    @app.callback(
    Output(component_id='choropleth', component_property='figure'),
    [Input(component_id='size-choro-input', component_property='value')]
    )
    def update_choropleth(size):
       
        
        df = pd.read_csv("StockX_2019.csv",parse_dates=['Order Date','Release Date'], date_parser=pd.to_datetime, skipinitialspace = True)
        if (size != -1):
            df = df.loc[df["Shoe Size"] == size]

      
        df = df[['Shoe Size', 'Buyer Region']]
        df = df.groupby(['Buyer Region'])['Shoe Size'].count().reset_index(name='Number of Shoes Sold')
        df['Buyer Region'] = df['Buyer Region'].astype('string')
        df['Code'] = df['Buyer Region'].map(us_state_to_abbrev)

        fig = px.choropleth(
            df,
            locations='Code',
            locationmode='USA-states',
            color='Number of Shoes Sold',
            scope="usa",
            color_continuous_scale=px.colors.sequential.Greens,
        )
        if (size == -1):
            size = '(All)'

        fig.update_layout(
            title={'text': 'Number of Shoes sold on Size ' + str(size) + ' By State in United States',
                   'xanchor':'center',
                   'yanchor':'top',
                   'x':0.5
            
            }, height=500,width=500
        )


        return fig

   
    
    @app.callback(
        Output(component_id='heatmap', component_property='figure'),
        [Input(component_id='brand-input', component_property='value'),
        Input(component_id='size-input', component_property='value')]

    )
    def update_heatmap(brand,size):
        #1. query through brands first
        
        new_keys = []
        days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
        df1 = df[['Order Date','Brand','Sneaker Name','Shoe Size']]
        if (brand == 'All'):
            query_brand = df1
            

        else:
            #query both brand and size from initial dataframe query
            query_brand = df1[df1['Brand'] == brand]

        query_size = query_brand[query_brand['Shoe Size'].isin(size)]
        query_size['Day of Week'] = query_size['Order Date'].dt.dayofweek
        
        query_data = query_size[['Shoe Size','Day of Week']]
        #print(query_data)
        # print('data: ', query_data)
        query_data = query_data.groupby(['Shoe Size','Day of Week']).agg({'Day of Week': ['count']})


        #begin organizing datasets:
        data = list(query_data.to_dict().values())
        actual_data = data[0]
        
        keys = list(data[0].keys())
        vals = list(data[0].values())

        new_keys = [k[0] for k in keys]
        day_of_week = [k[1] for k in keys]

        new_keys = list(set(new_keys))
        day_of_week = list(set(day_of_week))

        new_keys.sort()

        multi_dim = []
        for n in new_keys:
            temp_list = []
            for d in day_of_week:
                tup = (n,d)

                if tup not in actual_data:
                    temp_list.append(0)
                else:
                    temp_list.append(actual_data[tup])
            multi_dim.append(temp_list)

  
        
        labels = dict(x='Day of Week', y='Shoe Size', color="Number of Shoes Sold")

        fig = px.imshow(multi_dim,
                        title='',
                        labels = labels,
                        x = days,
                        y = new_keys,
                        color_continuous_scale=px.colors.sequential.Greens,
                       )

     
        fig.update_xaxes(side='top')
        fig.update_layout(title_text=brand + " Shoe Brands Bought in 2017-2019 by Day Of Week", title_y=0.01)
        



            
       
     

        return fig






