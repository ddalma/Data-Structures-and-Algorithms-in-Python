#Sequential Search - unordered List
def seq_search(arr, ele):
	pos = 0
	found = False
	while pos < len(arr) and not found:
		if arr[pos] == ele:
			found = True
		else:
			pos += 1
	return found
	

#Sequential Search - ordered List
def ordered_seq_search(arr, ele):
	pos = 0
	found = False
	stopped= False
	while pos < len(arr) and not found:
		if arr[pos] == ele:
			found = True
		else:
			if arr[pos] > ele:
				stopped = True
			else:
				pos += 1
	return found


	