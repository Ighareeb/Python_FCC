# Time Calculator
def add_time(start, duration, day=None):
    days_of_the_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    start_time, am_pm = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    duration_hour, duration_minute = map(int, duration.split(":"))

    if am_pm.lower() == "pm":
        start_hour += 12

    total_minutes = (start_minute + duration_minute) % 60
    total_hours = start_hour + duration_hour + (start_minute + duration_minute) // 60
    days_passed = total_hours // 24
    final_hour = (
        total_hours % 24
    )  # account for remaining hours after whole days_passed are calculated

    if final_hour >= 12:
        final_am_pm = "PM"
        if final_hour > 12:
            final_hour -= 12
    else:
        final_am_pm = "AM"
        if final_hour == 0:
            final_hour = 12

    if day:
        day_index = (days_of_the_week.index(day.capitalize()) + days_passed) % 7
        final_day_of_week = ", " + days_of_the_week[day_index]
    else:
        final_day_of_week = ""

    if days_passed == 0:
        days_later = ""
    elif days_passed == 1:
        days_later = " (next day)"
    else:
        days_later = f" ({days_passed} days later)"

    if final_day_of_week:
        new_time = f"{final_hour}:{total_minutes:02d} {final_am_pm}, {final_day_of_week}{days_later}"
    else:
        new_time = f"{final_hour}:{total_minutes:02d} {final_am_pm}{days_later}"

    return new_time


# Function should add duration to start time and return result.
# a start time in the 12-hour clock format (ending in AM or PM)
# a duration time that indicates the number of hours and minutes
# (optional) a starting day of the week, case insensitive
# If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.
# If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.
