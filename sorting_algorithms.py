from Drawing import * 
 
def bubble_sort(drawing_info, ascending=True): 
    list = drawing_info.list 
 
 
    for i in range(len(list) - 1): 
        for j in range(len(list) - 1 - i): 
            num1 = list[j] 
            num2 = list[j + 1] 
 
 
            if (num1 > num2 and ascending)  or (num1 < num2 and not ascending): 
                list[j], list[j + 1] = list[j + 1], list[j] 
                draw_list(drawing_info, {j: drawing_info.RED, j + 1: drawing_info.GREEN}, True) 
                yield True #  perform a swap and yield control to where  
                           # it was called from and wait to be called again and then perform the next step, pauses and stores current state of function, can yield anything, ex. yield 1. 
    return list 
 
 
def insertion_sort(drawing_info, ascending = True): 
    list = drawing_info.list 
 
 
    for i in range(1, len(list)): 
        current = list[i] 
         
        while True: 
            ascending_sort = i > 0 and list[i - 1] > current and ascending 
            descending_sort = i > 0 and list[i - 1] < current and not ascending 
 
            if not ascending_sort and not descending_sort: 
                break 
            list[i] = list[i - 1] 
            i = i - 1 
            list[i] = current 
            draw_list(drawing_info, {i - 1 : drawing_info.GREEN, i : drawing_info.RED}, True) 
            yield True 
 
    return list 
 
def selection_sort(drawing_info, ascending = True): 
    list = drawing_info.list 
 
 
    for i in range(len(list) - 1): 
        index = i 
 
        for j in range(i + 1, len(list), 1): 
 
            if (list[j] < list[index] and ascending) or (list[j] > list[index] and not ascending): 
                index = j 
 
        if index != i: 
            list[i], list[index] = list[index], list[i] 
            draw_list(drawing_info, {i: drawing_info.GREEN, index : drawing_info.RED}, True) 
            yield True 
 
def shell_sort(drawing_info, ascending = True): 
    list = drawing_info.list 
    n = len(list) 
    gap = n // 2 
    while (gap > 0): 
        for i in range(gap, n, 1): 
            temp = list[i] 
 
            j = i 
            while (j >= gap and list[j - gap] > temp and ascending) or  (j >= gap and list[j - gap] < temp and not ascending) : 
                list[j] = list[j - gap] 
                draw_list(drawing_info, {j: drawing_info.GREEN}, True) 
                yield True 
                j -= gap 
            list[j] = temp 
            draw_list(drawing_info, {j: drawing_info.RED}, True) 
 
        gap //= 2 
    return list 
 
def cocktain_sort(drawing_info, ascending = True): 
    list = drawing_info.list 
    swapped = True 
 
    while (swapped): 
        swapped = False 
 
        for i in range(len(list) - 1): 
            if (list[i] > list[i + 1] and ascending) or (list[i] < list[i + 1] and not ascending): 
                list[i], list[i + 1] = list[i + 1], list[i] 
                draw_list(drawing_info, {i: drawing_info.GREEN, i + 1 : drawing_info.RED}, True) 
                yield True 
 
                swapped = True 
         
        if not swapped: 
            break 
        swapped = False 
 
        for i in range(len(list) - 2, -1, -1): 
            if (list[i] > list[i + 1] and ascending) or (list[i] < list[i + 1] and not ascending): 
                list[i], list[i + 1] = list[i + 1], list[i] 
                draw_list(drawing_info, {i: drawing_info.GREEN, i + 1 : drawing_info.RED}, True) 
                yield True 
                swapped = True 
 

    return list 
