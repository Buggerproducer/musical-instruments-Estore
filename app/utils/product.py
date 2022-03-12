import string
import leancloud

if __name__ == '__main__':
    leancloud.init("pPObpvTV7pQB9poQHO1NJoMP-MdYXbMMI", "pShwYQQ4JVfSStc56MvkHNrr")


def getProductFromCategory(category_id:string,skip=0,limit=10):
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




