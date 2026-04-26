class MedianFinder:

    def __init__(self):
        self.numbers = []

    def addNum(self, num: int) -> None:
        self.numbers.append(num)

    def findMedian(self) -> float:
        self.numbers = sorted(self.numbers)
        length = len(self.numbers)
        if length % 2 == 0:
            result = (self.numbers[int(length/2)] + self.numbers[int(length/2 - 1)]) / 2
            return result
        else:
            index = int((length - 1) / 2)
            result = self.numbers[index]
            return result        