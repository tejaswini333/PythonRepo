from oop_electric_shopping.Address import Address
from oop_electric_shopping.Account import Account
class Vendor:

    def __init__(self,regNo,name,addr,acc):
        if type(addr)==Address:
            self.venAddress=addr
        else:
            print('Invalid Address...owner cannot be created')
            return

        if type(acc) == Account:
            self.venAccount = acc
        else:
            print('Invalid Account...owner cannot be created')
            return

        self.venregNo=regNo
        self.venName=name
        self.vendorInventory=[]


    def __str__(self):
        #return f'\n{self.__dict__}'
        return '''
            ----------------------------------------------------
            Registration No : {}
            Vendor Name : {}
            Vendor Account : {} 
            Vendor Addresss : {}
            Vendor Products : {}
            --------------------------------------------------------
        '''.format(self.venregNo,self.venName,self.venAccount,self.venAddress,self.vendorInventory)


    def __repr__(self):
        return str(self)
