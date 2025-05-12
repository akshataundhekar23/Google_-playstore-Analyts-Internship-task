from flask import Flask, render_template, send_from_directory
import datetime
import pytz
import os

app = Flask(__name__)

# Define the path to your static folder
STATIC_DIR = os.path.join(os.getcwd(), 'static')

# Function to check current time in IST
def is_time_in_range(start_time, end_time):
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.datetime.now(ist)
    return start_time <= now.hour < end_time

@app.route('/')
def index():
    # 'revenue_vs_installs' is always visible
    revenue_graph = 'revenue_vs_installs.html'
    
    installs_graph = None
    violin_graph = None

    # Time constraint for 'installs_vs_revenue_dual_axis' - Visible 1-4 PM IST
    if is_time_in_range(13, 14):
        installs_graph = 'installs_vs_revenue_dual_axis.html'
    
    # Time constraint for 'violin_rating_distribution' - Visible 4-6 PM IST
    if is_time_in_range(16, 18):
        violin_graph = 'violin_rating_distribution.html'

    return render_template('index.html', 
                           revenue_graph=revenue_graph,
                           installs_graph=installs_graph,
                           violin_graph=violin_graph)

# Route to serve the .html files from the 'static' folder
@app.route('/static/<filename>')
def serve_file(filename):
    return send_from_directory(STATIC_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
