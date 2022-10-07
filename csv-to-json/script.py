import pandas as pd

# Reading the csv file and converting it to a json file.
df = pd.read_csv('sample.csv')
df.to_json('sample.json')