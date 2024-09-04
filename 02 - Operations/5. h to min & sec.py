
def conv(hours: int) -> tuple[int, int]:
    minutes = hours * 60
    seconds = hours * 3600
    return minutes, seconds


hours_input = int(input("Hours: "))

minute = conv(hours_input)[0]
second = conv(hours_input)[1]

print("Minutes: {0} \nSeconds: {1}".format(minute, second))
