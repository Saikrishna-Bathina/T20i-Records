# Global Men's T20I Milestones Analysis

This project analyzes **Men's T20 International** cricket data to identify the fastest team milestones (50, 100, 150, 200, 250 runs) for **every team in history**.

## 🏏 Dashboard Features
Open `index.html` to view the interactive dashboard:
- **Global Records**: View the fastest milestones achieved by ANY team against ANY opponent.
- **Team Filter**: Drill down to see specific stats for India, Australia, England, Nepal, etc.
- **Opponent Filter**: See how teams perform against specific rivals.
- **Search & Sort**: Instantly find matches by venue, date, or sort records by balls faced.

## 📂 Files
- **index.html**: The main dashboard file.
- **dashboard_data.js**: Contains the processed milestone data used by the dashboard.
- **global_team_milestones.csv**: The raw CSV dataset generated from ball-by-ball analysis.
- **process_data.py**: Python script that processes ~2500+ Cricsheet CSV files to extract milestones.
- **download_data.py**: Script to acquire the latest T20I data.

## 🛠️ How it Works
1.  We process ball-by-ball data from [Cricsheet](https://cricsheet.org/).
2.  `process_data.py` calculates how many legal balls it took for a team to reach 50, 100, 150, etc. runs in every inning.
3.  The data is exported to CSV and JSON formats.
4.  `index.html` uses Chart.js to visualize this data without needing a backend server.

## 🚀 Live Demo
[Link to your Netlify/GitHub Pages site here]
