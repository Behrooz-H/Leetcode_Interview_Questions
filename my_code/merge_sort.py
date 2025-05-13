def merge(left, right):
    l = 0
    r = 0
    result =[]
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    return result+left[l:]+right[r:]


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = (len(arr)//2)
        return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


if __name__=="__main__":
    arr = [78,2,98,3,46,90,6,2,13,50,1,37,58,4,10]
    print('BEFORE sort: {}'.format(arr))
    print('AFTER sort:', merge_sort(arr))
