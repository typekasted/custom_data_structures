from numpy import array

class Error(Exception):
    '''Base class for other exceptions'''

class CustomUnderflowError(Error):
    def __init__(self) -> None:
        self.message = "UnderflowError while popping: Array-Stack is empty."

class CustomOverflowError(Error):
    def __init__(self) -> None:
        self.message = "OverflowError while pushing: Array-Stack is full."

class StackArray:

    def __init__(self, max_size, stack_type) -> None:
        '''In: 
            max_size: maximum size of the array
            stack_type: Element data type of the stack. e.g. int for Integer, str for String.'''
        self.__max_size = max_size
        self.__stack_type = stack_type
        self.__stack = array([None for _ in range(max_size)])
        self.__top = -1

    def size(self) -> int:
        return self.__top + 1
    
    def isEmpty(self) -> bool:
        if self.__top == -1:
            return True
        return False

    def top(self) -> int:
        '''if returned value is -1, then the stack is empty'''
        if self.isEmpty():
            return -1
        return self.__top

    def push(self, obj):
        '''This function returns the status: OverflowError for failure (Overflow), 1 for success, and TypeError for not a homogeneous element.'''
        if self.size() == self.__max_size:
            raise CustomOverflowError
        ## check if the object entered is homogeneous 
        if isinstance(obj, self.__stack_type):
            self.__top += 1
            self.__stack[self.__top] = obj
            return 1        
        raise TypeError(f"TypeError: element pushed is not homogeneous. Element type should be of {self.__stack_type}, was {type(obj)}")
        
    def pop(self):
        '''return UnderflowError for underflow, and return the popped element for success'''
        if self.isEmpty() is False:
            popped_element = self.__stack[self.__top]
            self.__stack[self.__top] = None
            self.__top -= 1
            return popped_element
        raise CustomUnderflowError
    
    def peek(self):
        return self.__stack

if __name__ == "__main__":

    stack1 = StackArray(max_size=2, stack_type=int)
    print(f"Stack is: {stack1.peek()}")

    # size before inserting
    print(f"isEmpty? {stack1.isEmpty()}")
    print(f"size? {stack1.size()}")

    # pop
    try:
        print(f"popped element: {stack1.pop()}")
    except CustomUnderflowError as ue:
        print(ue.message)
    finally:
        print("Popping function failed.")

    # push
    try:
        stack1.push('a')
    except TypeError as te:
        print(te.args[0])
    finally:
        try:
            obj = 10
            print(f"push status of {obj}: {stack1.push(obj)}")
            obj = 3
            print(f"pushed status of {obj}: {stack1.push(obj)}")
            obj = 21
            print(f"pushed status of {obj}: {stack1.push(obj)}")
        except CustomOverflowError as oe:
            print(f"{oe.message}, Object: {obj}")
        except ValueError as ve:
            print(ve.args[0])
        finally:
            print(f"Stack post push operation: {stack1.peek()}")

    # pop
    try:
        print(f"popped element: {stack1.pop()}")
    except CustomUnderflowError as ue:
        print(ue.message)

    print(f"stack post pop: {stack1.peek()}")

    print(__file__)