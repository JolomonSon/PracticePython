num = []
for x in range(1,11):
    if x>1:
        for xx in range(2,x):
            if x%xx == 0:
                break
        else:
            num.append(x)
print(num)
p_term = num[3]
print('The Prime Number in Third Term is:',p_term)
       
