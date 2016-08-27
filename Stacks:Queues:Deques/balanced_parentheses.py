def parCheck(symbolString):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbolStrinng) and balanced:
		symbol = symbolString[index]
		if symbol == '(':
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()
		index = index + 1
	
	if balanced and s.isEmpty():
		return True
	else:
		return False
		

