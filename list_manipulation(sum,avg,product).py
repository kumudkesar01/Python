#sum,average, product
inputs=input("Enter the integers seperated by commas ")
try:
    lst=[int(x) for x in inputs.split(",")]
    print("The list generated is: ",lst)
except ValueError:
    print("ERROR!!! \nEnter integer values seperated by commas only")

sum_inputs= sum(lst)
print("Sum of Input sequence is = ",sum_inputs)

product = 1
for i in lst:
    product *= i
print("Product of Input sequence is = ",product)

avg = sum_inputs/len(lst)
print("The Average of Input sequence is = ",int(avg))
