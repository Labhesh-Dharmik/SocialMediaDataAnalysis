# Import necessary libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Create Dash app
app = dash.Dash(__name__)

# Assume df_cleaned is your cleaned DataFrame
# Create a basic scatter plot as an example
fig = px.box(df_cleaned, x='Category', y='Likes', title='Boxplot of Likes by Category')

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='Interactive Social Media Dashboard'),

    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': cat, 'value': cat} for cat in df_cleaned['Category'].unique()],
        multi=True,
        placeholder="Select categories",
        value=df_cleaned['Category'].unique()  # default value: all categories
    ),

    dcc.Graph(
        id='boxplot-likes',
        figure=fig  # Initial figure
    )
])

# Define the callback to update the figure based on selected categories
@app.callback(
    Output('boxplot-likes', 'figure'),
    [Input('category-dropdown', 'value')]
)
def update_boxplot(selected_categories):
    # Filter the data based on the selected categories
    filtered_df = df_cleaned[df_cleaned['Category'].isin(selected_categories)]
    # Create updated boxplot
    updated_fig = px.box(filtered_df, x='Category', y='Likes', title='Boxplot of Likes by Category')
    return updated_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
