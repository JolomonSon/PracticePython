num = 10
numb = []
for x in range(1,num):
    if x>1:
        for xx in range(2,x):
            if (x%xx == 0):
                break
        else:
            numb.append(x)
#print(numb)
numb_sum = sum(numb)
print("Sum of List is:",numb_sum)