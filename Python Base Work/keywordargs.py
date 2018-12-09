#def employee_old(e,age,c,dept='IT',sal):
#    name=input('Enter name of empl:')
#    print('Name of empl is ',name)
#    print('Dept id ',e)
#    print('dept is ',dept)

def employee(e,*info,c,dept='IT',sal=0):
    print(e)
    print('a; other non keyword argument',info)
emp_id=101
course = 'dbda'
employee(emp_id,course,25 ,"ADMIN",sal=15000)
    