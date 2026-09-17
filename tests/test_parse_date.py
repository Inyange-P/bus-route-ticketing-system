from datetime import date, datetime
from utils.validation import parse_date

print("Parsing a text date:")
print(parse_date("2026-06-15"))

print("\nParsing a real date object:")
print(parse_date(date(2026, 6, 15)))

print("\nParsing a real datetime object:")
print(parse_date(datetime(2026, 6, 15, 14, 30)))



