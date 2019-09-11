
    if len(arr) > 1: #if array has more than one element
        mid = len(arr)//2 #Find the middle point of the array
        ## understanding slicing with : in arrays
        # a[start:stop]   items start through stop-1
        # a[start:]       items start through the rest of the array
        # a[:stop]        items from the beginning through stop-1
        # a[:]            a copy of the whole array
        left = arr[:mid] # : is the array slice method, so slice everything from the left half
        right = arr[mid:] # slice everything from right side
  
        merge_sort(left) # Returns the left half
        merge_sort(right) # Returns the right half
  
        i = 0 #left array variable
        j = 0 #right array variable
        k = 0 #temp variable for reassigning new array values in the main array passed in

        while i < len(left) and j < len(right): ## while the arrays have items in them, compare
            if left[i] < right[j]: ## if the left array element is < than the right side
                arr[k] = left[i] ## set temp variable to == the lesser (left side)
                i+=1 ## go to the next index in the left side since it's been used
            else: 
                arr[k] = right[j] ## if left is > right, then set the temp variable to == lesser (right side)
                j+=1 ## go to the next index in the right side since it's been used
            k+=1 # set k to next index

         
        #If any elements are left in the left array (if element remains)
        while i < len(left): ## if current index is less than the length, there are still elements in array
            arr[k] = left[i] # if it is there, reassign the temp variable to the lesser left
            i+=1 # go to the next index on the left side
            k+=1 # go to the next index on the right side

        #if any elements are left in the right array
        while j < len(right): # same as above
            arr[k] = right[j] #if any remain, reassign the temp variable to the lesser right
            j+=1
            k+=1