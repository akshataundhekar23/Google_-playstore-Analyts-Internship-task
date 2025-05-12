import pandas as pd
import numpy as np
import plotly.express as px
import os

# Load dataset
df = pd.read_csv("Play Store Data.csv")

# Clean & filter
df = df.dropna(subset=['App', 'Category', 'Rating', 'Reviews'])

# Ensure correct data types
df['Reviews'] = df['Reviews'].replace('3.0M', 3_000_000, regex=False)
df['Reviews'] = df['Reviews'].astype(str).str.replace('[^0-9]', '', regex=True).astype(int)
df['Rating'] = df['Rating'].astype(float)

# Filter based on task criteria
filtered_df = df[
    (df['App'].str.contains('C', case=False)) &
    (df['Reviews'] > 10) &
    (df['Rating'] < 4.0)
]

# Keep only categories with more than 50 apps
valid_categories = filtered_df['Category'].value_counts()
valid_categories = valid_categories[valid_categories > 50].index.tolist()
filtered_df = filtered_df[filtered_df['Category'].isin(valid_categories)]

# Create violin plot
fig = px.violin(
    filtered_df,
    x='Category',
    y='Rating',
    box=True,
    points='all',
    color='Category',
    title='Rating Distribution by Category (Filtered)',
    template='plotly_dark'
)

# Save to HTML
output_dir = "templates"
os.makedirs(output_dir, exist_ok=True)
fig.write_html(os.path.join(output_dir, "violin_rating_distribution.html"))

# Show plot
fig.show()
