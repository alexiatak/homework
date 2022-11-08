#ex 1.14 "LISTS"
lst = list(map(int, input("Enter the integer/elements:").strip().split()))
lst.sort()
print(lst)

lstbig=[]
for i in list(lst):
    if lst(i).attr !=  lst(i-1).attr :
        print(lst.count(i))   #how many times a number is repeated
        lstsmall=[] 
        for j in range(lst.count(i)):
            lstsmall.append(i)      #we add the multiplied numbers to a smaller list
            print(lstsmall) 
       #if lstsmall(j) not in lstbig(i):
        lstbig.append(lstsmall)       #we add all the small lists to a big list
   
print(lstbig)
#res=set(lstbig)