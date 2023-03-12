#быстрая сортировка.
def quick_sort(array):
    if len(array) <= 1:
        return array 
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater) #[] список

print(quick_sort([14, 5, 6, 9, 12]))


# сортировка слияния

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        
lst_1 = [1, 5, 6, 2, 12,12,14, 14, 11, 3]
merge_sort(lst_1)
print(lst_1)

