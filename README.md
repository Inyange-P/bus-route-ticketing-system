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

## Route Management

The Route Management section handles the journeys offered by the bus company.

Each route stores the following information:

- Route ID
- Origin
- Destination
- Distance in kilometres
- Base fare

The Route Management menu allows the user to:

- Add a route
- Display available routes
- Search for a route by destination
- Update route details
- Delete a route

Route IDs are generated automatically by the system.

The system also validates route information before it is accepted. The origin and destination cannot be empty, the distance must be greater than zero, and the base fare cannot be negative.

Route information is saved to file when the program exits and loaded again when the application starts, so previously created routes are not lost between sessions.
