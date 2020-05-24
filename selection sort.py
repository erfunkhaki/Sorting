def selection_sort(num_list):

    count = 0
    
    print("SELECTION SORT")
    for x in range(len(num_list)):
        current_list = num_list[x:]
        minum = min(current_list)
        num_list.pop(num_list.index(minum))
        num_list.insert(count, minum)

        count += 1
    
        print(num_list)
    print("Final sorted list: ")
    print(num_list)
    
num_list = [21,14,7,38,2] #diffrent examples
selection_sort(num_list) #to run selection sort


