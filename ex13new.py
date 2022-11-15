#ex1.3 NEARLY SORTED
lst = list(map(int, input("Enter the integer/elements:").strip().split()))

print(lst)
print(range(len(lst)))
def is_sorted(lst):
	is_increasing = True
	if lst[0] > lst[1]: is_increasing = False
	for i in (range(len(lst)-1)):
		if is_increasing:
			if lst[i] > lst[i+1]:
				return False
		if not is_increasing:
			if lst[i] < lst[i+1]:
				return False
	return True

def nearly_sorted(lst):
	if is_sorted(lst):
		return False
	for i in (range(len(lst))): 
		lst_copy = lst[:]
		del lst_copy[i]
		if is_sorted(lst_copy):
			return True
	return False

print(nearly_sorted(lst))
