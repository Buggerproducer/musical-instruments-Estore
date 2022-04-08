function MakeOrder(obj){
    const Order = AV.Object.extend('Order');
    const order  = new Order();
  if(checkLoginState()){
    let id = obj.getAttribute("id");
    const query = new AV.Query('Product');
    query.get(id).then((product) => {
  const titleid     = product.get('title').getObjectId();
  const priceid     = product.get('price').getObjectId();
  const currentUser = AV.User.current();
  const title     = product.get('title');
  const price     = product.get('price');
  console.log(title);
  let status = "delivering";
order.set('price',price);
order.set('status',status);
order.set('product',title);
order.set('user',currentUser);
    order.save().then((order) => {
  console.log('保存成功。objectId：'+order.getObjectId());
}, (error) => {
      console.log("error");
  // 异常处理
});
});
  }
  else{
     document.getElementById('result').innerText='not already login';
  }
}