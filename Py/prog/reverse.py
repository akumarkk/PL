def reverse(s1):
    lst = list(s1)
    lst.reverse()
    arr = ''.join(lst).split()
    print(arr)
    print("hello")
    ret = ""
    for i in range(len(arr)) :
        lst = list(arr[i])
        lst.reverse()
        ret += " " + ''.join(lst)
    return ret

print(reverse("hello welcome")) 

