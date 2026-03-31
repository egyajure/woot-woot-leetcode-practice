class MedianFinder:
    # concept - we'll have a max heap for the left half of the array and a min heap for the right half
    topLeft = []
    minRight = []

    def __init__(self):
        self.topLeft = []
        self.minRight = []

    def addNum(self, num: int) -> None:
        if (len(self.topLeft) == 0):
            heapq.heappush(self.topLeft, -1 * num)
        else:
            if (num > -self.topLeft[0]):
                heapq.heappush(self.minRight, num)
            else:
                heapq.heappush(self.topLeft, -1 * num)
        
            if (len(self.topLeft) - len(self.minRight) > 1):
                # we need to balance the two heaps
                temp = heapq.heappop(self.topLeft) * -1
                heapq.heappush(self.minRight, temp)
            if (len(self.minRight) - len(self.topLeft) > 1):
                # we need to balance the two heaps
                temp = heapq.heappop(self.minRight)
                heapq.heappush(self.topLeft, -1 * temp)
        print(self.topLeft, self.minRight)

    def findMedian(self) -> float:
        if (len(self.topLeft) != 0 and len(self.minRight) != 0):
            if ((len(self.topLeft) + len(self.minRight)) % 2 != 0):
                if (len(self.topLeft) > len(self.minRight)):
                    return -1 * self.topLeft[0]
                else:
                    return self.minRight[0]
            else:
                return ((-1 * self.topLeft[0] + self.minRight[0]) / 2)
        elif (self.topLeft):
            return -1 * self.topLeft[0]
        else:
            return self.minRight[0]
        