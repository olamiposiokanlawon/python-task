

def mergeLists(list1, list2):
    mergedList = list1 + list2
    return mergedList

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(mergeLists(list1, list2))

def secondLargest(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[-2]

print(secondLargest([10, 10, 9]))
