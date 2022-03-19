
function createProduct() {
    let pagecontent = editor.txt.html();
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

function updateProduct(title){

}