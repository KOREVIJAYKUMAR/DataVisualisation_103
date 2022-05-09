import pandas as pd
import plotly.express as px

df=pd.read_csv('D:/MRUDULA KORE/MRUDULA/Python/Projects/DataVisualisation_103/data (1).csv')



fig=px.scatter(df,x='country',y='cases',color='country',size_max=80)
fig.show()

