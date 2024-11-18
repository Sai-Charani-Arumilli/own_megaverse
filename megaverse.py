import requests
import json

# Base API URL
BASE_URL = "https://challenge.crossmint.io/api/polyanets"

# Function to place a Polyanet
def place_polyanet(candidate_id, row, column):
    url = BASE_URL
    data = {
        "candidateId": candidate_id,
        "row": row,
        "column": column
    }
    
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=data, headers=headers)

# Function to create the X-shape pattern automatically
def create_polyanet_cross(candidate_id):
    # Coordinates for X-shape (main and secondary diagonals)
    coordinates = [
        (2, 2), (2, 8),
        (3, 3), (3, 7),
        (4, 4), (4, 6),
        (5, 5),
        (6, 4), (6, 6),
        (7, 3), (7, 7),
        (8, 2), (8, 8)
    ]
    
    # Loop through the coordinates and place planets
    for coord in coordinates:
        row, column = coord
        place_polyanet(candidate_id, row, column)

# Main
if __name__ == "__main__":
    candidate_id = "9016cf69-f933-4bb8-b4b1-213e87d0066e"
    create_polyanet_cross(candidate_id)