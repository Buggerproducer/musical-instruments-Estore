AV.init({
  appId: "pPObpvTV7pQB9poQHO1NJoMP-MdYXbMMI",
  appKey: "pShwYQQ4JVfSStc56MvkHNrr",
});

const c_user = AV.User.current();
const user_name = AV.User.current().get('username');

var idArray = window.location.href.split("/");
var conversation_id = idArray[4];
console.log(idArray);

$(document).ready(
    function () {
    var list = document.getElementById('communication');
    realtime.createIMClient(c_user).then(async function (user) {
        var query = user.getQuery();
        //query.containedIn('m', [c_user.id]);
        query.find().then(function (conversations) {
            for (conversation in conversations) {
                console.log(conversations[conversation].id);
                var li = document.createElement("li");
                li.className = 'clearfix'
                var a = document.createElement("a");
                var img = document.createElement("img");
                var div1 = document.createElement("div");
                var div2 = document.createElement("div");
                var div3 = document.createElement("div");
                var i = document.createElement("i");
                div1.className = "about"
                div2.className = "name"
                div3.className = "status"
                i.className = "fa fa-circle online"
                a.href = "/conversation/" + conversations[conversation].id
                img.src = "../static/chat-widget/img/t1.png"
                img.alt = "avatar"
                list.appendChild(li);
                li.appendChild(a);
                a.appendChild(img);
                a.appendChild(div1);
                div1.appendChild(div2);
                div1.appendChild(div3);
                div3.appendChild(i);
            }
        }).catch(console.error.bind(console));
        if(conversation_id!=1){
            console.log(conversation_id);
            user.getConversation(conversation_id).then(function(conversation) {
                console.log(conversation.id);
                conversation.queryMessages({
                    limit: 30, // limit 取值范围 1~100，默认 20
                }).then(function(messages) {
                    for(var i = 0;i<messages.length;i++){
                    console.log(messages[i].content['_lctext']);

                }
                console.log(messages)
                // 最新的十条消息，按时间增序排列
                }).catch(console.error.bind(console));
            }).catch(console.error.bind(console));
        }

    }).catch(console.error);

    }
)




/*user.createConversation({ // tom 是一个 IMClient 实例
  // 指定对话的成员除了当前用户 Tom（SDK 会默认把当前用户当做对话成员）之外，还有 Jerry
  members: ['lv'],
  // 对话名称
  name: 'lvjunyi & lv',
  unique: true
}).then(console.log("create"));

var { TextMessage } = require('leancloud-realtime');
let message  = '今天几号？';
conversation.send(new TextMessage(message)).then(function(message) {
  console.log('lv & lvjunyi', '发送成功！');
}).catch(console.error);*/

