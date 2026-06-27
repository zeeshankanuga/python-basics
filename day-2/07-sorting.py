list_of_numbers=[1,3,5,6,7,9,10,22,45,67,43,-3,-6,-10]

for i in range(len(list_of_numbers)):
    for j in range(len(list_of_numbers)):
        if list_of_numbers[i] < list_of_numbers[j]:
           temp=list_of_numbers[i]
           list_of_numbers[i]=list_of_numbers[j]
           list_of_numbers[j]=temp

print(list_of_numbers)