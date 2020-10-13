WIFI="WiFi"
COLOR="COLOR"
IS_SMARTPHONE="SMART_PHONE"
INFRARED="INFRA"
CALLING="CALLING"
CAMERA="CAMERA"
BLUETOOTH="BLUETOOTH"



class Mobile:

    def __init__(self,mid,model,price,ven,qty,features=None):
        self.mobileId = mid
        self.mobileModel =model
        self.mobilePrice=price
        self.mobileVendor=ven
        self.mobileQty=qty
        if type(features)==dict:
            self.mobileFeatures=features
        else:
            print('Invalid feature types.. so not added..!')
            self.mobileFeatures={
                    BLUETOOTH:False,
                    CAMERA : ["8Mpx","16mpx"],
                    CALLING : True,
                    INFRARED:False,
                    COLOR : "BLACK",
                    WIFI:True,
                    IS_SMARTPHONE:False
                    }

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return self.mobileModel.__hash__()

    def __eq__(self, other):
        return self.mobileModel==other.mobileModel

