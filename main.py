from databases.sql_lite import SqlLiteDatabase
from repositories.productRepository import ProductRepositorySqlLite
from controllers import ProductController

sqlLiteDatabase = SqlLiteDatabase()
productRepository = ProductRepositorySqlLite(sqlLiteDatabase)
productController = ProductController(productRepository)

product = productController.create_product("product 1")
print("product", product)
