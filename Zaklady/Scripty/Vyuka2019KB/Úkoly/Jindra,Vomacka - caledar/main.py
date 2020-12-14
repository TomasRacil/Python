import calendar
import datetime
import argparse
	
def date(r,m):
# Funkce vypisující jednotlivé dny v zadaném měsíci/roce
	month = calendar.monthcalendar(r,m)	

	print ("\n" + calendar.month_name[m])
	for week in month:
		for day in week:
			if day == 0:
				print("  ", end ="  ")
			elif day < 10:
				print("",day, end ="  ")
			else:
				print(day, end ="  ")
		print("")

# Nastavení vlajek -m = měsíc; -r = rok
parser = argparse.ArgumentParser()
parser.add_argument('-m', metavar='měsíc', type=int, default="0", help='Zadejte měsíc současného roku, který chcete zobrazit')
parser.add_argument('-r', metavar='rok', type=int, default="0", help='Zadejte rok, který chcete zobrazit')
args = parser.parse_args()

# Pokrytí argumentu -r -m
if args.m > 0 and args.m <= 12 and args.r >= 1600:
	date(args.r, args.m)

# Pokrytí argumentu -m
elif args.m > 0 and args.m <= 12:
	now = datetime.datetime.now()
	date(now.year, args.m)

# Pokrytí argumentu -r
elif args.r >= 1600:
	for x in range(12):
		date(args.r, x+1)

