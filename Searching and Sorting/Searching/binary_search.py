#Binary Search- Iteratively

def bin_search(arr, ele):
	first = 0
	last = len(arr) - 1
	found = False
	while first <= last and not found:
		mid = (first + last)/2
		if arr[mid] == ele:
			found = True
		else:
			if arr[mid] > ele:
				last = mid - 1
			else:
				first = mid + 1
	return found
	

#Binary Search - Recursively

def recur_bin_search(arr, ele):
	if len(arr) == 0:
		return False
	else:
		mid = len(arr)/2
		if arr[mid] == ele:
			found = True
		else:
			if arr[mid] > ele:
				return recur_bin_search(arr[:mid], ele)
			else:
				return recur_bin_search(arr[mid + 1:], ele)

def recur_bin_search(arr, ele):
	if len(arr) == 0:
		return False
	else:
		mid = len(arr)/2
		if arr[mid] == ele:
			found = True
		else:
			if arr[mid] > ele:
				return recur_bin_search(arr[:mid], ele)
			else:
				return recur_bin_search(arr[mid+1:], ele)
