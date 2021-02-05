name = input('Enter your name please \n>>')
print("enter your age please if your'e eligible to vote")
age = int(input())
if age >= 18:
    print("You are eligible to vote")
elif age < 18:
    print("You are not eligible to vote")
