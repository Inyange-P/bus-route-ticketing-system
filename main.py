from route_manager import RouteManager
from trip_manager import TripManager
from ticket_manager import TicketManager
from utils.file_handler import load_routes, save_routes, load_trips, save_trips, load_tickets, save_tickets
from utils.validation import(
    validate_trip_date,
    validate_departure_and_arrival,
    validate_total_seats,
    validate_record_exists
)


route_manager = RouteManager()
trip_manager = TripManager()
ticket_manager = TicketManager()

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

def main():
    load_routes(route_manager)
    load_trips(trip_manager)

    while True:
        print("\n===== BUS ROUTE AND TICKETING SYSTEM =====")
        print("1. Route Management")
        print("2. Trip Management")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            route_menu()

        elif choice == "2":
            trip_menu()

        elif choice == "0":
            save_routes(route_manager)
            save_trips(trip_manager)
            print("Exiting system.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()