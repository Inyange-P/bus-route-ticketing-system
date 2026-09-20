# Bus Route & Ticketing Management System

## Team Members

1. Abigail Johnson Inyang
2. Chinelo Nnamdi Kanu 
3. Providence Inyange
4. Moses Kolaan 

## Project Description

The Bus Route & Ticketing Management System is a Python application for managing bus routes, trips, passengers, bus passes, and tickets.

The system allows users to add and search routes, register passengers, create trips, check seat availability, purchase and cancel tickets, calculate ticket prices, and save information so that it can be loaded again when the program starts.

## Main Features

- Add, display, search, update and delete bus routes
- Add, display, search, update and cancel trips
- Register, display, search and update passenger information
- Issue, renew, search and suspend bus passes
- Check seat availability
- Purchase tickets
- Calculate ticket prices
- Display and search purchased tickets
- Cancel tickets
- Validate user input
- Handle invalid input without crashing
- Save and load information from files

## Classes Used

### Route

Represents one bus route and stores information such as the origin, destination, distance and base fare.

### RouteManager

Manages route operations such as adding, displaying, searching, updating and deleting routes.

### Trip

Represents one scheduled journey on a route and stores the travel date, departure time, arrival time and number of seats.

### TripManager

Manages trips, including creating, searching, updating and cancelling trips and checking seat availability.

### Passenger

Represents one registered passenger and stores the passenger's ID, name and phone number.

### PassengerManager

Manages passenger registration, searching, displaying and updating passenger information.

### BusPass

Represents a bus pass issued to a passenger and stores the pass type, issue date, expiry date and status.

### BusPassManager

Manages bus passes, including issuing, searching, renewing, validating and changing pass status.

### Ticket

Represents one purchased ticket and stores the passenger, trip, seat number, bus pass used, price and ticket status.

### TicketManager

Manages ticket purchases, ticket prices, ticket searches, cancellations and occupied seats.

## Files Used

The system uses JSON files to save information between program sessions.

- `routes.json` stores route information.
- `trips.json` stores trip information.
- `passengers.json` stores passenger information.
- `bus_passes.json` stores bus pass information.
- `tickets.json` stores ticket information.

The file-handling functions are located in `utils/file_handler.py`.

## How to Run the Application

Make sure Python is installed.

Open the project folder in a terminal and run:

```bash
python main.py
```

To run the automated tests:
```
python -m pytest
```

## Team Contributions
### Abigail Johnson Inyang
- Created the Route and RouteManager classes.
- Implemented route creation, display, search, update and deletion.
- Added route validation and route file handling.
- Integrated Route Management into the main menu.
- Worked on testing, final validation checks and project documentation.
### Providence Inyange
- Worked on the Ticket and TicketManager classes.
- Implemented ticket purchasing, ticket price calculation, ticket searching and ticket cancellation.
- Added ticket validation and ticket file handling.
- Helped integrate ticket and passenger functionality into the main application.
- Worked on the Test Plan and README documentation.
### Chinelo Nnamdi Kanu 
- Created the Passenger, PassengerManager, BusPass and BusPassManager classes.
- Implemented passenger registration, searching and updating.
- Implemented bus pass issuing, validation, renewal and status changes.
- Added passenger and bus pass file handling and validation.
- Worked on testing and documentation.
### Moses Kolaan
- Created the Trip and TripManager classes.
- Implemented trip creation, searching, updating and cancellation.
- Implemented seat availability and seat layout functionality.
- Added trip validation and trip file handling.
- Worked on the class diagram and Trip-related documentation.
