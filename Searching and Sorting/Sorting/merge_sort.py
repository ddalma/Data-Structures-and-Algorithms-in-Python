def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr)/2
		
		left = arr[:mid]
		right = arr[mid:]
		
		merge_sort(left)
		merge_sort(right)
		
		i=0
		j=0
		k=0
		
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i +=1
			else:
				arr[k] = right[j]
				j +=1
			
			k += 1
		
		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1
		
		while j < len(right):
			arr[k] = right[j]
			j +=1
			k +=1
			
			

#Merge Sort
def merge_sort(arr, ele):
	mid = len(arr)/2
	right = arr[mid:]
	left = arr[:mid]
	
	merge_sort(right)
	merge_sort(left)
	
	i=0
	j=0
	k=0
	
	while i < len(left) and j < len(right):
		if left[i] < right[i]:
			arr[k] = left[i]
			i +=1
		else:
			arr[k] = right[j]
			j += 1
		k += 1
	
	while i < len(left):
		arr[k] = left[i]
		i += 1
		k += 1
	while j < len(right):
		arr[k] = right[j]
		j += 1
		k += 1
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		