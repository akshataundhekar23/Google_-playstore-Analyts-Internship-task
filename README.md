📊 Google Play Store Analytics Dashboard

An interactive web dashboard built using Flask and Plotly to analyze and visualize Google Play Store data. This dashboard provides insights into installs, ratings, and revenue distribution across categories and time frames.

🚀 Features
💸 Scatter Plot – Visualize the relationship between installs and revenue for paid apps.

📊 Dual Axis Chart – Compare average installs and revenue by app category (1–4 PM IST).

🎻 Violin Plot – Understand the distribution of app ratings by category (4–6 PM IST).

🧾 Data Table – Displays raw data like app name, category, installs, price, revenue, and ratings.

🛠️ Technologies Used
Python 3

Flask – Lightweight web framework

Pandas – Data analysis and manipulation

Plotly – For interactive charts

HTML/CSS – For frontend styling and layout

📁 Project Structure

Google_-playstore-Analyts-Internship-task/

├── internship task/

│   ├── dashboard.py   # Flask backend with data processing and visualization

│   ├── googleplaystore_merged.csv  # Cleaned Google Play Store dataset

│   ├── templates/

│   │   └── dashboard.html        # HTML template to render the plots

├── README.md                     # Project documentation

├── requirements.txt


📸 Screenshots

Scatter Plot
![image](https://github.com/user-attachments/assets/567f535c-db9d-422c-a27c-292d7f6537f1)

✅ Steps to Run the Project Locally
1. Clone the Repository
Open your terminal (or Git Bash/Command Prompt on Windows) and run:

bash
git clone https://github.com/akshataundhekar23/Google_-playstore-Analyts-Internship-task.git

2. Navigate to the Project Folder
   
Move into the internship task directory where your Flask app and dataset exist:
bash
cd Google_-playstore-Analyts-Internship-task/internship\ task

3. Install the Required Packages
If you already have a requirements.txt file:
bash
pip install -r requirements.txt

4. Run the Flask Application
Make sure you're inside the same folder as dashboard.py, then run:

bash
python dashboard.py

You will see output like:
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

6.View the Dashboard in Your Browser
Open a web browser and go to:

http://127.0.0.1:5000/

You will see:

📊 Scatter plot of Revenue vs Installs

📈 Dual axis chart of Avg Installs and Revenue

🎻 Violin plot of Ratings by Category

🧾 Data table of apps and metrics

📊 Dataset Information
The dataset googleplaystore_merged.csv contains information such as:

App name
Category
Rating
Installs
Type (Free/Paid)
Price
Last Updated

❓ Example Use Cases
📱 Market analysts can evaluate category-wise performance of apps.

💼 Developers can explore the relationship between pricing and installs.

🎯 Business analysts can derive insights on timing and app ratings.

👩‍💻 Author
Developed by 
Akshat Aundhekar as part of an internship analytics task.

