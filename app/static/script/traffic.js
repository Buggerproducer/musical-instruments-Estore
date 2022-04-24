$(document).ready(
    function add_traffic(){
        var time = getTime(10)
        console.log(time);
        const query = new AV.Query('Traffic');
        query.equalTo('Date', time)
        query.first().then((visit) => {
            console.log(visit.get('Desktop'));
            visit.increment('Desktop', 1);
            console.log(visit.get('Desktop'));
            visit.save();
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
});

function getTime(n){
    var myDate = new Date((new Date).getTime() + (n-10)*24*60*60*1000);
    var t1 = myDate.toJSON().split('T').join(' ').substr(0,10);
    return t1;
}