from route_manager import RouteManager
from utils.file_handler import load_routes, save_routes

route_manager = RouteManager()

def route_menu():
    while True:
        print("\n----- ROUTE MENU -----")
        print("1. Add route")
        print("2. Display routes")
        print("3. Search route")
        print("4. Update route")
        print("5. Delete route")
        print("0. Back")

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

        elif choice == "0":
            break

        else:
            print("Feature coming next.")

def main():
    while True:
        print("\n===== BUS ROUTE AND TICKETING SYSTEM =====")
        print("1. Route Management")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            route_menu()

        elif choice == "0":
            print("Exiting system.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()