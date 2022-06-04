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
        self.__cqueue = array( [None] * MAX_SIZE )
        self.__head, self.__size = 0, 0

    def size(self) -> int:
        return self.__size
    
    def is_empty(self) -> bool:
        return (self.__size == 0)
    
    def peek(self) -> array:
        return self.__cqueue
    
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
            dequeue_ele = self.__cqueue[self.__head]
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

# # OUTPUT:

# anish@Anish ~ % /opt/homebrew/opt/python@3.10/bin/python3 /Users/anish/Desktop/data_science/data_struct/custom_data_structures/queue/circular_queue.py
# C-Queue is: [None None]
# isEmpty? True
# size? 0
# Dequeue function failed.
# UnderflowError while dequeue: C-Queue is empty.
# TypeError: Object Enqueued is not homogeneous. Object type should be of <class 'int'>, was <class 'str'>
# enqueue status of 10: 1
# enqueue status of 3: 1
# OverflowError while enqueuing: C-Queue is full. First Dequeue then Enqueue., Object: 21
# C-Queue post enqueue operation: [10 3]
# Dequeue Object: 10
# C-Queue post dequeue: [None 3]
# enqueue status of 32: 1
# C-Queue post enqueue operation: [32 3]