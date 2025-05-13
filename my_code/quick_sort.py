def partition(left, right, array):
    pivot, pointer = array[right], left
    for i in range(left,right):
        if array[i]<pivot:
            array[i], array[pointer]=array[pointer], array[i]
            pointer+=1
    array[pointer], array[right]= array[right], array[pointer]
    return pointer


def quick_sort(left, right, array):
    if len(array)<2:
        return array
    if left < right:
        pivot_pointer = partition(left, right, array)
        quick_sort(left, pivot_pointer-1, array)
        quick_sort(pivot_pointer+1, right, array)
    return array
if __name__=="__main__":
    arr = [78,2,98,3,46,90,6,2,13,50,1,37,58,4,10]
    print(quick_sort(0,len(arr)-1, arr))
