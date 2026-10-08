def heapsort(a):
    n = len(a)
    comparisons = 0
    assignments = 0

    def swap(i, j):
        a[i], a[j] = a[j], a[i]

    def sink(i, size):
        nonlocal comparisons, assignments
        k = i
        while True:
            j = 2 * k + 1
            if j >= size:
                break
            
            comparisons += 1
            if j + 1 < size and a[j + 1] > a[j]:
                j += 1
                
            comparisons += 1
            if a[k] >= a[j]:
                break
                
            swap(k, j)
            assignments += 3
            k = j

    # Фаза 1: Побудова максимальної купи
    for i in range(n // 2 - 1, -1, -1):
        sink(i, n)
        
    # Фаза 2: Сортування
    for i in range(n - 1, 0, -1):
        swap(0, i)
        assignments += 3
        sink(0, i)
        
    return a, comparisons, assignments

if __name__ == '__main__':
    my_list = [77, 89, 74, 68, 70, 49, 5, 62, 51]
    sorted_list, comps, assigs = heapsort(my_list.copy())
    print("Оригінальний список:", my_list)
    print("Відсортований список:", sorted_list)
    print(f"Кількість порівнянь: {comps}")
    print(f"Кількість присвоєнь: {assigs}")
