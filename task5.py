import schedule
import time
import datetime

def ky():
    current_hour = datetime.datetime.now().hour
    ku_count = current_hour % 12
    if ku_count == 0:
        ku_count = 12
    print("Ку " * ku_count)

schedule.every().hour.at(":00").do(ky)

while True:
    schedule.run_pending()
    time.sleep(1)