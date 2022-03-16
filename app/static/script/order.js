function MakeOrder(obj){
    const Order = AV.Object.extend('Order');
    const order  = new Order();
  if(checkLoginState()){
    let id = obj.getAttribute("id");
    const query = new AV.Query('Product');
    query.get(id).then((product) => {
  // order 就是 objectId 为 582570f38ac247004f39c24b 的 order 实例
  const title     = product.get('title').getObjectId();
  const price     = product.get('price').getObjectId();
  const currentUser = AV.User.current();
  let status = "delivering";
order.set('price',price);
order.set('status',status);
order.set('title',title);
order.set('user',currentUser.getObjectId());
  //const price  = order.get('priority');
//console.log(currentUser.getObjectId());
    order.save().then((order) => {
  // 成功保存之后，执行其他逻辑
  console.log('保存成功。objectId：'+order.getObjectId());
}, (error) => {
      console.log("error");
  // 异常处理
});
});



// 你还可以直接使用 AV.Object 的构造器


  }
  else{
     document.getElementById('result').innerText='not already login';
  }
}