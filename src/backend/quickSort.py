def quickSort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # escolhe o pivô (meio)
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quickSort(left) + middle + quickSort(right)
