# NBA Player Statistics Analyzer

A web application built with Python and Streamlit for analyzing NBA player statistics.

## Features
- Upload CSV files with NBA player data
- Filter by team, position, and minimum games played
- Sort and rank players by any statistical metric
- Visualize top players with bar charts and distribution histograms
- Compare two players side-by-side
- Download filtered results as CSV

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

## Usage
1. Upload an NBA statistics CSV file
2. Select filters and metrics from the sidebar
3. View rankings, charts, and comparisons
4. Download results as needed
```

### Action 3: Create .gitignore

Create a file called `.gitignore` and add:
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Virtual environments
venv/
env/
ENV/

# Streamlit
.streamlit/

# Data files (optional - remove if you want to include sample data)
*.csv
data/

# IDE
.vscode/
.idea/
*.swp
*.swo

