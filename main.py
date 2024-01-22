from datetime import datetime

import pytz



# Define the timezone for Réunion

reunion_tz = pytz.timezone('Indian/Reunion')



# Get the current time in Réunion

current_time_reunion = datetime.now(reunion_tz)



current_time_reunion = current_time_reunion.strftime('%H:%M:%S')

print(f"Il est {current_time_reunion} à la Réunion")