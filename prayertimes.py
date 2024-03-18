from praytimes import PrayTimes
from datetime import datetime, timedelta
import pytz

# Initialize PrayTimes
PT = PrayTimes()

# Set calculation method to 'MWL' (Muslim World League)
PT.setMethod('MWL')

# Adjust Fajr and Isha angles for 'MWL' method
PT.adjust({'fajr': 19.5, 'isha': 17.5})

# Set Asr method to 'Standard' (for Shafi'i, Maliki, Ja'fari, Hanbali)
PT.asrMethod = 0

# Set your location (latitude, longitude)
latitude = 31.2156
longitude = 29.9553

# Get the current date and time
current_date = datetime.now()

# Get the current date in the format [year, month, day]
current_date_list = [current_date.year, current_date.month, current_date.day]

# Get the current timezone
current_timezone = pytz.timezone('Africa/Cairo')

# Get the current timezone offset in hours from UTC
timezone_offset = current_timezone.utcoffset(current_date).total_seconds() / 3600

# Calculate prayer times
times = PT.getTimes(current_date_list, (latitude, longitude), timezone_offset)

# Subtract 20 minutes from Maghrib
maghrib_time = datetime.strptime(times['maghrib'], '%H:%M')
earlier_maghrib_time = (maghrib_time - timedelta(minutes=15)).strftime('%H:%M')
times['maghrib'] = earlier_maghrib_time

# Print prayer times
for time in ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
    print(f'{time}: {times[time.lower()]}')
