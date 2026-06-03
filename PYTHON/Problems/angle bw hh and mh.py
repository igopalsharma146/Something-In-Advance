#compute the smallest angle in degrees between the hour and minute hands of an analog clock.
def clock_angle(hour, minute):
    if hour < 0 or minute < 0 or minute > 60:
        return "Invalid input"
    if hour == 12:
        hour = 0
    if minute == 60:
        minute = 0
        hour += 1
    if hour > 12:
        hour = hour - 12
    hour_angle = (hour * 60 + minute) * 0.5
    minute_angle = minute * 6
    angle = abs(hour_angle - minute_angle)
    angle = min(360 - angle, angle)
    return angle
# Example usage
hour = 1
minute = 15
print(clock_angle(hour, minute))