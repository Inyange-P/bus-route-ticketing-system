from datetime import date
from route_manager import RouteManager
from trip_manager import TripManager
from ticket_manager import TicketManager
from passenger_manager import PassengerManager
from bus_pass_manager import BusPassManager
from utils.file_handler import (load_routes, save_routes, load_trips, save_trips, load_passengers, save_passengers, load_bus_passes, save_bus_passes, load_tickets, save_tickets,)
from utils.validation import( validate_trip_date,validate_departure_and_arrival,validate_total_seats,validate_record_exists)


route_manager = RouteManager()
trip_manager = TripManager()
ticket_manager = TicketManager()
passenger_manager = PassengerManager()
bus_pass_manager = BusPassManager()

def route_menu():
    while True:
        print("\n----- ROUTE MENU -----")
        print("1. Add route")
        print("2. Display routes")
        print("3. Search route")
        print("4. Update route")
        print("5. Delete route")
        print("0. Back to the main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")

            try:
                distance_km = float(input("Enter distance in km: "))
                base_fare = float(input("Enter base fare: "))

                route = route_manager.add_route(
                    origin,
                    destination,
                    distance_km,
                    base_fare
                )

                if route is not None:
                    print("Route added successfully.")
                    print(route)

            except ValueError:
                print("Invalid number entered.")

        elif choice == "2":
            route_manager.display_routes()

        elif choice == "3":
            destination = input("Enter destination to search: ")

            results = route_manager.search_routes(destination)

            if not results:
                print("No matching routes found.")
            else:
                print("\n----- MATCHING ROUTES -----")
                for route in results:
                    print(route)

        elif choice == "4":
            try:
                route_id = int(input("Enter route ID to update: "))

                origin = input("Enter new origin (leave blank to keep current): ")
                destination = input("Enter new destination (leave blank to keep current): ")
                distance_input = input("Enter new distance in km (leave blank to keep current): ")
                fare_input = input("Enter new base fare (leave blank to keep current): ")

                distance_km = None
                base_fare = None

                if distance_input:
                    distance_km = float(distance_input)

                if fare_input:
                    base_fare = float(fare_input)

                updated_route = route_manager.update_route(
                    route_id,
                    origin if origin else None,
                    destination if destination else None,
                    distance_km,
                    base_fare
                )

                if updated_route is None:
                    print("Route not found or invalid information entered.")
                else:
                    print("Route updated successfully.")
                    print(updated_route)

            except ValueError:
                print("Invalid number entered.")

        elif choice == "5":
            try:
                route_id = int(input("Enter route ID to delete: "))

                result = route_manager.delete_route(route_id)

                if result:
                    print("Route deleted successfully.")
                else:
                    print("Route not found.")

            except ValueError as error:
                print(error)

        elif choice == "0":
            break

        else:
            print("Feature coming next.")


