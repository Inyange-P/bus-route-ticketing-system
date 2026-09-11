from ticket import Ticket
from ticket_manager import TicketManager

manager = TicketManager()

ticket1 = Ticket(
    ticket_id=1,
    passenger_id=101,
    trip_id=1,
    seat_number=5,
    price=50
)

manager.add_ticket(ticket1)

manager.display_all_tickets()

found = manager.search_ticket(1)

if found:
    print("\nTicket found:")
    print(found)

manager.cancel_ticket(1)

manager.display_all_tickets()