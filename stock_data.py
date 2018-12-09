
''''
try:
    with open('/home/student/Desktop/NSE-INFY.csv', 'r') as infy:
        #print(infy.readlines()[1:10])
        close = []
        for line in infy:
            closing_price = line.split(',')[5]
            if closing_price == 'Close':
                continue
            close.append(float(closing_price))
        print(close)
        print(sum(close)/ len (close))
except IOError as err:
    print('File not Foud---> ',err)

'''


try:
    with open('/home/student/Desktop/NSE-INFY.csv', 'r') as infy:
        #print(infy.readlines()[1:10])
        close = []
        for line in infy:
            closing_price = line.split(',')[0]
            if closing_price == 'Close':
                continue
            close.append(float(closing_price))
        print(close)
        print(sum(close)/ len (close))
except IOError as err:
    print('File not Foud---> ',err)