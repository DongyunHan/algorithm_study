#heap tree testing
import random

class MinHeap:
    def __init__(self):
        self.queue = [None]

    @staticmethod
    def parent(index):
        return int(index/2)

    def insert(self, n):
        self.queue.append(n)
        i = len(self.queue) -1
        while i>1:
            parent = self.parent(i)
            if self.queue[i] < self.queue[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def swap(self, i, parent):
        temp = self.queue[i]
        self.queue[i] = self.queue[parent]
        self.queue[parent] = temp

    @staticmethod
    def leftchild(index):
        return index*2

    @staticmethod
    def rightchild(index):
        return index*2 + 1

    def pop_out(self):
        popped_value = self.queue[1]
        self.swap(1, len(self.queue) -1)
        self.queue = self.queue[:-2]
        self.minHeapify(1)

    def minHeapify(self,i):
        left = self.leftchild(i)
        right = self.rightchild(i)
        smallest = i #일단은 가장 작은 것을 자신으로 놓고
        if left <= len(self.queue)-1 and self.queue[left] < self.queue[smallest]: #만약 왼쪽 자식이 존재하고, 가장 작은 것보다 더 작으면
            smallest = left #가장작은 것은 왼쪽자식이 된다.
        if right <= len(self.queue)-1 and self.queue[right] < self.queue[smallest]: #만약 오른쪽 자식도 존재하고, 그것이 현재까지 최소보다 더 작으면
            smallest = right #가장 작은 것은 오른쪽 자식
        if smallest != i: #만약 자신이 가장 작은 것이 아니면,
            self.swap(i, smallest) #자식들 중 가장 작은 것과 바꿔주고
            self.minHeapify(smallest) #recursive call을 하여 내려가서 다시 진행


def main():
    minheap = MinHeap()
    for _ in range(10):
        minheap.insert(random.randint(1,50))

    print(minheap.queue)

if __name__ == "__main__":
    main()
