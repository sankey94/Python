import re
class Facebook_usr():
    def __init__(self):
        self.usrnm='Sanket'
        self.pwd='121212'
#    def set_details(self,usrnm,pwd):
#     
#             self.validate_password(pwd)
#        else:
#            return "Enter a username"
    
    def validate_password(self,usrnm,pwd):
        if(self.usrnm != ''):
            if re.search(r'[a-z0-9@#$%^&+=]{8,}', self.pwd):
                    if re.search(r'^[A-Z]', self.pwd):
                        return True
                    else:
                        return False

        else:
           print( "Enter a username")
        
def main():
    account = Facebook_usr()
    usrnm=input("Enter username:")
    pwd=input("Enter password:")
    #account.set_details(usrnm,pwd)
    print(account.validate_password(usrnm,pwd))
    
main()
    
        
        
        