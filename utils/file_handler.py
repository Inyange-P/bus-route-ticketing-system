# Shared file handling functions for the bus route and ticket management system

from datetime import date
from ticket import Ticket
import json
from passenger import Passenger
from bus_pass import BusPass
from trip import Trip
from route import Route

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


# with .isoformat() before it can go into JSON, and converted back with date.fromisoformat() when loading. JSON itself has no idea what a date object is, so this step can't be skipped or it will crash on save.

def save_tickets(tickets, filename="tickets.json"):
    # convert each Ticket object into a plain dictionary so it can be saved as JSON
    data = []
    for ticket in tickets.values():
        data.append({
            "ticket_id": ticket.ticket_id,
            "passenger_id": ticket.passenger_id,
            "trip_id": ticket.trip_id,
            "seat_number": ticket.seat_number,
            "pass_id": ticket.pass_id,
            "price": ticket.price,
            "purchase_date": ticket.purchase_date.isoformat(),
            "status": ticket.status
        })
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Saved {len(data)} ticket(s) to {filename}.")

def load_tickets(filename="tickets.json"):
    tickets = {}

    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"No saved file found at {filename}. Starting with no tickets.")
        return tickets

    for item in data:
        ticket = Ticket(
            ticket_id=item["ticket_id"],
            passenger_id=item["passenger_id"],
            trip_id=item["trip_id"],
            seat_number=item["seat_number"],
            price=item["price"],
            pass_id=item["pass_id"],
            purchase_date=date.fromisoformat(item["purchase_date"]),
            status=item["status"]
        )
        tickets[ticket.ticket_id] = ticket

    print(f"Loaded {len(tickets)} ticket(s) from {filename}.")
    return tickets



def save_trips(trip_manager, filename="trips.json"):
    # Convert each Trip object into a plain dictionary so it can be saved as JSON
    trips_data = []

    for trip in trip_manager.trips.values():
        trips_data.append({
            "trip_id": trip.trip_id,
            "route_id": trip.route_id,
            # travel_date is a real date object, so it needs .isoformat()
            # before it can go into JSON — JSON has no concept of dates
            "travel_date": trip.travel_date.isoformat(),
            "departure_time": trip.departure_time,
            "arrival_time": trip.arrival_time,
            "total_seats": trip.total_seats
        })

    with open(filename, "w") as file:
        json.dump(trips_data, file, indent=4)

    print(f"Saved {len(trips_data)} trip(s) to {filename}.")


def load_trips(trip_manager, filename="trips.json"):
    # Reads trips from file and adds them directly into trip_manager.trips,
    # matching the same pattern as load_routes (mutates in place, returns nothing)
    try:
        with open(filename, "r") as file:
            trips_data = json.load(file)

        for trip_data in trips_data:
            # Rebuild travel_date from its saved string back into a real
            # date object using date.fromisoformat()
            trip = Trip(
                trip_data["trip_id"],
                trip_data["route_id"],
                date.fromisoformat(trip_data["travel_date"]),
                trip_data["departure_time"],
                trip_data["arrival_time"],
                trip_data["total_seats"]
            )

            trip_manager.trips[trip.trip_id] = trip

        print(f"Loaded {len(trips_data)} trip(s) from {filename}.")

    except FileNotFoundError:
        print(f"{filename} not found. Starting with no saved trips.")

        
def save_routes(route_manager, filename="routes.json"):
    routes_data = []

    for route in route_manager.routes.values():
        routes_data.append({
            "route_id": route.route_id,
            "origin": route.origin,
            "destination": route.destination,
            "distance_km": route.distance_km,
            "base_fare": route.base_fare
        })

    with open(filename, "w") as file:
        json.dump(routes_data, file, indent=4)

    print(f"Saved {len(routes_data)} route(s) to {filename}.")


def load_routes(route_manager, filename="routes.json"):
    try:
        with open(filename, "r") as file:
            routes_data = json.load(file)

        for route_data in routes_data:
            route = Route(
                route_data["route_id"],
                route_data["origin"],
                route_data["destination"],
                route_data["distance_km"],
                route_data["base_fare"]
            )

            route_manager.routes[route.route_id] = route

        print(f"Loaded {len(routes_data)} route(s) from {filename}.")

    except FileNotFoundError:
        print(f"{filename} not found. Starting with no saved routes.")