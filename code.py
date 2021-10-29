import csv
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("data.csv")
data = df["date","cases","country"].tolist()

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)

print("mean is: ",mean)
print("median is: ",median)
print("mode is: ",mode)