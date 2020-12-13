import calendar
import datetime
import argparse

def month(m):
	now = datetime.datetime.now()
	month = calendar.monthcalendar(now.year,m)
	for week in month:
		for day in week:
			if day == 0:
				print("  ", end ="  ")
			elif day < 10:
				print("",day, end ="  ")
			else:
				print(day, end ="  ")
		print("")


parser = argparse.ArgumentParser()
parser.add_argument('-m', metavar='měsíc', type=int, default="0", help='Zadejte měsíc současného roku který chcete zobrazit')
args = parser.parse_args()

if args.m > 0 and args.m <= 12:
	month(args.m)