from oop_electric_shopping.Order import Order
from oop_electric_shopping.Account import Account
from oop_electric_shopping.Customer import Customer
from oop_electric_shopping.Product import Product
from oop_electric_shopping.Vendor import Vendor
from oop_electric_shopping.Address import Address

def generate_customer_info():
    custacc2 = Account(50000.2)
    ad2 = Address(aid=22333, city="Pune-Pimpari", state='MH', pin=292922)
    cust = Customer(cid='C19293', cnm='ABCD', caddress=ad2, account=custacc2)
    return cust

def generate_owner_info():
    venacc1 = Account(100000.5, 'Current')

    ad1 = Address(aid=111222, city="Pune-Chinchwad", state='MH', pin=342922)

    p1 = Product(pid=111, pnm='Mobile', pcat='E', pqty=3, pprice=15252.3)
    p2 = Product(pid=121, pnm='TV', pcat='A', pqty=13, pprice=55252.3)
    p3 = Product(pid=14541, pnm='Remote', pcat='B', pqty=3, pprice=1252.3)
    p4 = Product(pid=411, pnm='Laptop', pcat='C', pqty=43, pprice=85252.3)
    p5 = Product(pid=1151, pnm='Charger', pcat='Q', pqty=10, pprice=9252.3)
    listOfProducts = [p1, p2, p3, p4, p5]
    balajimart = Vendor(regNo="R1922", name='Balaji Mart', addr=ad1, acc=venacc1)
    balajimart.vendorInventory = listOfProducts
    return balajimart
