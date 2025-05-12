import pandas as pd
import numpy as np
import plotly.express as px
import os

# Load the dataset
df = pd.read_csv("Play Store Data.csv")

# Filter only paid apps
df_paid = df[df['Type'] == 'Paid'].copy()

# Clean 'Installs' column (remove commas and '+' symbols, then convert to int)
df_paid['Installs'] = df_paid['Installs'].str.replace('[+,]', '', regex=True).astype(int)

# Clean 'Price' column (remove '$' if present, then convert to float)
df_paid['Price'] = df_paid['Price'].replace('[\$,]', '', regex=True).astype(float)

# Calculate revenue
df_paid['Revenue'] = df_paid['Price'] * df_paid['Installs']

# Remove rows with missing or infinite values
df_paid = df_paid.replace([np.inf, -np.inf], np.nan).dropna(subset=['Revenue', 'Installs', 'Category'])

# Create 'templates' directory if it doesn't exist
output_dir = "templates"
os.makedirs(output_dir, exist_ok=True)

# Create the scatter plot
fig = px.scatter(
    df_paid,
    x="Installs",
    y="Revenue",
    color="Category",
    title="Revenue vs Installs for Paid Apps",
    labels={"Installs": "Number of Installs", "Revenue": "Revenue (USD)"},
    trendline="ols",
    template="plotly_dark",
    hover_name="App"
)

# Save plot as HTML
html_path = os.path.join(output_dir, "revenue_vs_installs.html")
fig.write_html(html_path)

# Show the plot
fig.show()
