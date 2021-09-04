import pandas as pd
import plotly_express as px

df = pd.read_csv("final.csv")
df = df.sort_values("total_actions",axis=0,ascending=False)
print(df)
fig = px.bar(df.head(10),x="total_actions",y="title")

fig.show()