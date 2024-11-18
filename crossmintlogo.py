import requests
import time

# Base URL
URL = "https://challenge.crossmint.io/api"
Candidate_ID = "9016cf69-f933-4bb8-b4b1-213e87d0066e" 

# Fetch the goal map
def fetch_goal_map():
    response = requests.get(f"{URL}/map/{Candidate_ID}/goal")
    response.raise_for_status()
    return response.json()

# Create Polyanet
def create_polyanet(row, column):
    response = requests.post(f"{URL}/polyanets", json={
        "candidateId": Candidate_ID,
        "row": row,
        "column": column
    })
    response.raise_for_status()

# Create Soloon
def create_soloon(row, column, color):
    response = requests.post(f"{URL}/soloons", json={
        "candidateId": Candidate_ID,
        "row": row,
        "column": column,
        "color": color
    })
    response.raise_for_status()

# Create Cometh
def create_cometh(row, column, direction):
    response = requests.post(f"{URL}/comeths", json={
        "candidateId": Candidate_ID,
        "row": row,
        "column": column,
        "direction": direction
    })
    response.raise_for_status()

# Parse the goal map and create entities
def final_goal_map(goal_map):
    for row_idx, row in enumerate(goal_map):
        for col_idx, cell in enumerate(row):
            if cell == "POLYANET":
                create_polyanet(row_idx, col_idx)
            elif "SOLOON" in cell:
                color = cell.split("_")[0].lower()  
                create_soloon(row_idx, col_idx, color)
            elif "COMETH" in cell:
                direction = cell.split("_")[0].lower()  
                create_cometh(row_idx, col_idx, direction)

             # Avoid rate limiting
            time.sleep(0.2) 

# Main
if __name__ == "__main__":
    try:
        goal_map_data = fetch_goal_map()
        goal_map = goal_map_data["goal"] 
        final_goal_map(goal_map)
    except Exception as e:
        print(f"Exception: {e}")
