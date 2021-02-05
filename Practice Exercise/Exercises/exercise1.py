#Excercise 1
  #Sum_of_Squares
num = []
new_num = []
for x in range(11):
    num.append(x)
    #Finding the sum of square 
#Finding Square
    num_sqr = (num[x]**2)
  #print(num_sqr)
  #Finding Sum of Squares
#Finding Sum
    new_num.append(num_sqr)
    sum_of_sqr = sum(new_num)
#print("The sum of square is: ",sum_of_sqr)
    #Finding the Square of sum
#Finding Summ(sum)
    summ = sum(num)
#print(summ)
  #Finding Square of sum
#Finding Square
    sqr_of_sum = summ**2
#print("The Square of Sum is: ",sqr_of_sum)
    sqr_sum = sqr_of_sum - sum_of_sqr
print("The Square of Sum - Sum of Squares in range 1 to 10 is:")
print(sqr_sum)


 