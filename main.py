from datetime import datetime
import logging
import pytz


# Define the timezone for Réunion

logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.DEBUG)

def get_time():
    logging.info(f"Lancement du traitement")
    
    reunion_tz = pytz.timezone('Indian/Reunion')

    # Get the current time in Réunion
    current_time_reunion = datetime.now(reunion_tz).strftime('%H:%M:%S')

    print(f"Il est {current_time_reunion} à la Réunion")

if __name__ == "__main__":
    get_time()