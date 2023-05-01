def diagonalDifference(arr):
    # Write your code here
    nums1 = 0
    nums2 = 0
    res = 0
    for i in range(n):
        nums1 += arr[i][i]
    
    for j in range(n):
        nums2 += arr[j][n-1-j]
    
    res = abs( nums1-nums2 )
    return res
