#ex1.3 NEARLY SORTED
lst = list(map(int, input("Enter the integer/elements:").strip().split()))
print(lst)
count=0
def nearly_sorted(lst):
	res = []
	for i in lst:
		if lst[i] < lst[i-1] : 
			del lst[i]
			count+=1
	return result
if count==1 :
	print("TRUE")
else:
	print("FALSE")
print(nearly_sorted)
