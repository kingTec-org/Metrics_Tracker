import time
from datetime import timedelta
import datetime


def current_time():
	while True:
		localtime = time.localtime()
		result = time.strftime("%H%M", localtime)
		print(result)
		time.sleep(60)



def flight_period(entry_time, exit_time, entry_date, exit_date):
	flight_time_of_entry = datetime.datetime.strptime(entry_time, "%H%M")
	flight_date_of_entry = datetime.datetime.strptime(entry_date, "%d %b %Y")
	flight_time_of_exit = datetime.datetime.strptime(exit_time, "%H%M")
	flight_date_of_exit = datetime.datetime.strptime(exit_date, "%d %b %Y")

	hours_flown = flight_time_of_exit - flight_time_of_entry

	seconds_flown = datetime.timedelta.total_seconds(hours_flown)
	seconds_flown = int(seconds_flown)

	hours, remainder = divmod(seconds_flown, 60 * 60)
	minutes, seconds = divmod(remainder, 60)

	hours = str(hours)
	minutes = str(minutes)

	if len(hours) == 1:
		hours = str(0)+hours

	if len(minutes) == 1:
		minutes = str(0)+minutes

	hours_flown_string = (f'{hours}{minutes}')

	print(hours_flown_string)
	print(flight_date_of_entry, flight_date_of_exit)


#entry_time = input("Enter Start Time: ")
#exit_time = input("Enter End Time: ")
#entry_date = input("Enter ATO T/O Date: ")
#exit_date = input("Enter ATO Land Date; )"

#flight_period(entry_time, exit_time, entry_date=date, exit_date=date)
