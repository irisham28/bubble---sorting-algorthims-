#pythonsort algorithm function
numbers = [4,2,6,8,9,3,5,7,8]
#numbers.sort() #ascending order
#print(numbers)

#descending order
#numbers.sort(reverse=True)
#print(numbers)

#Bubble sort
# i is the first number, j is ths second number. then it moves on to the next pair
for i in range(0,len(numbers)):
    for j in range(i,len(numbers)):
        if numbers[i]>numbers[j]:
            numbers[i], numbers[j] = numbers[j],numbers[i]

print(numbers)

#time complexity = (o)n^2
#(o)n^2 = worst case
#worst case = list is in reverse order
 
#(o)n = average case 
#average case = mixed up order 

#best case (o)1
#best case = already sorted 
