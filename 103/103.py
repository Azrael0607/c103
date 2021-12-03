import pandas as pd
import plotly.express as px

df = pd.read_csv('data.csv')
fig = px.scatter(df,x = 'Population', y = 'internetusers', color = 'Country',title = 'Internet')
fig.show()
