import pandas as pd
import datetime as dt
import dash
from dash import dcc, html, Input, Output
import tab1
import tab2
import tab3
import os
import plotly.graph_objects as go
class db:
    def __init__(self):
        self.transactions = db.transactions_init()
        self.cc = pd.read_csv(r'db\country_codes.csv',index_col=0)
        self.customers = pd.read_csv(r'db\customers.csv',index_col=0)
        self.prod_info = pd.read_csv(r'db\prod_cat_info.csv')
    @staticmethod
    def transactions_init():
        transactions = pd.DataFrame()
        src = r'D:\Bootcamp\GIT\db\transactions'
        dfs = []
        for filename in os.listdir(src):
            path = os.path.join(src, filename)
            df = pd.read_csv(path, index_col=0)
            print(f"{filename}: {df.columns.tolist()}")
            dfs.append(df)
        transactions = pd.concat(dfs)

        print("Połączono:", transactions.shape)

        if 'tran_date' not in transactions.columns:
            raise ValueError("'tran_date' column is missing!")

        def convert_dates(x):
            try:
                return dt.datetime.strptime(x,'%d-%m-%Y')
            except:
                return dt.datetime.strptime(x,'%d/%m/%Y')
                
        transactions['tran_date'] = transactions['tran_date'].apply(lambda x: convert_dates(x))
        return transactions
    def merge(self):
        df = self.transactions.join(self.prod_info.drop_duplicates(subset=['prod_cat_code']).set_index('prod_cat_code')['prod_cat'],on='prod_cat_code',how='left')
        df = df.join(self.prod_info.drop_duplicates(subset=['prod_sub_cat_code']).set_index('prod_sub_cat_code')['prod_subcat'],on='prod_subcat_code',how='left')
        df = df.join(self.customers.join(self.cc,on='country_code').set_index('customer_Id'),on='cust_id')
        self.merged = df

df = db()
df.merge()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

app.layout = html.Div([html.Div([dcc.Tabs(id='tabs',value='tab-1',children=[
                            dcc.Tab(label='Sprzedaż globalna',value='tab-1'),
                            dcc.Tab(label='Produkty',value='tab-2'),
                            dcc.Tab(label='Kanały sprzedaży', value='tab-3')
                            ]),
                            html.Div(id='tabs-content')
                    ],style={'width':'80%','margin':'auto'})],
                    style={'height':'100%'})

@app.callback(Output('tabs-content','children'),[Input('tabs','value')])
def render_content(tab):

    if tab == 'tab-1':
        return tab1.render_tab(df.merged)
    elif tab == 'tab-2':
        return tab2.render_tab(df.merged)
    elif tab == 'tab-3':
        return tab3.render_tab(df.merged)
    
## tab1 callbacks
@app.callback(Output('bar-sales','figure'),
    [Input('sales-range','start_date'),Input('sales-range','end_date')])

def tab1_bar_sales(start_date,end_date):

    truncated = df.merged[(df.merged['tran_date']>=start_date)&(df.merged['tran_date']<=end_date)]
    grouped = truncated[truncated['total_amt']>0].groupby([pd.Grouper(key='tran_date',freq='M'),'Store_type'])['total_amt'].sum().round(2).unstack()

    traces = []
    for col in grouped.columns:
        traces.append(go.Bar(x=grouped.index,y=grouped[col],name=col,hoverinfo='text',
        hovertext=[f'{y/1e3:.2f}k' for y in grouped[col].values]))

    data = traces
    fig = go.Figure(data=data,layout=go.Layout(title='Przychody',barmode='stack',legend=dict(x=0,y=-0.5)))

    return fig

@app.callback(Output('choropleth-sales','figure'),
            [Input('sales-range','start_date'),Input('sales-range','end_date')])
def tab1_choropleth_sales(start_date,end_date):

    truncated = df.merged[(df.merged['tran_date']>=start_date)&(df.merged['tran_date']<=end_date)]
    grouped = truncated[truncated['total_amt']>0].groupby('country')['total_amt'].sum().round(2)

    trace0 = go.Choropleth(colorscale='Viridis',reversescale=True,
                            locations=grouped.index,locationmode='country names',
                            z = grouped.values, colorbar=dict(title='Sales'))
    data = [trace0]
    fig = go.Figure(data=data,layout=go.Layout(title='Mapa',geo=dict(showframe=False,projection={'type':'natural earth'})))

    return fig

## tab2 callbacks
@app.callback(Output('barh-prod-subcat','figure'),
            [Input('prod_dropdown','value')])
def tab2_barh_prod_subcat(chosen_cat):

    grouped = df.merged[(df.merged['total_amt']>0)&(df.merged['prod_cat']==chosen_cat)].pivot_table(index='prod_subcat',columns='Gender',values='total_amt',aggfunc='sum').assign(_sum=lambda x: x['F']+x['M']).sort_values(by='_sum').round(2)

    traces = []
    for col in ['F','M']:
        traces.append(go.Bar(x=grouped[col],y=grouped.index,orientation='h',name=col))

    data = traces
    fig = go.Figure(data=data,layout=go.Layout(barmode='stack',margin={'t':20,}))
    return fig

## tab3 callbacks
@app.callback(Output('customer_age','figure'),
              [Input('tabs','value')])
def tab3_customer_age(tab_value):
    df.merged['DOB'] = pd.to_datetime(df.merged['DOB'], errors='coerce')
    df.merged = df.merged[df.merged['DOB'].notna()]
    df.merged['age'] = ((pd.to_datetime('today') - df.merged['DOB']).dt.days // 365)

    bins = [0, 29, 44, 59, 120]
    labels = ['18-29', '30-44', '45-59', '60+']
    df.merged['age_group'] = pd.cut(df.merged['age'], bins=bins, labels=labels, right=True)

    grouped = df.merged[df.merged['total_amt'] > 0].groupby(['age_group', 'Store_type'])['total_amt'].sum().unstack().fillna(0).round(2)

    print("Groupby shape:", grouped.shape)  # DEBUG

    traces = []
    for col in grouped.columns:
        traces.append(go.Bar(name=col, x=grouped.index.astype(str), y=grouped[col]))

    fig = go.Figure(data=traces)
    fig.update_layout(
        barmode='group',
        title='Udział grup wiekowych w sprzedaży wg kanału',
        xaxis_title='Grupa wiekowa',
        yaxis_title='Wartość sprzedaży'
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)