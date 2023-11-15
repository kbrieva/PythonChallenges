def add_time(start, duration, day=None):
    # Parse the start time
    start_time, am_pm = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    if am_pm == "PM":
        start_hour += 12 if start_hour != 12 else 0

    # Parse the duration
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Calculate the new time
    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute

    # Adjust for carryover minutes
    new_hour += new_minute // 60
    new_minute %= 60

    # Calculate the number of days passed
    days_passed = new_hour // 24
    new_hour %= 24

    # Determine the new AM/PM
    new_am_pm = "AM" if new_hour < 12 else "PM"
    new_hour = new_hour % 12 if new_hour % 12 != 0 else 12

    # Calculate the new day of the week if specified
    if day:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_index = (days.index(day.capitalize()) + days_passed) % 7
        new_day = days[day_index]
    else:
        new_day = ""

    # Create the new time string
    new_time = f"{new_hour}:{new_minute:02d} {new_am_pm}"
    if new_day:
        if days_passed == 1:
            new_time += f", {new_day} (next day)"
        elif days_passed > 1:
            new_time += f", {new_day} ({days_passed} days later)"
        else:
            new_time += f", {new_day}"
    else:
        if days_passed == 1:
            new_time += " (next day)"
        elif days_passed > 1:
            new_time += f" ({days_passed} days later)"

    return new_time