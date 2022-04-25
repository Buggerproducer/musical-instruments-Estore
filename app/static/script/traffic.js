$(document).ready(
    add_traffic()
    );
function add_traffic(){
        var time = getTime(10);
        console.log(time);
        const query = new AV.Query('Traffic');
        query.equalTo('Date', time);
        query.find().then((visit) => {
            if(visit.length != 0){
                console.log(visit[0].get('Desktop'));
                visit[0].increment('Desktop', 1);
                console.log(visit[0].get('Desktop'));
                visit[0].save();
            }
            else{
                const Traffic = AV.Object.extend('Traffic');
                const traffic = new Traffic();
                traffic.set('Date', time);
                traffic.set('Desktop', 1);
                traffic.set('Mobile', 0);
                traffic.save().then((todo) => {
                    // 成功保存之后，执行其他逻辑
                    console.log(`保存成功`);
                    }, (error) => {
                    // 异常处理
                });
            }

        }, (error) => {
             console.log("error")
        });
        // query.get(id).then((product) => {
        //     console.log(product.get('visit_count'))
        //     product.increment('visit_count', 1);
        //     console.log(product.get('visit_count'))
        //     product.save();
        // }, (error) => {
        //     console.log("error")
        // });
      //document.getElementById('username2').innerText=current_user.getUsername();
}

function getTime(n){
    var myDate = new Date((new Date).getTime() + (n-10)*24*60*60*1000);
    var t1 = myDate.toJSON().split('T').join(' ').substr(0,10);
    return t1;
}