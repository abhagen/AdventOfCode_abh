from aocd import get_data
from io import StringIO
import pandas as pd

data = get_data(day=1, year=2024)

# Part 1:

# Simulate a file from the data string
data_io = StringIO(data)

# Create a DataFrame
df = pd.read_csv(data_io, sep="\t", header=None, names=["Column1", "Column2"])

df = df["Column1"].str.split(expand=True)
df.columns = ["Column1", "Column2"]  # Renaming columns

df["Column1"] = pd.to_numeric(df["Column1"], errors='coerce')
df["Column2"] = pd.to_numeric(df["Column2"], errors='coerce')

col1 = df["Column1"].sort_values().reset_index(drop=True)
col2 = df["Column2"].sort_values().reset_index(drop=True)

diff = []

for i in range(1000):
    diff.append(abs(col1.iloc[i] - col2.iloc[i])) 

ans1 = sum(diff)
ans1 = str(ans1)

print("The answer to day 1, 2024, Part 1 is:\n"+ans1)

# Part 2:

count_sim = []

for i in range(1000):
    a = (col2 == col1[i]).sum()
    a = a*col1[i]
    count_sim.append(a)

ans2 = sum(count_sim)
ans2 = str(ans2)

print("The answer to day 1, 2024 Part 2 is:\n"+ans2)