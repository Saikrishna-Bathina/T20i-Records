import csv
import json

def create_js_data():
    data = []
    try:
        with open("global_team_milestones.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert numbers
                row['milestone'] = int(row['milestone'])
                row['legal_balls_faced'] = int(row['legal_balls_faced'])
                data.append(row)
    except FileNotFoundError:
        print("CSV file not found, creating empty data")
        
    js_content = f"window.milestoneData = {json.dumps(data, indent=2)};"
    
    with open("dashboard_data.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    print("dashboard_data.js created.")

if __name__ == "__main__":
    create_js_data()
