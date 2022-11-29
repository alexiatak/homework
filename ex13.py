#ex1.3 NEARLY SORTED
lst = list(map(int, input("Enter the integer/elements:").strip().split()))
print(lst)

def nearly_sorted(lst,ccount):
	
	for i in (range(len(lst)-1)):
		if lst[i+1] < lst[i] :
			ccount+=1
	return ccount

res=nearly_sorted(lst,0)

if res==1 :
	print("TRUE")		
else:
	print("FALSE")
