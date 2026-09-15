# Bus Route and Ticketing Management System

## Introduction

This project is a Python application developed for a bus company to manage routes, trips, passengers, bus passes, and tickets.

The system allows users to manage bus routes and trips, register passengers, issue bus passes, check seat availability, purchase and cancel tickets, and calculate ticket prices. Information is also saved to files so that it can be loaded again when the application starts.

The project was developed as a group summative assignment and demonstrates Python concepts such as classes and objects, functions, conditional statements, loops, file handling, exception handling, input validation, and testing.

## Installation

1. Make sure Python and Git are installed.
2. Clone the repository:
```bash
git clone https://github.com/Inyange-P/bus-route-ticketing-system.git
```

3. Open the project folder:
```
cd bus-route-ticketing-system
```

4. Install pytest for running the automated tests:
```
python -m pip install pytest
```

## How to Run

From the project folder, run:
```
python main.py
```

Follow the menu options displayed in the terminal to use the system.

## Running Tests

Run the automated tests from the project root using:
```
python -m pytest
```

## Features

The system includes:

- Route management
- Trip and seat management
- Passenger management
- Bus pass management
- Ticket purchasing and cancellation
- Ticket price calculation
- Search and display functions
- Input validation and error handling
- Saving and loading data between sessions

## System Architecture

The system is Organized around independent modules that each manages one part of the bus ticketing process:

- **Route Management** - stores the journeys the bus company offers (origin, destination, distance, base fare)
- **Trip Management** – schedules actual bus trips that run on a route (date, departure/arrival time, seat count)
- **Passenger and BusPass Management** – registers passengers and issues discount passes
- **Ticket Management** – handles ticket purchase, pricing, and cancellation, and is the single source of truth for which seats are occupied


Each module has its own manager class (e.g. `TripManager`, `RouteManager`) that stores its records in a dictionary keyed by ID, and its own validation functions in `utils/validation.py`. Data is saved to and loaded from JSON files using shared functions in `utils/file_handler.py`, so information persists between sessions. All modules are connected together through the menus in `main.py`.

## Trip and Route Relationship

A **Trip** represents one scheduled journey on a specific date and time, and it always belongs to exactly one **Route**.

- The Route defines the journey itself — where it goes and what it costs as a base fare.
- The Trip defines when that journey actually happens — a specific date, departure time, arrival time, and how many seats are available.

Multiple trips can be created for the same route (for example, the same Beau Plan–Grand Baie route running on different days), but a trip cannot exist without a valid route. When a trip is created, the system checks that the given route ID actually exists before allowing the trip to be scheduled.

This relationship also matters for pricing: when a ticket is purchased for a trip, the system looks up the trip's route to find the base fare, then applies any relevant bus pass discount on top of it.

## Seat Management

Seat availability for a trip is not tracked separately — it is determined directly from active tickets, so there is only one source of truth for whether a seat is taken.

- Each trip has a fixed number of total seats.
- A seat is considered available if no active ticket exists for that trip and seat number.
- When a ticket is purchased, the seat becomes occupied because a matching ticket now exists.
- When a ticket is cancelled, the seat becomes available again automatically, since the ticket is no longer active.

This means booking a seat and buying a ticket are the same action — there's no separate "reserve a seat" step that could get out of sync with actual ticket records. The Trip menu's "View seats" option displays a simple seat map (e.g. `[1:O] [2:X] [3:O]`) by checking every seat number against the ticket system, where `O` means open and `X` means occupied.

A trip can only be cancelled if it has no active tickets, preventing a trip from being removed while passengers still hold valid tickets for it.



## Passenger and BusPass Management

A **Passenger** represents one person registered in the system, identified by a passenger ID, name, and phone number. Before a passenger is created or updated, the system checks that the name isn't empty and that the phone number is a valid length of digits; invalid details are rejected rather than silently accepted.

A **BusPass** belongs to exactly one passenger and grants a fare discount or free travel, depending on its type:

- **Student** — reduced fare
- **Senior** — free travel
- **Priority** — free travel

