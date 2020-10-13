import unittest
from oop_electric_shopping.Address import *

class TestAdrInfo(unittest.TestCase):

    def setUp(self):
        self.adrList = []
        for item in range(1, 5):
            adr = Address(aid=22333+item, city="Pune-Pimpari", state='MH', pin=292922)
            self.adrList.append(adr)


    def test_adr_gen(self):
        self.assertEqual(len(self.adrList), 4)

def main():
    unittest.main()

if __name__ == "_main_":
    main()


'''import unittest

from oop_electric_shopping.ShoppingService import ServiceImpl
from oop_electric_shopping.application_data import *

class TestProductPurchase(unittest.TestCase):

    def setUp(self):
        self.service = ServiceImpl()
        self.owner = generate_owner_info()
        self.cust = generate_customer_info()

    def test_product_purchase(self):
        self.assertEqual(self.service.purchase_product('Remote','B',3,self.owner,self.cust),'Order placed Successfully...')


if __name__ == '_main_':
    unittest.main()'''
'''

import unittest

from oop_electric_shopping.ShoppingService import ServiceImpl
from oop_electric_shopping.application_data import *

class TestOwnerInfo(unittest.TestCase):

    def setUp(self):
        pass

    def test_owner_info(self):
        self.assertEqual(self.generate_owner_info(), 'Owner created successful')


if __name__ == '_main_':
    unittest.main()'''

