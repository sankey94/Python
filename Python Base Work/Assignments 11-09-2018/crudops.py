import sys
def get_details():
    s=[]
    s.append(input('Enter name:'))
    s.append(input('Enter age:'))
    return s
def add_stud_info(stud_info):
    prn=int(input('Enter PRN:'))
    s=get_details()
    stud_info[prn] = s
def update_stud_info(stud_info):
    s1=int(input('who in studinfo:'))
    s=get_details()
    if s1 in stud_info:
        stud_info[s1] = s#.update(s)
        print(s1,'updated successfully')
def delete_stud_info(stud_info):
    who=int(input('who in studinfo:'))
    if who in stud_info:
        del stud_info[who]
        print(who,'deleted successfully')
        
def display_stud_info(stud_info):
    print(stud_info)

def dump_stud_info(stud_info):
    data=str(stud_info)
    with open(r'/home/student/stud-db.csv','w') as file:
        file.write(data)
   

stud_info={}
while True:
    print('1.Add Student')
    print('2.Update Student')
    print('3.Remove Student')    
    print('4.Display Student')
    print('5.Export Student Data')
    option= int(input('Enter the option [1-6]:'))
    if option == 1:
        add_stud_info(stud_info)
    elif option == 2:
        update_stud_info(stud_info)
    elif option == 3:
        delete_stud_info(stud_info)
    elif option == 4:
        display_stud_info(stud_info)
    elif option == 5:
        dump_stud_info(stud_info)
    else:
        sys.exit('Done. Exitting..')
        
        
