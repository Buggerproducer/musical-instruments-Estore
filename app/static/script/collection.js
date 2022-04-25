let collection_id;

function setCollect(){
    var idArray = window.location.href.split("/");
    var id = idArray[idArray.length-1];
    const Collection = AV.Object.extend('CollectionMap');
        const collection = new Collection();
        query.get(id).then((product) => {
                const titleid     = product.get('title').getObjectId();
                const priceid     = product.get('price').getObjectId();
                const currentUser = AV.User.current();
                const title     = product.get('title');
                const price     = product.get('price');
            collection.set('user',currentUser);
            collection.set('product',product);
            collection.set('status',true);
            collection.save().then((collection) => {
                collection_id = collection.id;
                $("#collection").attr("onclick", "cancelCollect()");
                document.getElementById('collection').innerText = "cancel collect";
            }, (error) => {
                console.log("error");
                // 异常处理
            });
    });
}

function cancelCollect(){
    var idArray = window.location.href.split("/");
    var id = idArray[idArray.length-1];
    const Collection = AV.Object.extend('CollectionMap');
    console.log(collection_id);
    const collection = Collection.createWithoutData(collection_id);
    collection.set('status',false);
    collection.save().then((order) => {
        document.getElementById('collection').innerText = "Add to your wish list"
        $("#collection").attr("onclick", "setCollect()");
    }, (error) => {
        console.log("error");
        // 异常处理
    });
}