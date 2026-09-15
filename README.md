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
