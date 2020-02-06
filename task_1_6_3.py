import time


class Loggable:

    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):

    def append(self, element):
        super().append(element)
        self.log(element)


# a = Loggable()
# a.log("Hi!!!")

b = LoggableList([1, 2])
b.append("3")
print(b)