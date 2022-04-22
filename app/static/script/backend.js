    AV.init({
  appId: "pPObpvTV7pQB9poQHO1NJoMP-MdYXbMMI",
  appKey: "pShwYQQ4JVfSStc56MvkHNrr",
});
const queryP = new AV.Query('ProductTraffic');

let qp = queryP.greaterThan('visit',5);
qp.include('product.title');
qp.descending('visit');
qp.limit(5);
qp.find().then((products)=>{
    for(let a = 0;a<5;a++){
        let title = products[a].get('product').get('title').get('english');
        let visit = products[a].get('visit');
             console.log(products[a].get('product').get('title').get('english'));
             $('#mostVisit').append('<tr><td>'+title+'</td>' +
                 '<td class="text-muted">'+visit+'</td>'+'</td>' +
                 '<td class="text-muted">'+visit+'</td>'+'</td>' +
                 '<td class="text-muted">'+visit+'</td>'+
                 '<td class="text-end w-1">' +
                 '                        <div class="chart-sparkline chart-sparkline-sm" id="sparkline-bounce-rate-2"></div>' +
                 '</td>'+'</tr>');
    }
});