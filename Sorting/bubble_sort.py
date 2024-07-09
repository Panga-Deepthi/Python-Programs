def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[5,3,6,7,2,8]
sorted_array=bubbleSort(arr)
print("sorted array:",sorted_array)
