
function createProduct(detail,title,description,price) {
    if(detail!==''){
       // document.getElementById('right').innerHTML=detail;

    const Title = AV.Object.extend('Strings');
    const c_title = new Title();
    c_title.set('english',title);
/*    c_title.save().then((t) => {
  console.log('保存成功c。objectId：'+t.getObjectId());
}, (error) => {
      console.log("error");
});*/
const Price = AV.Object.extend('Price');
    const c_price = new Price();
    c_price.set('dollar',price);
    c_price.set('CNY',price*6);
/*    c_price.save().then((p) => {
  console.log('保存成功p。objectId：'+p.getObjectId());
}, (error) => {
      console.log("error");
});*/
    const DES = AV.Object.extend('Strings');
    const des = new DES();
    des.set('english',description);
/*    des.save().then((d) => {
  console.log('保存成功d。objectId：'+d.getObjectId());
}, (error) => {
      console.log("error");
});*/
    const HTMLs = AV.Object.extend('HTMLs');
    const html  = new HTMLs();
    html.set('englishHTML',detail.toString());
/*   html.save().then((html) => {
  console.log('保存成功htmll。objectId：'+html.getObjectId());
}, (error) => {
      console.log("error");
  // 异常处理
});*/
    const Product = AV.Object.extend('Product');
    const product =  new Product();
    product.set('price',c_price);
    product.set('title',c_title);
    product.set('detail',html);
    product.set('description',des);
    product.save().then((pro) => {
  console.log('保存成功pro。objectId：'+pro.getObjectId());
}, (error) => {
      console.log("error");
  // 异常处理
});
    }
    else{
        console.log("enter your page");
    }
}

createProduct('<p>s</p>','ab','sa',15);





function updateProduct(id,detail,title,description,price){
      //  id = $('#id').val();
const Product = AV.Object.extend('Product');
const product = Product.createWithoutData(id);
product.set('title',title);
product.set('price',price);
product.set('detail',detail);
product.set('description',description);
product.save();

}