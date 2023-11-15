
def add_time(start, duration):

    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    print(start_time)
    return

add_time("3:00 PM", "3:10")