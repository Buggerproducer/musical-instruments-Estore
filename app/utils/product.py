import string
import leancloud

if __name__ == '__main__':
    leancloud.init("pPObpvTV7pQB9poQHO1NJoMP-MdYXbMMI", "pShwYQQ4JVfSStc56MvkHNrr")


def getProductFromCategory(category_id:string,skip=0,limit=10):
    Category = leancloud.Object.extend('ProductCategory')
    category = Category.create_without_data(category_id)
    query = leancloud.Query('ProductCategoryMap')
    query.equal_to('category', category)
    query.limit(limit)
    query.skip(skip)
    return query.find()
