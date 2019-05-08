def mergesort(arr, left, right){
    if left < right:
        mid = (left + right) // 2
        mergesort(arr, left, mid)
        mergesort(arr, mid+1, right)
        merge(arr, left, mid, right)
}

from random import randrange

arr = [randrange(1, 100) for _ in range(20)]
# arr = sorted(arr)
print(arr)

