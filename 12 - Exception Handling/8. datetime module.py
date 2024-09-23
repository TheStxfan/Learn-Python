import datetime

# Get today's date and time.
today_date = datetime.datetime.today()  # (year, month, day, hour, minute, second, microsecond)
print(today_date)

print()

# Display only the date and time components.
print(today_date.date())
print(today_date.time())

print()

# Print individual components of today's date and time.
print(today_date.year)
print(today_date.month)
print(today_date.day)
print(today_date.hour)
print(today_date.minute)
print(today_date.second)
print(today_date.microsecond)

print()

# Create a specific date and time.
specific_date = datetime.datetime(2019, 5, 27, 9, 5, 25)
print(specific_date)

# Demonstrate adding time with timedelta.
print(specific_date + datetime.timedelta(days=90, minutes=1))  # Adds 90 days and 1 minute.
print(specific_date + datetime.timedelta(weeks=3))              # Adds 3 weeks.
print(specific_date + datetime.timedelta(hours=48))             # Adds 48 hours.

# Timedelta allows adding specific amounts of days, seconds, microseconds, milliseconds, minutes, hours, and weeks.
