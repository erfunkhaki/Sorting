def insertion_sort(num_list):

    print("INSERTION SORT")
    print(num_list)
    for x in range(1,len(num_list)):
        key = num_list[x]
        y = x-1

        while(y >= 0 and key < num_list[y]):
            previous_y = num_list[y]
            num_list[y] = key
            num_list[y+1] = previous_y
            y -= 1

        print(num_list)





num_list = [21,14,7,38,2] #diffrent examples
insertion_sort(num_list) #to run insertion sort

