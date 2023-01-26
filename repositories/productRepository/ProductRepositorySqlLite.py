import uuid
from repositories import IRepository
from databases import IDatabase


class ProductRepositorySqlLite(IRepository):

    def __init__(self, database):
        self.database: IDatabase = database

    def create(self, product_name):
        sql = 'INSERT INTO products (id, product_name) VALUES (?, ?)'
        product_id = str(uuid.uuid4())
        product_id = self.database.create(sql, (product_id, product_name))
        # return Product(product_id, product_name)
        return product_id