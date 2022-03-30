
const user_name = AV.User.current().get('username');








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

