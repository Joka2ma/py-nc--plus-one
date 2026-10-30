# main.py
from fastapi import FastAPI
import json
from config.connection import get_db_connection
from src.seed import seed,SeedData
from typing import cast



def load_data(filepath:str):
    with open(filepath) as file:
        return json.load(file)
    
    
def main() -> None:
   
    
    data= {
        "users": load_data("db/data/users.json"),
        "venues": load_data("db/data/venues.json"),
        "events":load_data("db/data/events.json"),
        "rsvps":load_data("db/data/rsvps.json")}
        
    conn = get_db_connection()
    try:
        seed(conn,cast(SeedData,data))
        print("Database successfully seeded!")
        
    finally:
        conn.close()

if __name__ == "__main__":
    main()