class Queue:
    # initialized queue constructor
    def __init__(self,max_size = None):
        self.queue = list()
        self.max_size = max_size

    # get all elements of queue
    def all(self):
        return self.queue.copy()

    # checks queue is empty or not
    def is_empty(self):
        return self.size() == 0

    # checks queue is full or not
    def is_full(self):
        return self.max_size is not None and self.size() >= self.max_size

    # add element to the queue
    def enqueue(self,item):
        if(self.max_size is None or self.max_size > self.size()):
            self.queue.append(item)
        else:
            raise Exception('Queue is full')
            
    # remove element from queue
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.queue.pop(0)

    # get the size of queue
    def size(self):
        return len(self.queue)

    # copy queue 
    def copy(self):
        return Queue(self.queue.copy())

    # checks if queue contains item or not
    def contains(self,item):
        return item in self.queue

    # clear the queue
    def clear(self):
        self.queue = list()

    # print the queue elements
    def print_queue(self):
        print(self.queue)

    # reverse the queue elements
    def reverse(self):
        return self.queue.reverse()

    # remove item from queue
    def remove(self,item):
        if item in self.queue:
            self.queue.remove(item)
        else:
            raise Exception(item,'is not in queue')

    # count number of occurance of item
    def count(self,item):
        return self.queue.count(item)

    # sort queue elements
    def sort(self,reverse=False):
        return self.queue.sort(reverse = reverse)
    # get the index of item

    def index(self,item):
        if item in self.queue:
            return self.queue.index(item)
        else:
            raise Exception('this item is not in queue')
    
    # get range of queue
    def get_range(self,start,end):
        return self.queue[start:end]


queue = Queue()
print(queue.count(5))
print(queue.is_empty())
print(queue.all())
print(queue.is_full())

queue.enqueue(5)
queue.enqueue(6)
print(queue.all())

