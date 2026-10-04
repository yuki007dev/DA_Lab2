def merge_sort_iterative(a):
    n = len(a)
    comparisons = 0
    assignments = 0
    i = 1
    while i < n:
        j = 0
        while j < n - i:
            left = j
            mid = j + i
            right = min(j + 2 * i, n)
            n1 = mid - left
            n2 = right - mid
            L = a[left:mid]
            R = a[mid:right]
            assignments += n1 + n2
            it1 = 0
            it2 = 0
            k = left
            assignments += 3
            while it1 < n1 and it2 < n2:
                comparisons += 1
                if L[it1] <= R[it2]:
                    a[k] = L[it1]
                    it1 += 1
                else:
                    a[k] = R[it2]
                    it2 += 1
                k += 1
                assignments += 2
            while it1 < n1:
                a[k] = L[it1]
                it1 += 1
                k += 1
                assignments += 2
            while it2 < n2:
                a[k] = R[it2]
                it2 += 1
                k += 1
                assignments += 2
            j += 2 * i
        i *= 2
    return a, comparisons, assignments

def merge_sort_recursive(arr):
    comparisons = 0
    assignments = 0
    recursive_calls = 0
    if len(arr) <= 1:
        return arr, comparisons, assignments, recursive_calls
    
    mid = len(arr) // 2
    assignments += 1
    recursive_calls += 2
    
    left_half, c1, a1, r1 = merge_sort_recursive(arr[:mid])
    right_half, c2, a2, r2 = merge_sort_recursive(arr[mid:])
    
    comparisons += c1 + c2
    assignments += a1 + a2
    recursive_calls += r1 + r2
    
    merged_arr = []
    i = 0
    j = 0
    assignments += 2
    
    while i < len(left_half) and j < len(right_half):
        comparisons += 1
        if left_half[i] <= right_half[j]:
            merged_arr.append(left_half[i])
            i += 1
        else:
            merged_arr.append(right_half[j])
            j += 1
        assignments += 2
        
    while i < len(left_half):
        merged_arr.append(left_half[i])
        i += 1
        assignments += 2
        
    while j < len(right_half):
        merged_arr.append(right_half[j])
        j += 1
        assignments += 2
        
    return merged_arr, comparisons, assignments, recursive_calls

if __name__ == '__main__':
    my_list = [77, 89, 74, 68, 70, 49, 5, 62, 51]
    
    print("Ітеративне сортування злиттям")
    sorted_iter, c_iter, a_iter = merge_sort_iterative(my_list.copy())
    print("Оригінальний список:", my_list)
    print("Відсортований список:", sorted_iter)
    print(f"Кількість порівнянь: {c_iter}")
    print(f"Кількість присвоєнь: {a_iter}\n")

    print("Рекурсивне сортування злиттям")
    sorted_rec, c_rec, a_rec, r_rec = merge_sort_recursive(my_list.copy())
    print("Оригінальний список:", my_list)
    print("Відсортований список:", sorted_rec)
    print(f"Кількість порівнянь: {c_rec}")
    print(f"Кількість присвоєнь: {a_rec}")
    print(f"Кількість рекурсивних викликів: {r_rec}")
