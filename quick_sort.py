def quicksort(a, l, r):
    comparisons = 0
    assignments = 0
    recursive_calls = 1
    if l < r:
        q, c1, a1 = partition(a, l, r)
        comparisons += c1
        assignments += a1
        
        c2, a2, r2 = quicksort(a, l, q)
        c3, a3, r3 = quicksort(a, q + 1, r)
        
        comparisons += c2 + c3
        assignments += a2 + a3
        recursive_calls += r2 + r3
    else:
        return 0, 0, 0
    return comparisons, assignments, recursive_calls

def partition(a, l, r):
    comparisons = 0
    assignments = 0
    pivot = a[l]
    assignments += 1
    i = l - 1
    j = r + 1
    assignments += 2
    
    while True:
        i += 1
        assignments += 1
        while a[i] < pivot:
            comparisons += 1
            i += 1
            assignments += 1
        comparisons += 1
        
        j -= 1
        assignments += 1
        while a[j] > pivot:
            comparisons += 1
            j -= 1
            assignments += 1
        comparisons += 1
        
        comparisons += 1
        if i >= j:
            return j, comparisons, assignments
            
        a[i], a[j] = a[j], a[i]
        assignments += 3

if __name__ == '__main__':
    my_list = [77, 89, 74, 68, 70, 49, 5, 62, 51]
    sorted_list = my_list.copy()
    
    print("Швидке сортування (схема Хоара)")
    total_c, total_a, total_r = quicksort(sorted_list, 0, len(sorted_list) - 1)
    
    print("Оригінальний список:", my_list)
    print("Відсортований список:", sorted_list)
    print(f"Загальна кількість порівнянь: {total_c}")
    print(f"Загальна кількість присвоєнь: {total_a}")
    print(f"Загальна кількість рекурсивних викликів: {total_r}")
