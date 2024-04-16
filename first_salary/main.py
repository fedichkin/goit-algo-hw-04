def total_salary(path):
    sum_of_salary = 0
    avg_salary = 0

    try:
        with open(path, 'r') as file:
            lines = [el.strip() for el in file.readlines()]
    except FileNotFoundError:
        print('File is not found')
    
    try:
        for line in lines:
            _, salary = line.split(',')
            sum_of_salary += int(salary)
        
        avg_salary = int(sum_of_salary / len(lines))
    except ValueError:
        print('Type of salary is wrong')
    except ZeroDivisionError:
        print('There is not data in the file')

    return sum_of_salary, avg_salary
    
        


print(total_salary('./data.txt'))
