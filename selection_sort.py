def selection_sort(data):
    for scan_index in range(len(data)):
        min_index = scan_index

        for comp_index in range(scan_index + 1, len(data)):
            if data[comp_index] < data[min_index]:
                min_index = comp_index
        
        if min_index != scan_index:
            data[scan_index], data[min_index] = data[min_index], data[scan_index]
            print(data)

selection_sort(data=[9, 5, 7, 4, 2, 8, 1, 10, 6, 3])
