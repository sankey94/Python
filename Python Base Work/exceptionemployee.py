lst=[]
try:
    path=input("Enter valid Path with valid file name:")
    lines=[]
    with open(path,'r') as h:
        for line in h:
            line = line.split(',')[3]
            lines.append(int(line))
        avg=sum(lines)/len(lines)
        print(avg)
except FileNotFoundError as e:
    print("File not found")
    try:
        path=input("Enter valid Path with valid file name:")
        lines=[]
        with open(path,'r') as h:
            for line in h:
                line = line.split(',')[3]
                lines.append(int(line))
            avg=sum(lines)/len(lines)
            print(avg)
    except FileNotFoundError as e:
         print(e)
#/home/student/employeeinfo.txt
         
#path=input("Enter valid Path with valid file name:")
#lines=[]
#with open(path,'r') as h:
#    for line in h: 
#        line = line.split(',')[3]
#        lines.append(int(line))
#    avg=sum(lines)/len(lines)
#    print(avg)
    
#        avg=sum(lst)/len(lst)
#        print(avg)
        

#    lst=[]
#    line=h.read()
#    for str in line:
#        lst.append(str.split(','))
#        print(lst)
