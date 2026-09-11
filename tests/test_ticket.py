from ticket import Ticket


ticket = Ticket(
    ticket_id=1,
    passenger_id=101,
    trip_id=5,
    seat_number=12,
    pass_id=None,
    price=50.00,
)

print(ticket)
print("Is active:", ticket.is_active())

ticket.cancel()

print(ticket)
print("Is active:", ticket.is_active())