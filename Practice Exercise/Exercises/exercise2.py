#PRIME NUMBERS
num = []
for x in range(1,11):
    if x > 1:
        for xx in range(2,x):
            if (x%xx == 0):
                break
        else:
            num.append(x)
print("List of Prime Numbers in 1,11")
print(num)
