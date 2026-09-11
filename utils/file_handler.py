# Shared file handling functions for the bus route and ticket management system
# Chinelo's section: Passenger and BusPass saving/loding

import json
from passenger import Passenger
from bus_pass import BusPass

def save_passengers(passengers, filename="passengers.json"):
    # convert each Passenger object into a plain dictionary so it can be saved as JSON
    data = []
    for passenger in passengers.values():
        data.append({
            "passenger_id": passenger.passenger_id,
            "name": passenger.name,
            "phone": passenger.phone
        })
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Saved {len(data)} passenger(s) to {filename}.")

def load_passengers(filename="passengers.json"):
    passengers = {}

    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"No saved file found at{filename}. Starting with no passengers.")
        return passengers

    for item in data:
        passenger = Passenger(item["passenger_id"], item["name"], item["phone"])
        passengers[passenger.passenger_id] = passenger

    print(f"Loaded {len(passengers)} passenger(s) from {filename}.")
    return passengers

def save_bus_passes(bus_passes, filename="bus_passes.json"):
    # convert each BusPass object into a plain dictionary so it can be saved as JSON
    data = []
    for bus_pass in bus_passes.values():
        data.append({
            "pass_id": bus_pass.pass_id,
            "passenger_id": bus_pass.passenger_id,
            "pass_type": bus_pass.pass_type,
            "issue_date": bus_pass.issue_date,
            "expiry_date": bus_pass.expiry_date,
            "status": bus_pass.status
        })
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Saved {len(data)} bus pass(es) to {filename}.")

def load_bus_passes(filename="bus_passes.json"):
    bus_passes = {}

    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"No saved file found at {filename}. Starting with no bus passes.")
        return bus_passes

    for item in data:
        bus_pass = BusPass(
            item["pass_id"], 
            item["passenger_id"], 
            item["pass_type"],
            item["issue_date"], 
            item["expiry_date"], 
            item["status"])
        bus_passes[bus_pass.pass_id] = bus_pass

    print(f"Loaded {len(bus_passes)} bus pass(es) from {filename}.")
    return bus_passes

