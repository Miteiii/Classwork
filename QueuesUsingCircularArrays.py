class CIRCULARARRAYQUEUE:
    #Define the maximum number:
    DEFAULT_CAPACITY = 10

    def __init__(self):

        #Create a list/our array, with DEFAULT_CAPACITY slots, all filled with None, You can think of this as creating 10 empty parking spaces in a circular parking lot
        self._data = [None] * CIRCULARARRAYQUEUE.DEFAULT_CAPACITY

        #Here we keep track of how many elements that are actually in the list; number of cars that are parked
        self._size = 0

        #Here we keep track og the first car we parked at the lot
        self._front = 0

    def __len__(self):
        """
        This is an inbuilt constructor method or rather a dunder method, just like the __init__.
        It returns the size of an attribute created in the primary constructor
        In this case, it's elements currently in the queue. This is like counting how may cars we have in our circular parking lot.
        """
        return self._size

    def is_empty(self):
        """
        This method will return a boolean, denoted by the double equal sign operator which is a comparison operator.
        Thus, it will return True if empty the array is empty, including when it's filled is none, And false if it has at least one element.
        """
        return self._size == 0

    def first(self):
        """
        This method is analogous to the PEEK() method in stacks, which will return the element ata the front of the queue without removing it.
        Here, it like looking at the first car to be parked in the lot without making it leave.
        Or a bank teller checking the first person in the queue so as to be expectant who they are serving first
        The method will raise an Empty exception if the queue is empty.
        """

        if self.is_empty():
            raise Empty('Queue is empty') #This exception is raised by calling the class Exception and passing the exception type/message
        return self._data[self._front]

    def dequeue(self):
        """
        This method will remove and return the first element of the queue, fulfilling our principle FIFO
        We have another concept as in Circular linked list, where instead of shifting all elements left, which is slow,
        we just move our _front pointer to the next position and use MODULO
        arithmetic to wrap around when we reach the end of the array.
        """

        #Check if queue is empty
        if self.is_empty():
            raise Empty('Queue is empty')

        # Here we get the element at the front of th queue, and save it in an attribute
        item_to_dequeue = self._data[self._front]

        #Then clear the old front position to help with garbage collection

    # GARBAGE COLLECTION: is a technique/process/procedure manual or autonomous, that handles memory allocation and de-allocation, ensuring efficient use of memory.

        self._data[self._front] = None

        #Move the front pointer to the next position
        #the MODULO (%) operator makes it "wrap around", if we're at the last position then and add 1, which will go back to position 0 like a circular parking lot
        self._front = (self._front + 1) % len(self._data)

        #decrease queue size by one since we have one less item
        self._size -= 1
        """
        Ofcourse the method should return the dequeued element.
        """
        return item_to_dequeue

    def enqueue(self,element):
        """
        This is adding an element to the rear/back of our queue.
        This is like a new person joining the queue, which will be at the back of the line.

        We calculate where the "back" of the queue is using MODULO arithmetic: (front + size) % capacity
        This automatically wraps around the array when needed
        """

        #We Start with an IS_FULL check, and if true we increase the size of our queue;
        if self._size == len(self._data):
            self._resize(2 * len(self._data)) #double the capacity

            #Calculate where to put the new element(at the back of the queue)

        back_of_the_queue = (self._front + self._size) % len(self._data)

        self._data[back_of_the_queue] = element
        self._size += 1

    def _resize(self, new_capacity):

        #Create a new, bigger array
        old_data = self._data
        self._data = [None] * new_capacity

        current_index = self._front
        for item in range(self._size):
            # Copy each element to the new array in order
            self._data[item] = old_data[current_index]
            current_index = (current_index + 1) % len(old_data)

        self._front = 0

 # This is the class we spoke of earlier, with a Custom exception message for an empty queue operations
class Empty(Exception):
     """
     Exception will be raised when trying to access elements from an empty queue.
     """
     def __init__(self, message = "Queue is empty"):
         self.message = message
         super().__init__(self.message)

if __name__ == "__main__":
    queue = CIRCULARARRAYQUEUE()

    print("QUEUES USING CIRCULAR ARRAYS")
    print(f"The initial queue size is: {len(queue)}")
    print(f"Is queue empty? {queue.is_empty()}")

    print("\n Enqueueing our Queue")
    elements_to_enqueue = ['Alice', 'Bob', 'William', 'Dorothy', 'Jessica']

    for person in elements_to_enqueue:
        queue.enqueue(person)
        print(f"Added {person}. Queue size is now: {len(queue)}")

    print(f"\n Person at the front of the line: {queue.first()}")

    print("\n Serving people from the front of the queue:")
    for i in range(3):
        served_person = queue.dequeue()
        print(f"Served: {served_person}. Queue size is now: {len(queue)}")

    print("\n Adding more people to induce a wrap around in the array")
    more_people = ['Frank', 'Linda', 'Ford']

    for person in more_people:
        queue.enqueue(person)
        print(f"Added {person}. Queue size is now: {len(queue)}")

    print(f"\n Person currently at the front: {queue.first()}")
    print(f"Total people still in queue: {len(queue)}")

    print(f"\n Internal details:")
    print(f"Front index: {queue._front}")
    print(f"Array contents: {queue._data}")





