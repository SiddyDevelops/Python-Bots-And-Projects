from datetime import date, datetime, time
from tabulate import tabulate
import pandas as pd

def break_habit(habit_name, start_date, cost_per_day, minutes_wasted):
    # Personal details
    goal = 60
    hourly_wage = 12

    # Total time ellapsed in seconds
    time_elapsed = (datetime.now() - start_date).total_seconds()

    # Convert timestamp into hours and days
    hours = round(time_elapsed/3600, 1)
    days = round(hours/24, 2)

    # Random bonus details
    money_saved = round(cost_per_day * days, 2)
    minutes_saved = round(days * minutes_wasted)
    total_money_saved = f'Rs. {round(money_saved + (minutes_saved / 60*hourly_wage), 2)}'

    # Goal (days to go)
    days_to_go = round(goal - days)

    # Change hours to days
    if hours >72:
        hours = str(days) + ' days'
    else:
        hours = str(hours) + ' hours'

    return {'habit': habit_name, 'time_since': hours, 'days_remaining': days_to_go, 'minutes_saved': minutes_saved,
                                 'money_saved': money_saved}        



habits = [
    break_habit('Coffee',datetime(2021, 8, 22, 10, 21), cost_per_day=7, minutes_wasted= 15),
    break_habit('Beer',datetime(2021, 7, 15, 8, 00), cost_per_day=7, minutes_wasted= 15),
    break_habit('Gossip',datetime(2021, 6, 10, 12, 5), cost_per_day=7, minutes_wasted= 15)
]

df = pd.DataFrame(habits)

print(tabulate(df, headers='keys', tablefmt='psql'))