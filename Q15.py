# Q15. Given a list of employee records (Name, Department), group employees by department using a dictionary.

def group_by_department(employees):
    result ={}

    for name,dept in employees:
        if dept not in result:
            result[dept] =[]
        
        result[dept].append(name)
        
    return result


employees = [
    ("Rahul", "IT"),
    ("Amit", "HR"),
    ("Neha", "IT"),
    ("Priya", "Finance"),
    ("Ravi", "HR")
]

print(group_by_department(employees))