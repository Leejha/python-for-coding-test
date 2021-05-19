N = int(input())

horror = list(map(int, input().split()))

horror.sort() 

count = 0 
sum = 0

for hor in horror : 
	count += 1
	if count >= hor :
		count = 0
		sum += 1
		

print(sum)
