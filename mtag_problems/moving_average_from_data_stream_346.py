'''
Given a stream of integers and a window size,
calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
'''
import collections
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        # number of elements seen so far
        self.count = 0


    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        tail = (self.head + 1) % self.size
        self.window_sum += val - self.queue[tail]
        self.head = (self.head + 1) % self. size
        self.queue[self.head] = val
        return  self.window_sum / min (self.count, self.size)



'''
class MovingAverage:

#unoptimal solution
    def __init__(self, size: int):
        self.queue = collections.deque()
        self.limit = size
        self.total_sum = 0

    def next(self, val: int) -> float:
        if len(self.queue) == self.limit:
            tail = self.queue.popleft()
            self.total_sum -= tail
        self.queue.append(val)
        self.total_sum += val
        return self.total_sum / len(self.queue)
'''
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)