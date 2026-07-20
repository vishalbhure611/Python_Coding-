# Q12. Given a dictionary of employee names and salaries, find the employee with the highest salary.

def highest_salary(dict):
    max_salary =0
    emp =""

    # for i in dict:
    #     if dict[i]>max_salary:
    #         max_salary= dict[i]
    #         emp=i

    for name, salary in dict.items():
        if salary > max_salary:
            max_salary = salary
            emp = name

    return emp


employee_salaries = {
    "Alice": 65000,
    "Bob": 85000,
    "Charlie": 72000
}
print(highest_salary(employee_salaries))