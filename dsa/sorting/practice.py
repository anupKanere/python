def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_indx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_indx]:
                min_indx = j
        arr[i], arr[min_indx] = arr[min_indx], arr[i]
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            break
    return arr


def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1 , n-1):
        key = arr[i]
        j = i-1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def main():
    arr = [7, 3, 5, 1, 9]

    selection = selection_sort(arr)
    bubble = bubble_sort(arr)
    insertion = insertion_sort(arr)

    print(f"Selection Sort = {selection}")
    print(f"Bubble Sort = {bubble}")
    print(f"Insertion sort : {insertion}")


if __name__ == "__main__":
    main()
