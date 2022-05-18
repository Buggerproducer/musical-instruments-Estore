import leancloud


def getOrderByUser(user_id, limit=10, skip=0):
    User = leancloud.Object.extend('_User')
    user = User.create_without_data(user_id)
    query = leancloud.Query('Order')
    query.equal_to('user', user)
    query.include('product')
    query.include('product.title')
    query.include('product.description')
    query.include('product.price')
    query.include('price')
    query.limit(limit)
    query.skip(skip)
    result = query.find()
    # lst = []
    # for i in result:
    #     lst += [i.get('product')]
    return result


def getCollectionByUser(user_id, limit=10, skip=0):
    User = leancloud.Object.extend('_User')
    user = User.create_without_data(user_id)
    query = leancloud.Query('CollectionMap')
    query.equal_to('user', user)
    query.include('product')
    query.include('product.title')
    query.include('product.description')
    query.include('product.price')
    query.limit(limit)
    query.skip(skip)
    result = query.find()
    # lst = []
    # for i in result:
    #     lst += [i.get('product')]
    return result


def getAllOrder(skip, limit):
    query = leancloud.Query('Order')
    query.limit(limit)
    query.skip(skip)
    query.include('product')
    query.include('user')
    query.include('price')
    query.include('product.title')
    query.include('product.description')
    result = query.find()
    return result
