n = int(input())
arr = [
    0,
    1
]
s = ""
if n > 0 and n < 46:
    for i in range(2,n):
        arr.insert(i, arr[i-1]+arr[i-2])
    for j in range(len(arr)):
        if j == len(arr)-1:
            s+= "{}".format(arr[j])
        else:
            s+= "{} ".format(arr[j])
    
print(s)