def insertion_sort(arr):
	for i in range(1, len(arr)):
		
		#set current values and position
		currentvalue = arr[i]
		position = i
		
		#Sorted Sublist
		while position > 0 and arr[position-1] > currentvalue:
			arr[position] = arr[position-1]
			position = position - 1
		
		arr[position] = currentvalue


