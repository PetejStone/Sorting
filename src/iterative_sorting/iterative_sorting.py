# # TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i  
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
    
        #Another loop (n2) -- loop through array and if the current index > then any of the items, set the cur index to that item
        #Loop through i + 1 -- the next item through the length of the array
        for j in range(i+1, len(arr)):
            if arr[cur_index] > arr[j]:
                cur_index = j
                    
        # SWAP 
        ###swap example
        #####        > <
        ## swap [ 1,2,4,3,5 ]
        ## inside loop found that 4 is > 3, so new cur_index is 3 (3)
        ### temp = arr[2] (4) - the current position, so temp value is 4
        #### arr[2] == arr[3] -- so 4 is now = 3 -> [1,2,3,3,5]
        ###### arr[cur_index] = temp  aka (arr[3]) == arr[2] -> [1,2,3,4,5]

        ####
        temp = arr[i] #temp variable is == the current position in the outside loop
    
        arr[i] = arr[cur_index] #current position of outside loop is set equal to the new current index from the inside loop
       
        arr[cur_index] = temp #current index is set equal to the temp variable



    return arr



# # TO-DO:  implement the Bubble Sort function below
# def bubble_sort( arr ):
#     for i in range(len(arr)-1,0,-1): # reverses the list from top to bottom
#         for j in range(i): #only check in the range of the current index
#             if arr[j] > arr[j+1]: #if current index is greater than the next index
#                 temp = arr[j]  ##swap
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp
    
#     return arr

def bubble_sort( arr ):
    for i in range(len(arr)): 
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
        

# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr