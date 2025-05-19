import pandas as pd
import plotly.express as px

# Step 1: Load the dataset
import preswald
from preswald import connect, get_df

connect()
df = get_df('netflix.csv')  

# Step 2: Query or manipulate the data
from preswald import query

# Filter: Only Movies released after 2010
sql = """
SELECT * FROM df
WHERE type = 'Movie' AND release_year > 2010
"""
filtered_df = query(sql, df)

# Step 3: Build an interactive UI
from preswald import text, table

text("# Welcome to Preswald!")
text("Netflix Data Explorer: Movies Released After 2010")
table(filtered_df, title="Filtered Netflix Movies")

# Step 4: Create a visualization
from preswald import plotly
import plotly.express as px

fig = px.histogram(filtered_df,
                   x="release_year",
                   title="Movies Released by Year (After 2010)",
                   labels={"release_year": "Release Year"})
fig.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))
fig.update_layout(template='plotly_white')
preswald.plotly(fig)
preswald.table(df)
