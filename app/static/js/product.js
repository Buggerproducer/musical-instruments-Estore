
function createProduct(pagecontent) {
    if(pagecontent!==''){
        document.getElementById('right').innerHTML=pagecontent;
          const HTMLs = AV.Object.extend('HTMLs');
    const html  = new HTMLs();
    html.set('englishHTML',pagecontent.toString());
    console.log(pagecontent);

   html.save().then((html) => {
  console.log('保存成功。objectId：'+html.getObjectId());
}, (error) => {
      console.log("error");
  // 异常处理
});
    }
    else{
        console.log("enter your page");
    }
}

function updateProduct(id,pagecontent){
      //  id = $('#id').val();
const query = new AV.Query('HTMLs');
console.log(id);
query.get(id).then((page) => {
    let current = page.get('englishHTML');
     page.set('englishHTML',pagecontent.toString());
       page.save().then((html) => {
  console.log('保存成功。objectId：'+html.getObjectId());
}, (error) => {
      console.log("error");
  // 异常处理
});
});

}