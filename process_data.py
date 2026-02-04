import csv
import glob
import os

def process_data():
    data_dir = "data"
    csv_files = glob.glob(os.path.join(data_dir, "*.csv"))
    
    global_milestones = []
    
    print(f"Found {len(csv_files)} files. Processing...")
    
    milestones_to_track = [50, 100, 150, 200, 250]
    
    count = 0
    for file_path in csv_files:
        count += 1
        if count % 100 == 0:
            print(f"Processed {count} files...")
            
        match_id = os.path.basename(file_path).split(".")[0]
        
        info = {}
        innings_data = {}
        
        try:
            with open(file_path, "r") as f:
                reader = csv.reader(f)
                rows = list(reader)
        except Exception:
            continue
            
        current_inning = None
        
        for row in rows:
            if not row:
                continue
                
            if row[0] == 'version':
                continue
                
            if row[0] == 'info':
                if row[1] == 'team':
                    if 'teams' not in info:
                        info['teams'] = []
                    info['teams'].append(row[2])
                elif row[1] == 'gender':
                    info['gender'] = row[2]
                elif row[1] == 'date':
                     # Handle multiple dates, take the first one or just keep overwriting (usually consecutive days)
                     if 'date' not in info:
                        info['date'] = row[2]
                elif row[1] == 'venue':
                    info['venue'] = row[2]
            
            elif row[0] == 'ball':
                inning = row[1]
                if inning not in innings_data:
                    innings_data[inning] = []
                innings_data[inning].append(row)
        
        # Filter for Men's T20Is only
        if info.get('gender') != 'male':
            continue
            
        teams = info.get('teams', [])
        if len(teams) < 2:
            continue
            
        date = info.get('date', 'Unknown')
        venue = info.get('venue', 'Unknown')

        for inn, rows in innings_data.items():
            if not rows:
                 continue
            
            # Determine batting team
            batting_team = rows[0][3]
            
            # Identify opponent
            opponent = "Unknown"
            for t in teams:
                if t != batting_team:
                    opponent = t
                    break
            
            current_inning_runs = 0
            current_inning_legal_balls = 0
            milestones_reached = set()
            
            for row in rows:
                try:
                    runs_bat = int(row[7]) if row[7] else 0
                    extras = int(row[8]) if row[8] else 0
                    total_runs = runs_bat + extras
                    
                    wides = row[9] if len(row) > 9 else ""
                    noballs = row[10] if len(row) > 10 else ""
                    
                    is_legal = (wides == "") and (noballs == "")
                    
                    current_inning_runs += total_runs
                    if is_legal:
                        current_inning_legal_balls += 1
                        
                    # Check milestones
                    for m in milestones_to_track:
                        if current_inning_runs >= m and m not in milestones_reached:
                            global_milestones.append([
                                match_id, date, batting_team, opponent, venue, inn, m, current_inning_legal_balls
                            ])
                            milestones_reached.add(m)
                            
                except IndexError:
                    continue
                        
    # Write aggregated milestones CSV
    print("Writing global milestones CSV...")
    with open("global_team_milestones.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["match_id", "date", "team", "opponent", "venue", "inning", "milestone", "legal_balls_faced"])
        writer.writerows(global_milestones)
        
    print("Processing complete.")

if __name__ == "__main__":
    process_data()
