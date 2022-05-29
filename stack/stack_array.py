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
        self.max_size = max_size
        self.stack_type = stack_type
        self.stack = array(["_" for _ in range(max_size)])
        self.top = -1

    def size(self) -> int:
        return self.top + 1
    
    def isEmpty(self) -> bool:
        if self.top == -1:
            return True
        return False

    def top(self) -> int:
        '''if returned value is -1, then the stack is empty'''
        if self.isEmpty():
            return -1
        return self.top

    def push(self, obj):
        '''You can only push positive numbers. 
        This function returns the status: OverflowError for failure (Overflow), 
        1 for success, ValueError if pushed value <= 0, and TypeError for not a homogeneous element.'''
        if self.size() == self.max_size:
            raise CustomOverflowError
        ## check if the object entered is homogeneous 
        if isinstance(obj, self.stack_type):
            self.top += 1
            self.stack[self.top] = obj
            return 1        
        raise TypeError(f"TypeError: element pushed is not homogeneous. Element type should be of {self.stack_type}, was {type(obj)}")
        
    def pop(self):
        '''return UnderflowError for underflow, and return the popped element for success'''
        if self.isEmpty() is False:
            popped_element = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return popped_element
        raise CustomUnderflowError

if __name__ == "__main__":

    stack1 = StackArray(max_size=2, stack_type=int)

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
    else:
        try:
            obj = 10
            print(f"pushed status? {stack1.push(obj)}")
            obj = 3
            print(f"pushed status? {stack1.push(obj)}")
            obj = 21
            print(f"pushed status? {stack1.push(obj)}")
        except CustomOverflowError as oe:
            print(f"{oe.message}, Object: {obj}")
        except ValueError as ve:
            print(ve.args[0])

    # pop
    try:
        print(f"popped element: {stack1.pop()}")
    except CustomUnderflowError as ue:
        print(ue.message)