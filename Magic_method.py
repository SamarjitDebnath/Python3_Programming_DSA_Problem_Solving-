"""
Magic Method
Q. Add two different time which is defined by a "class Time"


@samarjit_debnath
"""


class Time:
    def __init__(self, hour=0, min=0, sec=0):
        self.hour = hour
        self.min = min
        self.sec = sec

    def __str__(self):
        return "{} : {:02d} : {:02d}".format(self.hour, self.min, self.sec)

    def __add__(self, other_time):
        newTime = Time()
        if (self.sec + other_time.sec) >= 60:
            self.min += 1
            newTime.sec = (self.sec + other_time.sec) - 60
        else:
            newTime.sec = abs(self.sec - other_time.sec)

        if (self.min + other_time.min) >= 60:
            self.hour += 1
            newTime.min = (self.min + other_time.min) - 60
        else:
            newTime.sec = abs(self.min - other_time.min)

        if (self.hour + other_time.hour) >= 24:
            newTime.hour = (self.hour + other_time.hour) - 24
        else:
            newTime.hour = self.hour + other_time.hour

        return newTime

# Driver Code


if __name__ == '__main__':
    time1 = Time(1, 20, 30)
    time2 = Time(23, 25, 35)

    print('{} + {} = {}'.format(time1, time2, (time1 + time2)))

