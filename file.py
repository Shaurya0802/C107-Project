import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
print(df)
fig = px.scatter(df.groupby("level")["attempt"].mean(), x="student_id", y=["Level 1", "Level 2", "Level 3", "Level 4"], color="attempt", size="attempt")
fig.show()