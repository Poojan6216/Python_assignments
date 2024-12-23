class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        total_minutes %= 60
        return Time(total_hours, total_minutes)

    def displayTime(self):
        print(f"{self.hours} hr and {self.minutes} min")

    def displayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"Total minutes: {total_minutes}")

hours1 = int(input(" Enter hours for Time 1: "))
minutes1 = int(input(" Enter minutes for Time 2: "))
time1 = Time(hours1, minutes1)

hours2 = int(input(" Enter hours for Time 2: "))
minutes2 = int(input(" Enter minutes for Time 2: "))
time2 = Time(hours2, minutes2)

total_time = time1.addTime(time2)

print("Time 1:")
time1.displayTime()
print("Time 2:")
time2.displayTime()

print("Added Time:")
total_time.displayTime()
total_time.displayMinute()
