function setCollect(user,product){
 const Collection = AV.Object.extend('CollectionMap');
    const collection = new Collection();
    collection.set('user',user);
    collection.set('product',product);
    collection.set('status',true);
    collection.save();
}

function cancelCollect(id){
    const Collection = AV.Object.extend('CollectionMap');
    const collection = Collection.createWithoutData(id);
    collection.set('status',false);
    collection.save();
}