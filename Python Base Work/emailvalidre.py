import re

def validate_email(a):
    m=re.search('^[a-z._0-9]+\@[a-z]+\.[a-z]',a)
    if m:
        return True
    else:
        return False

    
a=input("Enter Email ID:")
print(validate_email(a))