# Visualisation at: https://www.cs.usfca.edu/~galles/visualization/Search.html
def binary_search_iter(target_list, target):
    """Iterative binary search: return index or -1 if not found."""

    # set low pointer to start of array
    # set high_marker pointer to end of array
    low_marker, high_marker = 0, len(target_list) - 1  
    # while the markers are in the right order
    while low_marker <= high_marker:    
        # get the mid point 
        mid_point = (low_marker + high_marker) // 2     
        if target_list[mid_point] == target:    
            return mid_point      
        # if mid point is smaller than the target   
        if target_list[mid_point] < target: 
            # move low_marker right (search right half)      
            low_marker = mid_point + 1                     
        # if mid point is larger than the target  
        else:         
            # move high_marker pointer left (search left half)            
            high_marker = mid_point - 1        


    return -1              


def binary_search_rec(target_list, target, low_marker=0, high_marker=None):
    """Recursive binary search: return index or -1 if not found."""
    # if high_marker bound not set, set it to the end of the array.
    if high_marker is None: 
        # set high_marker to end of array                # if high_marker bound not provided
        high_marker = len(target_list) - 1 
    # shount happen so indicates not found           
    if low_marker > high_marker:               
        return -1
    # compute mid_pointdle index
    mid_point = (low_marker + high_marker) // 2  
    #found target at mid_point       
    if target_list[mid_point] == target:          
        return mid_point
    # if mid_point is too large
    if target_list[mid_point] < target:          
        # recurse on right half
        return binary_search_rec(target_list, target, mid_point + 1, high_marker)
    # otherwise mid_point is too large
    else:                   
        # recurse on left half
        return binary_search_rec(target_list, target, low_marker, mid_point - 1)


target_collection = [1, 4, 7, 9, 12, 15, 20]  # sorted input required for binary search
print(binary_search_iter(target_collection, 12))  # expect 4 (index of 12)
print(binary_search_rec(target_collection, 5))    # expect -1 (not present)