def heapsort(a):
    n = len(a)
    comparisons = 0
    assignments = 0

    def swap(i, j):
        a[i], a[j] = a[j], a[i]

    def sink(i, size, trace_phase=""):
        nonlocal comparisons, assignments
        k = i
        while True:
            j = 2 * k + 1
            if j >= size:
                break
            
            if j + 1 < size:
                comparisons += 1
                if a[j + 1] > a[j]:
                    j += 1
                
            comparisons += 1
            if a[k] >= a[j]:
                if trace_phase: print(f"    {a[k]} >= {a[j]}, залишається на місці.")
                break
                
            if trace_phase: print(f"    Обмін {a[k]} та {a[j]}.")
            swap(k, j)
            assignments += 3
            k = j

    print("ФАЗА 1: Побудова максимальної купи")
    for i in range(n // 2 - 1, -1, -1):
        print(f"Занурюємо елемент з індексом {i} ({a[i]}):")
        sink(i, n, trace_phase="Phase1")
    print(f"Масив після побудови купи: {a}\n")
        
    print("ФАЗА 2: Сортування")
    for i in range(n - 1, 0, -1):
        print(f"Міняємо корінь ({a[0]}) з останнім ({a[i]}). Розмір = {i}.")
        swap(0, i)
        assignments += 3
        sink(0, i, trace_phase="Phase2")
        print(f"  Масив: {a}")
        
    return a, comparisons, assignments

if __name__ == '__main__':
    my_list = [77, 89, 74, 68, 70, 49, 5, 62, 51]
    sorted_list, comps, assigs = heapsort(my_list.copy())
    print("\nОригінальний список:", my_list)
    print("Відсортований список:", sorted_list)
    print(f"Кількість порівнянь: {comps}")
    print(f"Кількість присвоєнь: {assigs}")
