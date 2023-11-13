import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="CO2 Emission", page_icon=":bar_chart:", layout="wide")

st.title("IUST Junior Project")
st.markdown("<style>div.block-container{padding-top:1rem;}</style>",unsafe_allow_html=True)















'''
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load the data
url = 'https://raw.githubusercontent.com/moufeedovich/co2_emissions/main/final_data.csv'
df = pd.read_csv(url)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("CO2 Emissions Dashboard"),

    # Dropdown for selecting country names
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['country_name'].unique()],
        value=df['country_name'].unique()[0],
        multi=False,
        style={'width': '50%'}
    ),

    # Scatter plot for CO2 emissions
    dcc.Graph(id='scatter-plot'),

])

# Define callback to update scatter plot based on dropdown selection
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_scatter_plot(selected_country):
    # Filter the data based on the selected country
    filtered_df = df[df['country_name'] == selected_country]

    # Create a scatter plot
    fig = px.scatter(filtered_df, x='year', y='co2', color='count',
                     title=f'CO2 Emissions for {selected_country}',
                     labels={'co2': 'CO2 Emissions', 'year': 'Year'},
                     hover_data=['country_name'])

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
'''
