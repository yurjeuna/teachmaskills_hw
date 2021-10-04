class Range:
    def __init__(self, stop, start= None, step= None):
        if step == None:
            self.step = 1
            if start == None:
                self.start = 0
                self.stop = stop
            else:
                self.start = stop
                self.stop = start
        elif step == 0:
            raise ValueError
        else:
            self.step = step
            self.start = stop
            self.stop = start

    def is_ok(self):
        if not isinstance(self.stop, int):
            raise ValueError
        if not isinstance(self.start, int):
            raise ValueError

    def __iter__(self):
        if self.start < self.stop:
            while self.start < self.stop:
                yield self.start
                self.start += self.step
        else:
            while self.start > self.stop:
                yield self.start
                self.start -= abs(self.step)

