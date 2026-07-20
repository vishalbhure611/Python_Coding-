# Q19. Sort a list of employee records based on salary using a lambda function.
def sort_emp_using_sorted(employees):
    result = sorted(employees,key=lambda x:x[2],reverse=True)   #sorted gives new list
    return result

employees = [
    ("Rahul", "IT", 50000),
    ("Amit", "HR", 75000),
    ("Neha", "Finance", 60000),
    ("Priya", "IT", 90000)
]

print(sort_emp_using_sorted(employees))

def sort_emp_using_sort(employees):
    employees.sort(key=lambda x: x[2], reverse=True)
    return employees   #sort doesn,t give new list ,it modifies original

print(sort_emp_using_sort(employees))