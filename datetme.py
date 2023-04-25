import datetime
# Creating datetime objects
today = datetime.date.today()
now = datetime.datetime.now()
current_time = datetime.time(now.hour, now.minute, now.second)

# Accessing and modifying individual components
year = today.year
month = today.month
day = today.day

# Formatting datetime objects as strings
formatted_date = today.strftime("%Y-%m-%d")
formatted_time = current_time.strftime("%H:%M:%S")

# Creating timedelta objects
time_difference = datetime.timedelta(days=7, hours=3)

# Performing arithmetic operations with timedelta objects
new_date = today + time_difference

# Subtracting datetime objects
date1 = datetime.date(2023, 4, 22)
date2 = datetime.date(2023, 5, 1)
date_difference = date2 - date1

# Comparing datetime objects
is_after = date1 > date2

# Scheduling events
event_date = datetime.datetime(2023, 6, 1, 18, 0)
time_until_event = event_date - now

# Calculating age
birth_date = datetime.date(1990, 1, 1)
age = (today - birth_date).days // 365

# Handling time zones
from datetime import timezone
utc_time = datetime.datetime.now(timezone.utc)

# Working with alternative calendar systems
import calendar
is_leap = calendar.isleap(year)
