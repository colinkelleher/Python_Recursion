
'''
QUESTION 2

2. BinarySearchR(l )
Write a recursive version of the binary search algorithm that accepts a list.
A template of the iterative version has been provided on Moodle.
You can hardcode the list and the search term as in this template.
Test with several inputs. Refer to the class notes to see how this search algorithm works.
Assume the midpoint floors the value i.e. if a midpoint could be position 4 or 5, the lower value (4) is chosen.
'''
import math
def BinarySearchR(list, search_num):
    if len(list) == 0:
        return "This number is not in the list"
    else:
        mid = math.floor(len(list)//2)
        if (search_num == list[mid]):
            return "This number is in the list"
        else:
            if search_num > list[mid]:
                return BinarySearchR(list[mid+1:6],search_num)
            else:
                return BinarySearchR(list[0:mid],search_num)
list = [2,3,5,7,8,10]
x = int(input("Enter a number to check if it is in the list >>>"))
print(BinarySearchR(list,x))