Each pass also has an issue date, an expiry date, and a status (`active`, `suspended`, or `cancelled`). A passenger can only hold one active pass at a time; attempting to issue a second active pass to the same passenger is rejected. Dates are validated so that a pass's expiry date must always come after its issue date, and can be provided as either a text date (`"2026-01-01"`) or a real `date`/`datetime` object, since different parts of the system pass dates around in different formats.

Whether a pass can actually be used on a given travel date is decided by a single check (`is_pass_valid`), which confirms the pass is still `active` and that the travel date falls on or before the expiry date. A pass that is expired, suspended, or cancelled is treated the same way as having no pass at all, the full fare applies.

## Pricing Rules

When a ticket is purchased, the price starts from the base fare of the trip's route, then is adjusted based on the passenger's pass, if they have one and it is currently valid:

- **No pass, or an invalid/expired pass** → full base fare
- **Valid student pass** → reduced fare
- **Valid senior or priority pass** → free travel

This means the same route can produce different ticket prices for different passengers, depending entirely on whether they hold a currently valid pass at the time of purchase — a pass that expired the day before travel does not apply, and the passenger is charged full fare instead.

## Ticketing Workflow

The ticketing process connects several parts of the system. A ticket is only created after the required information has been checked.

When a passenger wants to purchase a ticket, the system first checks that the passenger and trip exist. Since every trip belongs to a route, the route is then used to find the base fare. The system also checks the selected seat and makes sure that it is available.

If the passenger provides a bus pass, the system checks whether the pass exists, belongs to that passenger, is active, and is valid for the travel date. The appropriate discount is then applied based on the type of pass.

After all the required checks are successful, the system calculates the final ticket price and creates the ticket.

The main steps are:

1. Check that the passenger exists.
2. Check that the trip exists.
3. Find the route connected to the trip.
4. Get the base fare from the route.
5. Check that the seat number is valid.
6. Check that the seat is not already occupied by an active ticket.
7. Validate the bus pass if one is provided.
8. Calculate the final ticket price.
9. Create and store the ticket.

The ticket contains information such as the ticket ID, passenger ID, trip ID, seat number, bus pass ID when applicable, price, purchase date, and ticket status.

### Seat Availability

The system does not keep a separate list of reserved seats. Instead, seat availability is determined from the ticket records.

If an active ticket exists for a particular trip and seat, that seat is considered occupied. If there is no active ticket for that seat, it is considered available.

---

## Validation and Error Handling

Validation is used throughout the system to prevent incorrect information from being stored.

The reusable validation functions are mainly located in `utils/validation.py`. They are used for different parts of the application, including passengers, routes, trips, bus passes, and tickets.

Some of the checks include:

* Passenger name validation
* Phone number validation
* Pass type validation
* Date validation
* Date order validation
* Trip date validation
* Time format validation
* Departure and arrival time validation
* Seat number validation
* Positive number validation
* Fare and distance validation
* Record existence checks
* Status validation

The system also handles invalid user input using exception handling. For example, if a user is asked to enter a passenger ID and enters letters instead of a number, the application does not crash.

Example:

```text
Enter passenger ID: abc
Invalid passenger ID entered.
```

The user can continue using the system after the error.

The project also checks business rules, not only data types. A value can have the correct format but still be invalid for the system.

For example, seat number `5` is a valid integer, but it should still be rejected if the trip only has four seats or if seat 5 is already occupied.

Some of the business rules checked by the system include:

* A trip must belong to an existing route.
* A ticket must belong to an existing passenger and trip.
* A seat cannot be sold twice while the previous ticket is active.
* A passenger cannot have more than one active bus pass.
* An expired, suspended, or cancelled pass cannot provide a fare benefit.
* A trip cannot be cancelled while it still has active tickets.
* A route should not be removed when it is still being used by trips.
* Invalid dates and times are rejected.
* Invalid passenger information is rejected.

This makes the validation part of the actual business logic of the system rather than treating it as only input formatting.

---

## Data Persistence

The system uses JSON files to save information between program sessions.

The main data files are:

```text
routes.json
trips.json
passengers.json
bus_passes.json
tickets.json
```

