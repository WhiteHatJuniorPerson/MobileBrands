import pandas as pd 
import plotly.figure_factory as pf 
df = pd.read_csv("project 108.csv")
rating = df["Avg Rating"].tolist()
graph = pf.create_distplot([rating],["Rating"],show_hist=False)
graph.show()
