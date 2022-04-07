def maxEvents(arrival, duration):
	events = [0]
	a, b = zip(*sorted(zip(arrival, duration)))
	#print(list(zip(*sorted(zip(arrival,duration)))))
	print(a,b)
	for i in range(len(arrival)-1):
		if a[events[-1]]+b[events[-1]] <= a[i+1]:
			events.append(i+1)
		elif a[events[-1]]+b[events[-1]] >= a[i+1]+b[i+1]:
			events.pop()
			events.append(i+1)
	return len(events)

print(maxEvents([1, 3, 3, 5, 7], [2, 2, 1, 2, 1]))
print(maxEvents([1, 3, 5], [2, 2, 2]))