The functions responsible for saving and loading data are located in `utils/file_handler.py`.

When the program starts, the existing JSON files are loaded into the appropriate managers. When the user exits the program normally, the current data is saved again.

This allows information such as passengers, bus passes, and tickets to remain available when the application is opened again.

The project separates file handling from the main business logic. The manager classes focus on creating, updating, searching, and deleting records, while `file_handler.py` is responsible for saving and loading those records.

If a JSON file does not exist, the application starts with an empty collection instead of stopping with an error.

---

## Data Relationships

The different parts of the system are connected through their IDs.

A route represents a journey between two locations and contains information such as the distance and base fare.

A trip represents a particular scheduled journey on a route. It contains information such as the travel date, departure time, arrival time, and number of seats.

A passenger represents a person registered in the system.

A bus pass belongs to a passenger and can provide a fare benefit.

A ticket connects a passenger to a particular trip and seat. It also stores the final price and the bus pass used, if applicable.

The relationships can be understood as follows:

* One route can have multiple trips.
* One trip can have multiple tickets.
* One passenger can have multiple tickets.
* A passenger can have one active bus pass.
* A ticket belongs to one passenger and one trip.
* A ticket can optionally be linked to a bus pass.

These relationships are important because one record can depend on another. For example, a trip cannot be properly created without a valid route, and a ticket cannot be purchased without a valid trip.

---

### Using Manager Classes

The project separates the classes that represent individual records from the classes that manage those records.

For example, `Passenger` represents one passenger, while `PassengerManager` handles passenger operations such as registration, searching, and updating.

The same idea is used for routes, trips, bus passes, and tickets.

The manager classes store records using dictionaries with IDs as keys. This makes it easier to find and work with a particular record.

### Keeping Route and Trip Separate

Routes and trips are separate because the same route can be used for many different trips.

For example, a route from Beau Plan to Grand Baie could have a trip on Monday morning and another trip on Tuesday afternoon.

The route describes where the journey goes, while the trip describes when that particular journey takes place.

This also makes pricing easier because the trip can use the base fare stored in its route.

### Using Tickets to Determine Seat Availability

The system does not create a separate seat reservation record.

Instead, an active ticket means that the corresponding seat is occupied.

This was chosen to avoid maintaining two different records for the same information. If both a seat record and a ticket record were used, they could potentially disagree after a ticket was cancelled.

Using active tickets as the source for seat availability keeps the process simpler and reduces duplication.

### Reusing Validation Functions

Common validation rules are kept in `utils/validation.py`.

This avoids writing the same validation logic in multiple classes and makes the rules easier to maintain.

### Centralizing File Handling

Saving and loading are handled through `utils/file_handler.py`.

This keeps JSON operations separate from the manager classes and makes the overall structure easier to understand.

---

## Edge Cases Considered

The system was designed to handle both successful operations and situations where the user provides incorrect information or tries to perform an operation that should not be allowed.

Some examples include:

| Situation                            | Expected behaviour                                           |
| ------------------------------------ | ------------------------------------------------------------ |
| Passenger does not exist             | The operation is rejected                                    |
| Route does not exist                 | Trip creation is rejected                                    |
| Trip does not exist                  | Ticket operation is rejected                                 |
| Invalid date                         | The operation is rejected                                    |
| Past travel date                     | The operation is rejected                                    |
| Invalid seat number                  | Ticket purchase is rejected                                  |
| Seat is already occupied             | Another ticket cannot be created for that seat               |
| Invalid passenger details            | Registration or update is rejected                           |
| Invalid pass type                    | Pass creation is rejected                                    |
| Passenger already has an active pass | Another active pass is rejected                              |
| Pass has expired                     | Pass benefit is not applied                                  |
| Pass is suspended                    | Pass benefit is not applied                                  |
| Pass is cancelled                    | Pass benefit is not applied                                  |
| Invalid ticket ID                    | Ticket operation is rejected                                 |
| Ticket is already cancelled          | It cannot continue as an active booking                      |
| Trip has active tickets              | Trip cancellation is prevented                               |
| Route has dependent trips            | Route removal is prevented where the relationship is checked |
| JSON file does not exist             | The application starts with an empty collection              |