def trip_menu():
    while True:
        print("\n----- TRIP MENU -----")
        print("1. Add trip")
        print("2. Display trips")
        print("3. Search trips")
        print("4. View seats")
        print("5. Update trip")
        print("6. Cancel trip")
        print("0. Back to the main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                route_id = int(input("Enter route ID: "))

                if not validate_record_exists(route_id, route_manager.routes):
                    print("Route not found.")
                    continue

                date_input = input("Enter travel date (YYYY-MM-DD): ")
                if not validate_trip_date(date_input):
                    continue

                departure_time = input("Enter departure time (HH:MM): ")
                arrival_time = input("Enter arrival time (HH:MM): ")
                if not validate_departure_and_arrival(departure_time, arrival_time):
                    continue

                total_seats = int(input("Enter total seats: "))
                if not validate_total_seats(total_seats):
                    continue

                travel_date = date.fromisoformat(date_input)

                trip = trip_manager.add_trip(
                    route_id, travel_date, departure_time, arrival_time, total_seats
                )
                print("Trip added successfully.")
                print(trip)

            except ValueError:
                print("Invalid number entered.")

        elif choice == "2":
            trip_manager.display_trips()

        elif choice == "3":
            route_input = input("Enter route ID to search (leave blank to skip): ")
            date_input = input("Enter travel date to search, YYYY-MM-DD (leave blank to skip): ")

            route_id = int(route_input) if route_input else None
            travel_date = date.fromisoformat(date_input) if date_input else None

            results = trip_manager.search_trips(route_id=route_id, travel_date=travel_date)

            if not results:
                print("No matching trips found.")
            else:
                print("\n----- MATCHING TRIPS -----")
                for trip in results:
                    print(trip)

        elif choice == "4":
            try:
                trip_id = int(input("Enter trip ID to view seats: "))
                layout = trip_manager.view_seat_layout(trip_id, ticket_manager)
                print(layout)
            except ValueError:
                print("Invalid trip ID entered.")

        elif choice == "5":
            try:
                trip_id = int(input("Enter trip ID to update: "))

                date_input = input("Enter new travel date, YYYY-MM-DD (leave blank to keep current): ")
                departure_time = input("Enter new departure time (leave blank to keep current): ")
                arrival_time = input("Enter new arrival time (leave blank to keep current): ")

                travel_date = None
                if date_input:
                    if not validate_trip_date(date_input):
                        continue
                    travel_date = date.fromisoformat(date_input)

                updated = trip_manager.update_trip(
                    trip_id,
                    travel_date=travel_date,
                    departure_time=departure_time if departure_time else None,
                    arrival_time=arrival_time if arrival_time else None
                )

                if updated:
                    print("Trip updated successfully.")
                else:
                    print("Trip not found.")

            except ValueError:
                print("Invalid number entered.")

        elif choice == "6":
            try:
                trip_id = int(input("Enter trip ID to cancel: "))
                result = trip_manager.cancel_trip(trip_id, ticket_manager)

                if result:
                    print("Trip cancelled successfully.")
                else:
                    print("Trip not found.")

            except ValueError as error:
                print(error)

        elif choice == "0":
            break

        else:
            print("Invalid choice.")

def passenger_menu():
    while True:
        print("\n----- PASSENGER / PASS MENU -----")
        print("1. Register passenger")
        print("2. Display passengers")
        print("3. Search passenger")
        print("4. Update passenger")
        print("5. Issue pass")
        print("6. Display passes")
        print("7. Renew pass")
        print("8. Suspend pass")
        print("0. Back to the main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter passenger name: ")
            phone = input("Enter passenger phone: ")

            passenger = passenger_manager.register_passenger(name, phone)

            if passenger is not None:
                print("Passenger registered successfully.")
                print(passenger)
            else:
                print("Could not register passenger.")

        elif choice == "2":
            passenger_manager.display_passengers()

        elif choice == "3":
            id_input = input("Enter passenger ID to search (leave blank to skip): ")
            name_input = input("Enter name to search (leave blank to skip): ")
            phone_input = input("Enter phone to search (leave blank to skip): ")

            try:
                passenger_id = int(id_input) if id_input else None
            except ValueError:
                print("Invalid passenger ID entered.")
                continue

            results = passenger_manager.search_passenger(
                passenger_id=passenger_id,
                name=name_input if name_input else None,
                phone=phone_input if phone_input else None
            )

            if not results:
                print("No matching passengers found.")
            else:
                print("\n----- MATCHING PASSENGERS -----")
                for passenger in results:
                    print(passenger)

        elif choice == "4":
            try:
                passenger_id = int(input("Enter passenger ID to update: "))

                name = input("Enter new name (leave blank to keep current): ")
                phone = input("Enter new phone (leave blank to keep current): ")

                updated = passenger_manager.update_passenger(
                    passenger_id,
                    name=name if name else None,
                    phone=phone if phone else None
                )

                if updated is not None:
                    print("Passenger updated successfully.")
                    print(updated)

            except ValueError:
                print("Invalid passenger ID entered.")

        elif choice == "5":
            try:
                passenger_id = int(input("Enter passenger ID: "))
                pass_type = input(
                    "Enter pass type (student/senior/priority): "
                )
                issue_date = input("Enter issue date (YYYY-MM-DD): ")
                expiry_date = input("Enter expiry date (YYYY-MM-DD): ")

                bus_pass = bus_pass_manager.issue_pass(
                    passenger_id,
                    pass_type,
                    issue_date,
                    expiry_date
                )

                if bus_pass is not None:
                    print("Bus pass issued successfully.")
                    print(bus_pass)

            except ValueError:
                print("Invalid passenger ID entered.")

        elif choice == "6":
            bus_pass_manager.display_passes()

        elif choice == "7":
            try:
                pass_id = int(input("Enter pass ID to renew: "))
                new_expiry_date = input(
                    "Enter new expiry date (YYYY-MM-DD): "
                )

                renewed = bus_pass_manager.renew_pass(
                    pass_id,
                    new_expiry_date
                )

                if renewed is not None:
                    print("Pass renewed successfully.")
                    print(renewed)

            except ValueError:
                print("Invalid pass ID entered.")

        elif choice == "8":
            try:
                pass_id = int(input("Enter pass ID to suspend: "))

                suspended = bus_pass_manager.set_pass_status(
                    pass_id,
                    "suspended"
                )

                if suspended is not None:
                    print("Pass suspended successfully.")
                    print(suspended)

            except ValueError:
                print("Invalid pass ID entered.")

        elif choice == "0":
            break

        else:
            print("Invalid choice.")

def ticket_menu():
    while True:
        print("\n----- TICKET MENU -----")
        print("1. Purchase ticket")
        print("2. Display tickets")
        print("3. Search ticket")
        print("4. Cancel ticket")
        print("0. Back to the main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                passenger_id = int(input("Enter passenger ID: "))
                trip_id = int(input("Enter trip ID: "))
                seat_number = int(input("Enter seat number: "))

                pass_input = input(
                    "Enter bus pass ID, if any (leave blank to skip): "
                )
                pass_id = int(pass_input) if pass_input else None

                ticket = ticket_manager.purchase_ticket(
                    passenger_id=passenger_id,
                    trip_id=trip_id,
                    seat_number=seat_number,
                    routes=route_manager.routes,
                    passengers=passenger_manager.passengers,
                    trips=trip_manager.trips,
                    passes=bus_pass_manager.bus_passes,
                    pass_id=pass_id
                )

                if ticket is not None:
                    print("Ticket purchased successfully.")
                    print(ticket)

            except ValueError as error:
                print(error)
            except TypeError as error:
                print(error)

        elif choice == "2":
            ticket_manager.display_all_tickets()

        elif choice == "3":
            try:
                ticket_id = int(input("Enter ticket ID to search: "))

                ticket = ticket_manager.search_ticket(ticket_id)

                if ticket is None:
                    print("No ticket found with that ID.")
                else:
                    print(ticket)

            except (ValueError, TypeError):
                print("Invalid ticket ID entered.")

        elif choice == "4":
            try:
                ticket_id = int(input("Enter ticket ID to cancel: "))

                result = ticket_manager.cancel_ticket(ticket_id)

                if result:
                    print("Ticket cancelled successfully.")

            except ValueError as error:
                print(error)
            except TypeError:
                print("Invalid ticket ID entered.")

        elif choice == "0":
            break

        else:
            print("Invalid choice.")
def main():
    load_routes(route_manager)
    load_trips(trip_manager)
    passenger_manager.passengers = load_passengers()
    bus_pass_manager.bus_passes = load_bus_passes()
    ticket_manager.tickets = load_tickets()

    while True:
        print("\n===== BUS ROUTE AND TICKETING SYSTEM =====")
        print("1. Route Management")
        print("2. Trip Management")
        print("3. Passenger / Pass Management")
        print("4. Ticket Management")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            route_menu()

        elif choice == "2":
            trip_menu()

        elif choice == "3":
            passenger_menu()

        elif choice == "4":
            ticket_menu()

        elif choice == "0":
            save_routes(route_manager)
            save_trips(trip_manager)
            save_passengers(passenger_manager.passengers)
            save_bus_passes(bus_pass_manager.bus_passes)
            save_tickets(ticket_manager.tickets)

            print("Exiting system.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
