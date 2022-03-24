import string
import leancloud
from .. import models

if __name__ == '__main__':
    leancloud.init("pPObpvTV7pQB9poQHO1NJoMP-MdYXbMMI", "pShwYQQ4JVfSStc56MvkHNrr")


def getProductById(product_id: string):
    """
    use product_id to get product
    return:  a product av object
    example operation: get the product's information
    product.get('title').get('english') 获取产品英文名
    product.get('title').get('chinese') 获取产品中文名
    product.get('description').get('english') 获取产品英文描述
    product.get('description').get('chinese') 获取产品中文描述
    product.get('price').get('dollar') 获取美元价格
    product.get('price').get('CNY') 获取人民币价格
    product.get('cover').url 获取封面图片链接
    """
    Product = models.Product
    query = Product.query
    query.include('title')
    query.include('description')
    query.include('detail')
    query.include('price')
    product = query.get(product_id)
    return product


def getProductByCategory(category_id: string, skip=0, limit=10):
    """
    use category_id to get products
    return:  a list of product av object

    example operation: get the first product's information
    result[0].get('title').get('english') 获取产品英文名
    result[0].get('title').get('chinese') 获取产品中文名
    result[0].get('description').get('english') 获取产品英文描述
    result[0].get('description').get('chinese') 获取产品中文描述
    result[0].get('price').get('dollar') 获取美元价格
    result[0].get('price').get('CNY') 获取人民币价格
    result[0].get('cover').url 获取封面图片链接
    """
    Category = leancloud.Object.extend('ProductCategory')
    category = Category.create_without_data(category_id)
    query = leancloud.Query('ProductCategoryMap')
    query.equal_to('category', category)
    query.include('product')
    query.include('product.title')
    query.include('product.description')
    query.include('product.price')
    query.limit(limit)
    query.skip(skip)
    result = query.find()
    lst = []
    for i in result:
        lst += [i.get('product')]
    return lst


def getAllCategory(skip=0, limit=50):
    """
    get all category
    return: a list of categories
    example operation: get the first category information
    result[0].get('title').get('english') 获取类别英文名
    result[0].get('title').get('chinese') 获取类别中文名
    result[0].get('cover').url 获取封面图片链接
    """
    query = leancloud.Query('ProductCategory')
    query.limit(limit)
    query.skip(skip)
    query.include('title')
    query.include('img')
    result = query.find()
    return result

def getAllProduct(skip=0, limit=50):
    """
    get all product
    return: a list of products
    example operation: get the first category information
    result[0].get('title').get('english') 获取类别英文名
    result[0].get('title').get('chinese') 获取类别中文名
    result[0].get('cover').url 获取封面图片链接
    """
    query = leancloud.Query('Product')
    query.limit(limit)
    query.skip(skip)
    query.include('title')
    query.include('price')
    query.include('description')
    result = query.find()
    return result

def getCategoryById(category_id: string):
    """
    use category_id to get product
    return:  a category av object
    example operation: get the first category information
    result[0].get('title').get('english') 获取类别英文名
    result[0].get('title').get('chinese') 获取类别中文名
    result[0].get('cover').url 获取封面图片链接
    """
    Category = leancloud.Object.extend('ProductCategory')
    query = Category.query
    query.include('title')
    query.include('img')
    category = query.get(category_id)
    return category
