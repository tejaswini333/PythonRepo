'''from oop_electric_shopping.Application_Data import *
from oop_electric_shopping.ShoppingService import ServiceImpl
from oop_electric_shopping.Application_Data import *'''

Admin_pass=['111','222','333','444','555']

class User:

    def _init_(self,cid,cnm,caddress,username,isadmin):
        self.customerId=cid
        self.customerName=cnm
        self.customerAddress=caddress
        self.customerUsername=username
        self.isadmin=isadmin
        self.purchasedProducts=set()

    def _str_(self):

        return '''
            Cust Id : {}
            Cust Name: {}
            Cust Address : {}
            Cust Username : {}
            Cust Isadmin : {}
            Cust Products : {}
        '''.format(self.customerId,self.customerName,self.customerAddress,self.customerUsername,self.isadmin,self.purchasedProducts)
    def _repr_(self):
        return str(self)

    @classmethod
    def create_user(cls,cid,cnm,caddress,account,isadmin):
        if isadmin.upper()=='Y':
            verify=input('Enter password provided for admin User if not admin enter normal pass')
            if verify in Admin_pass:
                User(cid,cnm,caddress,account,isadmin)
                print('Admin User created sucessflly')
            else:
                isadmin='N'
                User(cid, cnm, caddress, account, isadmin)
                print('N User created sucessflly')
        else:
            User(cid, cnm, caddress, account, isadmin)
            print('User created sucessflly')

'''
if __name__ == '_main_':
    u1=User.create_user(1,'Teju','pune','Teju','N')
'''