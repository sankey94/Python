import re
def email_val(email):
    m1=re.search( '^[a-z._0-9]+\@' , email)
    if m1:
        return True
    return False
def password_val(password):
    m2=re.search('[a-z1-9@#$%^&*]',password)
    m3=re.search('[A-Z]',password)
    if m2 and m3:
        return True
    return False





def main():
    print("1. Email Validation")
    print("2. Password Validation")
    ch=int(input("Enter Choice:"))
    if ch==1:
        email=input("Enter Email_id:")
        print(email_val(email))

    if ch==2:
        password=input("Enter Password:")
        print(password_val(password))
main()
