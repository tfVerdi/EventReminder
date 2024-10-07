import datetime
import time
from dataclasses import dataclass


date_now = datetime.datetime.now()


@dataclass
class Month:
    name     : str
    abr      : str
    num_days : int
    nOrder   : int
    events   : dict

if __name__ == "__main__":
    start = time.time()
    print(f"Current Date is {date_now.day}/{date_now.month}/{date_now.year}\n\n")

    # ---------------------IMPORTANT-DATES---------------------

    events_Jan = {
        9 : "Example"
        }

    events_Feb = {
        11: "Tattoo", 14 : "Valentine's Day"
        }

    events_Mar = {
        2 : "Event",
        11 : "Start of 2024-1"
        }

    events_Apr = {
        21 : "Cool day"
        }

    events_May = {
        5 : "Special day"
        }

    events_Jun = {}

    events_Jul = {
        12 : "Winter holidays\nEnd 2024-1",
        23 : "Pancake day"
        }

    events_Aug = {
        5 : "Start 2024-2"
        }

    events_Sep = {}

    events_Oct = {}

    events_Nov = {}

    events_Dec = {
        27: "Summer holidays\nEnd 2024-2"
        }

    # -----------------------MONTH-STATS-----------------------

    january   = Month("January",   "Jan", 31, 1,   events_Jan)
    february  = Month("February",  "Feb", 28, 2,   events_Feb)
    march     = Month("March",     "Mar", 31, 3,   events_Mar)
    april     = Month("April",     "Apr", 30, 4,   events_Apr)
    may       = Month("May",       "May", 31, 5,   events_May)
    june      = Month("June",      "Jun", 30, 6,   events_Jun)
    july      = Month("July",      "Jul", 31, 7,   events_Jul)
    august    = Month("August",    "Aug", 31, 8,   events_Aug)
    september = Month("September", "Sep", 30, 9,   events_Sep)
    october   = Month("October",   "Oct", 31, 10,  events_Oct)
    november  = Month("November",  "Nov", 30, 11,  events_Nov)
    december  = Month("December",  "Dec", 31, 12,  events_Dec)

    all_months = {1 : january, 2 : february, 3 : march, 4 : april, 5 : may, 6 : june, 7 : july, 8 : august, 9 : september, 10 : october, 11 : november, 12 : december}

    # -----------------------PROCESSING------------------------

    current_month = all_months[date_now.month]

    if date_now.month != 12 and date_now.month != 1:
        next_month = all_months[date_now.month + 1]
        last_month  = all_months[date_now.month - 1]
    elif date_now.month == 12:
        next_month = january
        last_month = november
    elif date_now.month == 1:
        next_month = february
        last_month = december
        
    events_to_show = []

    if (date_now.day + 7) > current_month.num_days:      # Si es que en una semana más estaremos en el mes siguiente
        for i in range(current_month.num_days - date_now.day, current_month.num_days + 1): 
        # "Por cada día posterior al día actual y correspondiente al mes actual"
            try:
                current_month.events[i]
            except KeyError:
                continue
            else:
                events_to_show.append(f"{current_month.abr} {i}: {current_month.events[i]}")
                
        for i in range(1, 7 - (current_month.num_days - date_now.day) + 1):
        # "Por cada día del mes próximo necesario para que la suma de días totales analizados sea 7"
            try:
                next_month.events[i]
            except KeyError:
                continue
            else:
                events_to_show.append(f"{next_month.name} {i}: {next_month.events[i]}")
            
    elif (date_now.day - 7) < 1:                     # Si hace una semana estabamos en el mes anterior
        for i in range(last_month.num_days - (7 - date_now.day), last_month.num_days + 1):
        # "Por cada día del mes anterior necesario para que la suma de días totales analizados sea 7"
            try:
                last_month.events[i]
            except KeyError:
                continue
            else:
                events_to_show.append(f"{last_month.name} {i}: {last_month.events[i]}")
                
        for i in range(1, date_now.day + 1):
        # "Por cada día anterior al día actual y correspondiente al mes actual"
            try:
                current_month.events[i]
            except:
                continue
            else:
                events_to_show.append(f"{current_month.name} {i}: {current_month.events[i]}")
                
        for i in range(date_now.day, date_now.day + 7):
        # "Por cada día anterior al día actual y correspondiente al mes actual"
            try:
                current_month.events[i]
            except:
                continue
            else:
                events_to_show.append(f"{current_month.name} {i}: {current_month.events[i]}")

    else:                                           # Si es que estamos analizando solo días de este mes
        for i in range(1, 15 + 1):
            try:
                day_to_analyze = date_now.day - 8 + i
                current_month.events[day_to_analyze]
            except:
                continue
            else:
                if day_to_analyze != date_now.day:
                    events_to_show.append(f"{current_month.name} {day_to_analyze}: {current_month.events[day_to_analyze]}")

    match len(events_to_show):
        case 0:
            print("There are no events near the current date.")
        case 1:
            print(events_to_show[0])
        case _:
            for event in events_to_show:
                print(event)   

    # ---------------------EVENTS-TODAY------------------------

    try:
        current_month.events[date_now.day]
    except:
        pass
    else:
        if "\n" in current_month.events[date_now.day]:
            string_today = current_month.events[date_now.day].split("\n")
        else:
            string_today = [(current_month.events[date_now.day])]
        print("\nTODAYTODAYTODAYTODAYTODAYTODAYTODAYTODAYTODAYTODAYTODAYTODAY")
        if len(string_today) != 1:
            for i in string_today:
                print(i)
        else:
            print(string_today[0])
        print("TODAYTODAYTODAYTODAYTODAYTODAYTODAYTODAYTODAYTODAYTODAYTODAY")
    end = time.time()
    print(f'\n[{end - start}s.]')
    close = input("Press ENTER to close\n")