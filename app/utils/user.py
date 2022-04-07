import leancloud


def getOrderByUser(user_id, limit=10, skip=0):
    User = leancloud.Object.extend('_User')
    user = User.create_without_data(user_id)
    query = leancloud.Query('Order')
    query.equal_to('user', user)
    query.include('title')
    query.include('price')
    query.limit(limit)
    query.skip(skip)
    result = query.find()
    # lst = []
    # for i in result:
    #     lst += [i.get('product')]
    return result


def getCollectionByUser():
    pass
