from numpy import array

class Error(Exception):
    '''Base class for other exceptions'''

class CustomUnderflowError(Error):
    def __init__(self) -> None:
        self.message = "UnderflowError while dequeue: C-Queue is empty."

class CustomOverflowError(Error):
    def __init__(self) -> None:
        self.message = "OverflowError while enqueuing: C-Queue is full. First Dequeue then Enqueue."

class CircularQueue():

    def __init__(self, MAX_SIZE, __TYPE_OBJ):
        self.__MAX_SIZE = MAX_SIZE
        self.__TYPE_OBJ = __TYPE_OBJ
        self.__cqueue = array( [None] * MAX_SIZE ) # array([None for _ in range(MAX_SIZE)])
        self.__head, self.__size = 0, 0

    def size(self) -> int:
        return self.__size
    
    def is_empty(self) -> bool:
        return (self.__size == 0)
    
    def peek(self) -> array:
        return self.__cqueue
    
    def top(self) -> any:
        return (self.peek())[self.__head]
    
    def enqueue(self, obj):
        '''returns 1 for success.'''
        # check if the object entered is homogeneous 
        if isinstance(obj, self.__TYPE_OBJ):
            if self.__size == self.__MAX_SIZE:
                raise CustomOverflowError
            self.__cqueue[(self.__head + self.__size) % self.__MAX_SIZE] = obj
            self.__size += 1
            return 1
        else:
            raise TypeError(f"TypeError: Object Enqueued is not homogeneous. Object type should be of {self.__TYPE_OBJ}, was {type(obj)}")

    def dequeue(self):
        if self.__size > 0:
            dequeue_ele = self.top()
            self.__cqueue[self.__head] = None
            self.__head =  (self.__head + 1) % self.__MAX_SIZE
            self.__size -= 1
            return dequeue_ele
        raise CustomUnderflowError

if __name__ == "__main__":

    cqueue1 = CircularQueue(2, int)

    print(f"C-Queue is: {cqueue1.peek()}")

    # size before enqueue
    print(f"isEmpty? {cqueue1.is_empty()}")
    print(f"size? {cqueue1.size()}")

    # dequeue
    try:
        print(f"Dequeue object: {cqueue1.dequeue()}")
    except CustomUnderflowError as ue:
        print("Dequeue function failed.")
        print(ue.message)

    # enqueue
    try:
        cqueue1.enqueue('a')
    except TypeError as te:
        print(te.args[0])
    finally:
        try:
            obj = 10
            print(f"enqueue status of {obj}: {cqueue1.enqueue(obj)}")
            obj = 3
            print(f"enqueue status of {obj}: {cqueue1.enqueue(obj)}")
            obj = 21
            print(f"enqueue status of {obj}: {cqueue1.enqueue(obj)}")
        except CustomOverflowError as oe:
            print(f"{oe.message}, Object: {obj}")
        except ValueError as ve:
            print(ve.args[0])
        finally:
            print(f"C-Queue post enqueue operation: {cqueue1.peek()}")

    # Dequeue
    try:
        print(f"Dequeue Object: {cqueue1.dequeue()}")
        print(f"C-Queue post dequeue: {cqueue1.peek()}")
    except CustomUnderflowError as ue:
        print(ue.message)

    # enqueue
    try:
        obj = 32
        print(f"enqueue status of {obj}: {cqueue1.enqueue(obj)}")
    except CustomOverflowError as oe:
        print(f"{oe.message}, Object: {obj}")
    except ValueError as ve:
        print(ve.args[0])
    finally:
        print(f"C-Queue post enqueue operation: {cqueue1.peek()}")

    print(f"Top: {cqueue1.top()}")
    print(f"Dequeue object: {cqueue1.dequeue()}")
    print(f"peek queue: {cqueue1.peek()}")

    print(f"Top: {cqueue1.top()}")
    print(f"Enqueue object: {cqueue1.enqueue(13)}")
    
    print(f"Top: {cqueue1.top()}")
    print(f"Dequeue object: {cqueue1.dequeue()}")

