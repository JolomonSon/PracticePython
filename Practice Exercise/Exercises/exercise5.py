#emp = ["List of Employees\n {}".format() for tuples in tuplesList for value in tuples]
#emp_mg
import time
staff_name = str(input('Enter your name here: '))
time.sleep(1)
print('Hello',staff_name,'Fill in following details\n')
def staff():
    emp1 = input('Enter rank of employee:\n>> ')
    emp2 = input('Enter employee\'s direct manager:\n>> ')
    tuplesList = [('Worker_1','Boss_1'), ('Worker_2','Boss_2'), ('Boss_1','Exec_1'),('Boss_2','Exec_2'), ('Exec_1','Director_1'), ('Exec_2','Director_2'),
    ('Director_1', 'CEO'), ('Director_2', 'CEO'), ('CEO', 'None')]
    new_tuple = {}
    for tuples in tuplesList:
        emp = tuples[0]
        emp_mg = tuples[1]
        new_tuple[emp] = emp_mg
        for dicts in new_tuple:
            continue
    if new_tuple[dicts] is dicts[key]:
        print('True')
    else:
        print('False')


staff()
    
       