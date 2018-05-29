from datetime import datetime
from pony.orm import Database, Required, Optional, Set, PrimaryKey

db = Database()

class Product(db.Entity):
    """Товар"""
    title = Required(str)
    unit = Required(str)
    price = Required(float)
    description = Optional(str)
    category = Required('Category')
    #alt_categories = Set(list('Category'))
    amount = int # количество товара
    history = Set('ProductHistory')
    cartitem = Set('CartItem')
    orderitem = Set('OrderItem')

class ProductHistory(db.Entity):
    """История конкреного товара"""
    product = Required('Product')
    created = Required(datetime, default=datetime.now)
    price = Required(float)


class Category(db.Entity):
    """Категория товара"""
    title = Required(str)
    parent = Required('Category')
    products = Set(Product)
    categorys = Set('Category')


class Customer(db.Entity):
    """Покупатель"""
    email = Required(str)
    phone = Required(str)
    name = Required(str)
    address = Set('Address')
    cart = Set('Cart')
    order = Set('Order')


class Address(db.Entity):
    """Адрес"""
    customer = Required('Customer')
    country = Required(str)
    city = Required(str)
    street = Required(str)
    zip_code = Required(str)
    house = Required(int)


class Cart(db.Entity):
    """Корзина с товарами"""
    customer = Required('Customer') or None
    products = Set('CartItem')
    #cart = Set('CartItem')        # ?    #########
    #cartitem = Set('CartItem')     # ?   #######


class CartItem(db.Entity):
    """Элемент корзины"""
    cart = Required('Cart')
    product = Required('Product')
    amount = Required(int) # 1 единица товара

class Order(db.Entity):
    """Заказ"""
    customer = Required('Customer')
    created = Required(datetime, default=datetime.now)
    products = Set('OrderItem')  ## ?    ##########
    status = Required('Status')
    cost = Required(float)
    #orderitem = Set('OrderItem')

class Status(db.Entity):
    """Любой статус"""
    name = Required(str)
    order = Set('Order')


class OrderItem(db.Entity):
    """Товар (одна позиция) в заказе"""
    order = Required('Order')
    product = Required('Product')
    amount = Required(int) # 1 единица товара


class Menu(db.Entity):
    """Меню"""
    pass





db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

