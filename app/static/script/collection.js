function setCollect(){
    var idArray = window.location.href.split("/");
    var id = idArray[idArray.length-1];
    console.log(id);
    const Collection = AV.Object.extend('CollectionMap');
        const collection = new Collection();
        console.log(id);
        query.get(id).then((product) => {
                const titleid     = product.get('title').getObjectId();
                const priceid     = product.get('price').getObjectId();
                const currentUser = AV.User.current();
                const title     = product.get('title');
                const price     = product.get('price');
            collection.set('user',currentUser);
            collection.set('product',product);
            collection.set('status',true);
     collection.save();
    });
}

function cancelCollect(id){
    const Collection = AV.Object.extend('CollectionMap');
    const collection = Collection.createWithoutData(id);
    collection.set('status',false);
    collection.save();
}