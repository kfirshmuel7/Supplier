from supplier.crosscutting.db.collections.base_document import BaseDocument


class SupplierMenu(BaseDocument):
    account_id = "account_id"
    created_time = 'created_time'
    currency = 'currency'
