AV.init({
  appId: "pPObpvTV7pQB9poQHO1NJoMP-MdYXbMMI",
  appKey: "pShwYQQ4JVfSStc56MvkHNrr",
});
const query = new AV.Query('Cov19');
            query.equalTo('kind','cov19');
            query.find().then((status) => {
                if(status[0].get('status')){
                 document.getElementById('covid').innerText = "COVID-ALARM-ON";
                }else{
                    document.getElementById('covid').innerText = "COVID-ALARM-OFF";
                }
            });





function Cov19(){
    const COV = AV.Object.extend('Cov19');
    const cov  = new COV();
           // let id = obj.getAttribute("id");
            const query = new AV.Query('Cov19');
            query.equalTo('kind','cov19');
            query.find().then((status) => {
                if(status[0].get('status')){
                 status[0].set('status',false);
                document.getElementById('covid').innerText = "COVID-ALARM-OFF";
                }else{
                    status[0].set('status',true);
                     document.getElementById('covid').innerText = "COVID-ALARM-ON";
                }
               status[0].save().then((order) => {
                    console.log('保存成功。objectId：'+order.getObjectId());
                }, (error) => {
                    console.log("error");
    // 异常处理
                });
            });
}