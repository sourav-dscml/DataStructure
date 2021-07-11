def BinarySearch(lst, num_to_find):
    left_ind = 0
    right_ind = len(lst)-1
    mid_ind = 0

    while left_ind<=right_ind:
        mid_ind = (left_ind + right_ind)//2
        mid_val = lst[mid_ind]

        if mid_val==num_to_find:
            return mid_ind
        if mid_val < num_to_find:
            left_ind = mid_ind+1
        else:
            right_ind = mid_ind-1


    return -1

def binarysearch_recursive(lst,num_find,left_ind,right_ind):
    left_ind = left_ind
    right_ind = right_ind
    mid_ind = 0


    mid_ind = (left_ind + right_ind)//2
    mid_val = lst[mid_ind]
    if mid_val==num_find:
        return mid_ind
    if mid_val < num_find:
        left_ind = mid_ind+1
        
    else:
        right_ind = mid_ind-1

    return binarysearch_recursive(lst,num_find,left_ind,right_ind)

def multiple_ind(lst, num_to_find,left_ind,right_ind):
    left_ind=left_ind
    right_ind=right_ind
    ind = BinarySearch(lst, num_to_find)
    indicies = []
    indicies.append(ind)
    i = ind-1

    #left search
    while i >=0:
        if lst[i]==num_to_find:
            indicies.append(i)
        else:
            break
        i = i-1

    i = ind+1
    while i<len(lst):
        if lst[i]==num_to_find:
            indicies.append(i)
        else:
            break
        i = i+1
    return indicies


if __name__ == '__main__':
    numbers_list = [1,4,6,9,15,15,15,15,17,21,34,35,56]
    number_to_find = 15
    print(BinarySearch(numbers_list,number_to_find))
    print(binarysearch_recursive(numbers_list,number_to_find,0,len(numbers_list)-1))
    print(multiple_ind(numbers_list,number_to_find,0,len(numbers_list)-1))
        
