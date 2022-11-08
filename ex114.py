#ex 1.14 "LISTS"
lst = list(map(int, input("Enter the integer/elements:").strip().split()))
print(lst)
def list_split(lst):
    res = []
    for i in lst:
        lstsmall = [i for k in range(lst.count(i))]
        if lstsmall not in res:
            res.append(lstsmall)
    return res


print(list_split(lst))
