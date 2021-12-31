import plotly.express as px
import csv
import numpy as np


df = csv.DictReader("Student Marks vs Days Present.csv")
fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
fig.show()

