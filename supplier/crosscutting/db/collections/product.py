from supplier.crosscutting.db.collections.base_document import BaseDocument


class Product(BaseDocument):
    account_menu_id = "account_menu_id"
    product_title_id = "product_title_id"
    name = 'name'
    price = 'price'
    stock_status = 'stock_status'
