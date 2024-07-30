from supplier.crosscutting.db.collections.base_document import BaseDocument


class Accounts(BaseDocument):
    nickname = 'nickname'
    title = 'title'
    deleted = 'deleted'
    deletion_date = 'deletion_date'
    created_time = 'created_time'
    enable = 'enable'
