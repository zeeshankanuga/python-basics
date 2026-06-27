#Input a list of Numbers from user i.e take integer inputs and append to list.
#Find the smallest and Second Smallest Numbers from that list
#eleminate repaeting numbers from the list

number=input("Enter numbers: ")
splitted_numbers=number.split(",")
list_of_numbers=list(dict.fromkeys(splitted_numbers))
print(list_of_numbers)
for i in range(len(list_of_numbers)):
    for j in range(i+1, len(list_of_numbers)):
        if int(list_of_numbers[i]) > int(list_of_numbers[j]):
            temp=list_of_numbers[i]
            list_of_numbers[i]=list_of_numbers[j]
            list_of_numbers[j]=temp
print("Smallest number is: ", list_of_numbers[0])
print("Second smallest number is :", list_of_numbers[1])