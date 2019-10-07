# STRETCH: implement Linear Search				
def linear_search(arr, target):
  i = 0
  for i in range(len(arr)):
    if arr[i] == target:
      print('true')
      return i
    else:
      print(f'false: {arr[i]} does not equal {target}')
      i += 1
      print(i)
  return -1
    

#def binary_search(to_find, names):
    # Cut our list in half, examine the midpoint item
    # start = 0
    # end = len(names)
    # while end - start > 0:
    #     mid = start + (end - start) // 2
    #     item = names[mid]
    #     # If the item is equal to to_find:
    #     if item == to_find:
    #         return True
    #     # Otherwise, if it's smaller
    #     elif item > to_find:
    #         end = mid - 1
    #         # Repeat binary search on first half of the list
    #     # Otherwise
    #     else:
    #         start = mid + 1
    #         # Repeat binary search on second half
    # return False
   
# STRETCH: write an iterative implementation of Binary Search 

def binary_search(arr, target):
    #Cut our list in half, examine the midpoint item
    start = 0
    end = len(arr) -1
    while start <= end:
        # length of array // 2
        mid = start + (end - 1) // 2 
        item = arr[mid]
        # If the item is equal to to_find:
        if item == target:
            return arr.index(item)
        # Otherwise, if it's smaller
        elif item > target:
           # print(item)
            end = mid - 1
            # Repeat binary search on first half of the list
        # Otherwise
        elif item < target:
            print(item)
            start = mid + 1
            # Repeat binary search on second half
    return -1
# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  

  if len(arr) == 0:
    return -1 # array empty
  
  mid = (low+high)//2
  item = arr[mid]

  if item == target:
    return item
  elif item > target:
    return binary_search_recursive(arr[:mid], target, low, high)
  else:
    return binary_search_recursive(arr[mid +1:], target, low, high)
  # TO-DO: add missing if/else statements, recursive calls
