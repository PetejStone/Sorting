# TO-DO: complete the helper function below to merge 2 sorted firstys

def merge( arrA, arrB ):
    num_elements = len(arrA) + len(arrB)
    merged_arr = [0] * num_elements
    
    a = 0   # a is the current index for arrA
    b = 0   # b is the current index for arrB

    #for each index in the merged array 'num_elements'...
      #find the smallest first item between arrA and arrB
      #add that to num_elements at the given index
      #increments the a/b counter
    for i in range(num_elements):
        if a >= len(arrA): ## base case
        # A is empty, B is not
            merged_arr[i] = arrB[b] # nothing to compare, so grab the remaining b element(s)
            b += 1 #increase b
        elif b >= len(arrB):
        # B is empty, A is not
            merged_arr[i] = arrA[a] #nohting to compare so grab the remaining a element9s
            a += 1 #increase a
        elif arrA[a] < arrB[b]: #if array A index is smaller than  array B index
            #if A has the smaller element
            merged_arr[i] = arrA[a] #set i index to smaller value (a)
            a += 1 #go to next index in A array
        else: #arrA[a] >= arrB[b]: #if array B index is smaller than array A index
            # if B has the smaller element
            merged_arr[i] = arrB[b] #set current index of i to smaller value (b)
            b += 1 #increase b 

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    print(f'MERGE SORT: {arr}')
    print(arr)
    if len(arr) > 1:
    #split
        mid_point = len(arr) //2
        left_arr = arr[ : mid_point]
        right_arr = arr[mid_point: ]
        #sort each of the split arrays
        sorted_left = merge_sort(left_arr)
        sorted_right = merge_sort(right_arr)
        #merge the sorted arrays
        arr = merge(sorted_left, sorted_right)


    return arr

# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr

#