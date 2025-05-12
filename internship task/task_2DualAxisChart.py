import pandas as pd
import numpy as np
import plotly.graph_objects as go
import os

# Load the dataset
df = pd.read_csv("Play Store Data.csv")

# Clean and preprocess
df = df.dropna(subset=['Installs', 'Price', 'Android Ver', 'Size', 'Content Rating', 'App', 'Type'])

# Convert installs to int
df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True).astype(int)

# Clean and convert price
df['Price'] = df['Price'].replace('[\$,]', '', regex=True).astype(float)

# Clean and convert size
def size_to_mb(size_str):
    if 'M' in size_str:
        return float(size_str.replace('M', ''))
    elif 'k' in size_str:
        return float(size_str.replace('k', '')) / 1024
    else:
        return np.nan

df['Size_MB'] = df['Size'].apply(size_to_mb)

# Parse Android version
def parse_android_version(ver):
    try:
        return float(ver.split()[0])
    except:
        return np.nan

df['Android_Version'] = df['Android Ver'].apply(parse_android_version)

# Calculate revenue
df['Revenue'] = df['Price'] * df['Installs']

# Apply filters
filtered_df = df[
    (df['Installs'] >= 10000) &
    (df['Revenue'] >= 10000) &
    (df['Android_Version'] > 4.0) &
    (df['Size_MB'] > 15) &
    (df['Content Rating'] == 'Everyone') &
    (df['App'].str.len() <= 30)
].copy()

# Get top 3 categories
top3_categories = filtered_df['Category'].value_counts().nlargest(3).index.tolist()

# Filter to top 3 categories
filtered_top3 = filtered_df[filtered_df['Category'].isin(top3_categories)]

# Group by Category and Type
grouped = filtered_top3.groupby(['Category', 'Type']).agg(
    Avg_Installs=('Installs', 'mean'),
    Avg_Revenue=('Revenue', 'mean')
).reset_index()

# Create dual-axis bar chart
fig = go.Figure()

# Bar for average installs
# Bar for average installs
fig.add_trace(go.Bar(
    x=grouped['Category'] + " (" + grouped['Type'] + ")",
    y=grouped['Avg_Installs'],
    name='Average Installs',
    marker_color='lightskyblue',
    yaxis='y1'
))

# Bar for average revenue
fig.add_trace(go.Bar(
    x=grouped['Category'] + " (" + grouped['Type'] + ")",
    y=grouped['Avg_Revenue'],
    name='Average Revenue',
    marker_color='lightgreen',
    yaxis='y2'
))

# Layout config
fig.update_layout(
    title="Avg Installs vs Revenue for Free vs Paid Apps in Top 3 Categories",
    xaxis_title="Category (Type)",
    yaxis=dict(
        title=dict(text="Average Installs", font=dict(color="royalblue")),
        tickfont=dict(color="royalblue")
    ),
    yaxis2=dict(
        title=dict(text="Average Revenue (USD)", font=dict(color="seagreen")),
        tickfont=dict(color="seagreen"),
        overlaying="y",
        side="right"
    ),
    legend=dict(x=0.01, y=0.99),
    barmode='group',
    template="plotly_dark"
)

# Save as HTML
output_dir = "templates"
os.makedirs(output_dir, exist_ok=True)
fig.write_html(os.path.join(output_dir, "installs_vs_revenue_dual_axis.html"))

# Show the chart
fig.show()
