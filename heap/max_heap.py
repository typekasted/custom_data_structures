# Build Max-Heap

from io import StringIO
import math

def max_heapify_bottom_up(A, HEAP_SIZE, idx):
    """
    A -> heap array
    HEAP_SIZE -> heap size
    idx -> the index of the node of a tree / subtree to start heapify with
    """

    left_idx  = (2 * idx) + 1
    right_idx = (2 * idx) + 2

    # initialize largest as the root idx of the tree / subtree
    largest = idx

    # if left child is larger than the root, then, make the left child idx as the largest, else mark idx as largest
    if (left_idx <  HEAP_SIZE) and (A[left_idx] > A[idx]):
        largest = left_idx
    else:
        largest = idx
    
    # If right child is larger than largest so far, then, make the right child idx as the largest
    if (right_idx <  HEAP_SIZE) and (A[right_idx] > A[largest]):
        largest = right_idx
    
    # If largest is not root, then swap root with largest child, and call max_heapify again recursively
    if largest != idx:
        A[idx], A[largest] = A[largest], A[idx]
        # Recursively heapify the affected sub-tree
        max_heapify_bottom_up(A, HEAP_SIZE, largest)


def build_max_heap(A):
    """# Function to build a Max-Heap from the given array"""
    HEAP_SIZE = len(A)
    start_idx = (HEAP_SIZE//2) - 1
    for idx in range(start_idx, -1, -1):
        max_heapify_bottom_up(A, HEAP_SIZE, idx)
    print_heap(A)

def print_heap(A, total_width=60, fill=' '):
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    for i in range(len(A)):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(f"{i+1}: {A[i]}".center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return
    
if __name__ == "__main__":
    A = [1, 2, 3, 3, 4, 5, 6, 71, 8, 9, 10, -5]
    build_max_heap(A)
    
# OUTPUT
# anish@Anish ~ % /opt/homebrew/opt/python@3.10/bin/python3 /Users/anish/Desktop/data_science/github_study/repo/custom_data_structures/heap/max_heap.py

#                            1: 71                            
#             2: 10                          3: 6             
#       4: 8           5: 9           6: 5           7: 3     
#   8: 3   9: 2  10: 1  11: 4  12: -5
# ------------------------------------------------------------