Considering these cases was important because a management system should not only work when the user enters everything correctly. It should also respond properly when something goes wrong.

---

## Examples of Usage

### Registering a Passenger

From the main menu, select:

```text
3. Passenger / Pass Management
```

Then select:

```text
1. Register passenger
```

The user enters the passenger's name and phone number.

Example:

```text
Name: Aline Uwase
Phone: 57987654
```

If the information is valid, the system creates the passenger and assigns an ID.

---

### Issuing a Bus Pass

From Passenger / Pass Management, select:

```text
5. Issue pass
```

The user enters the passenger ID, pass type, issue date, and expiry date.

Example:

```text
Passenger ID: 3
Pass type: student
Issue date: 2026-09-15
Expiry date: 2027-01-15
```

The system validates the information and creates the bus pass if all the requirements are satisfied.

---

### Purchasing a Ticket

From the main menu, select:

```text
4. Ticket Management
```

Then select:

```text
1. Purchase ticket
```

The user provides the passenger ID, trip ID, seat number, and optionally a bus pass ID.

Example:

```text
Passenger ID: 3
Trip ID: 1
Seat number: 5
Bus pass ID: 2
```

The system then checks the passenger, trip, route, seat, and bus pass before calculating the final fare.

The user does not manually enter the ticket price. The system calculates it from the route fare and the applicable bus pass rules.

---

### Buying an Occupied Seat

If another passenger already has an active ticket for Seat 5 on Trip 1, another passenger cannot purchase Seat 5 for the same trip.

The system rejects the purchase instead of replacing the existing ticket.

The passenger can view the available seats and select another seat.

---

### Viewing Seat Availability

From Trip Management, the user can select the option to view seats for a trip.

The system checks the active tickets for that trip and displays the current seat availability.

For example:

```text
[1:O] [2:X] [3:O] [4:O] [5:X]
```

In this example:

```text
O = Open
X = Occupied
```

The seat information comes from the ticket records.

---

### Applying a Student Discount

Suppose a route has a base fare of Rs 50.00 and the passenger has a valid student pass.

The ticket price is calculated by the system according to the student fare rule.

For example:

```text
Base fare: Rs 50.00
Student discount: 50%
Final price: Rs 25.00
```

The passenger does not need to calculate or enter the discounted price themselves.

---

### Free Travel

A valid senior or priority pass gives free travel according to the project's pricing rules.

For example:

```text
Base fare: Rs 50.00
Pass benefit: Free travel
Final price: Rs 0.00
```

If the pass is expired, suspended, or cancelled, the pass benefit is not applied and the normal fare is used.

---

### Cancelling a Ticket

From Ticket Management, select:

```text
4. Cancel ticket
```

The user enters the ticket ID.

A cancelled ticket remains in the system with its cancelled status rather than simply being deleted.

Since only active tickets count as occupied seats, cancelling a ticket makes that seat available again.

For example:

```text
Before cancellation:
Seat 5 = Occupied

After cancellation:
Seat 5 = Open
```

This keeps the ticket record while also keeping the seat information correct.

---

## Project Structure
```

The main responsibilities are divided as follows:

* Model classes represent individual records.
* Manager classes handle operations and business rules.
* `validation.py` contains reusable validation functions.
* `file_handler.py` handles saving and loading data.
* The `tests` directory contains automated tests.
* `main.py` connects the different managers through the user menus.
---


## Limitations and Future Improvements

The current project focuses on the requirements of the summative assignment. However, there are several areas that could be developed further.

Possible future improvements include:

* A graphical or web-based interface
* User authentication and different user roles
* Online payment processing
* Automatic ticket confirmation by email or SMS
* More detailed seat layouts
* Sales and revenue reports
* Searching and filtering trips by date or destination
* Using a database instead of JSON files for larger amounts of data
* Better support for multiple users purchasing tickets at the same time
* An administrative dashboard for managing the whole system

These improvements are outside the current scope of the project, but the current separation between models, managers, validation, file handling, tests, and the main menu provides a good foundation for extending the system in the future.



