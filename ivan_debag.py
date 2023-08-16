def predict_salary(min_salary, max_salary):
    average_salary = 0
    if min_salary == (None or 0):
        average_salary =  max_salary*0.8 
        print('if 1')
    if max_salary == (None or 0):
        average_salary =  min_salary*1.2
        print('if 2')
    if (min_salary and max_salary) != (None or 0):
        average_salary = ((max_salary+min_salary)/2) 
        print('if 3')      
    return average_salary

print(f'Result: {predict_salary(150, 170)}')
print(f'Result: {predict_salary(0, 100)}')
print(f'Result: {predict_salary(100, 0)}')
