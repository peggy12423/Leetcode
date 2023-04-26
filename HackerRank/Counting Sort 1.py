def countingSort(arr):
    # Write your code here
    element = []
    for i in range(100):
        element.append(0)
    
    for j in range(n):
        element[arr[j]] += 1    
    return element
