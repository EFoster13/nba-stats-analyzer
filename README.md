# NBA Player Statistics Analyzer

A web-based application for analyzing and visualizing NBA player statistics. Built with Python, Streamlit, and Pandas, this tool enables sports analysts, fans, and researchers to explore player performance data through interactive filtering, sorting, and comparison features.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.49.1-red.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.1.4-green.svg)

## Features

### Data Processing
- **CSV Upload**: Import NBA player statistics from CSV files
- **Automatic Data Cleaning**: Removes duplicates, handles missing values, and normalizes column names
- **Dynamic Column Detection**: Automatically identifies and processes numeric statistics

### Analysis & Filtering
- **Multi-Parameter Filtering**: Filter players by team, position, and minimum games played
- **Dynamic Metric Selection**: Analyze players across any statistical category (PTS, AST, REB, etc.)
- **Top-N Rankings**: Display top performers with customizable result limits (5-50 players)
- **Custom Column Display**: Select which statistics to include in results tables

### Visualizations
- **Bar Charts**: Visual comparison of top players for selected metrics
- **Distribution Histograms**: View statistical distributions across all qualified players
- **Summary Statistics**: Real-time calculation of averages and maximums

### Player Comparison
- **Side-by-Side Analysis**: Compare two players across all statistical categories
- **Comprehensive Metrics**: View all available stats in an organized comparison view

### Export & Download
- **CSV Export**: Download filtered and sorted results for further analysis
- **Dynamic File Naming**: Automatically generated filenames based on selected parameters

## Requirements

- Python 3.7+
- Streamlit 1.49.1
- Pandas 2.1.4
- Matplotlib 3.9.0
- openpyxl

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/EFoster13/nba-stats-analyzer.git
cd nba-stats-analyzer
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

The app will automatically open in your default web browser at `http://localhost:8501`

## Usage

### Basic Workflow

1. **Upload Data**
   - Click "Browse files" and select your NBA statistics CSV file
   - The app will automatically clean and process the data

2. **Configure Filters** (Sidebar)
   - Select the statistical metric to analyze (e.g., PTS, AST, REB)
   - Set the number of top players to display
   - Set minimum games played threshold
   - Choose additional columns to display
   - Filter by team (optional)
   - Filter by position (optional)

3. **View Results**
   - Review summary statistics at the top
   - Explore the bar chart visualization
   - Examine the distribution histogram
   - Analyze the ranked table of top players

4. **Compare Players**
   - Scroll to the comparison section
   - Select two players from the dropdown menus
   - Click "Compare Players" to see side-by-side statistics

5. **Export Data**
   - Click the "Download Results as CSV" button to save filtered data

### Expected CSV Format

Your CSV file should include these standard NBA statistics columns:
- `Player`: Player name
- `Pos`: Position (PG, SG, SF, PF, C)
- `Age`: Player age
- `Tm`: Team abbreviation
- `G`: Games played
- `MP`: Minutes played
- Statistical columns: `FG%`, `3P%`, `FT%`, `ORB`, `DRB`, `AST`, `STL`, `BLK`, `TOV`, `PTS`, etc.

## Sample Data

You can find NBA player statistics from sources like:
- [Basketball Reference](https://www.basketball-reference.com/)
- [NBA Stats](https://www.nba.com/stats/)
- [Kaggle NBA Datasets](https://www.kaggle.com/datasets)

## Technical Implementation

### Architecture
- **Frontend**: Streamlit for interactive web interface
- **Data Processing**: Pandas for data manipulation and analysis
- **Visualization**: Matplotlib for statistical charts
- **Version Control**: Git/GitHub for source code management

### Key Functions
- `clean_data()`: Preprocesses uploaded CSV data
- Dynamic filtering with Pandas query operations
- Sorting algorithms for player rankings
- Statistical calculations for summary metrics

## Future Enhancements

Potential features for future versions:
- [ ] Advanced statistics (PER, TS%, Win Shares)
- [ ] Multi-season comparison
- [ ] Team-level analytics
- [ ] Machine learning predictions
- [ ] Export to PDF reports
- [ ] Database integration for larger datasets


## Author

**Ethan Foster**
- GitHub: [@EFoster13](https://github.com/EFoster13)

- NBA for providing comprehensive player statistics
- Streamlit team for the excellent web framework
- Python data science community



