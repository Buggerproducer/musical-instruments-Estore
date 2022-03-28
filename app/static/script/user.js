AV.init({
  appId: "pPObpvTV7pQB9poQHO1NJoMP-MdYXbMMI",
  appKey: "pShwYQQ4JVfSStc56MvkHNrr",
});

$(document).ready(
    function change(){
      const current_user = AV.User.current();
      document.getElementById('username').innerText="HELLO, " + current_user.getUsername();
        console.log(sessionStorage.getItem('authenticated'))

      //document.getElementById('username2').innerText=current_user.getUsername();
});



function testConnect() {
  const TestObject = AV.Object.extend('TestObject');
  const testObject = new TestObject();
  testObject.set('words', 'Hello world!');
  testObject.save().then((testObject) => {
    console.log('保存成功。')
  })
}

async function signUp(username, email, phone, password, onSuccess, onFail){
    // 创建实例
    const user = new AV.User();

    // 等同于 user.set('username', 'Tom')
    user.setUsername(username);
    user.setPassword(password);

    // 可选
    if(phone !== null){
      user.setMobilePhoneNumber(phone);
    }
    if(email !== null){
      user.setEmail(email);
    }

    user.signUp().then((user) => {
      // 注册成功
      console.log(`注册成功。objectId：${user.id}`);
      onSuccess(user);
    }, (error) => {
      // 注册失败（通常是因为用户名已被使用）
      onFail(error)
    });
}

async function signInWithUsername(username,password, onSuccess, onFail){
    let key = 'authenticated';
  AV.User.logIn(username, password).then((user) => {
      // 登录成功
////
      const current_user = AV.User.current();
      $.post('/checkLogin',
          {
              'user': current_user.get('username')
          }).done(
          function(response){
                console.log(response);
                console.log(sessionStorage.getItem('authenticated'));
          });

      onSuccess(user);
  }, (error) => {
      // 登录失败（可能是密码错误）

      onFail(error)
  });
}

async function signInWithEmail(email,password, onSuccess, onFail){
    AV.User.loginWithEmail(email, password).then((user) => {
      // 登录成功
      onSuccess(user)
    }, (error) => {
      // 登录失败（可能是密码错误）
      onFail(error)
    });
}

async function logout() {
    console.log(getLoginState());
    if(getLoginState()!=null){
        AV.User.logOut();
        alert('logout successfully');
        const current_user = AV.User.current();
        let username;
        if(current_user==null){
            username = null;
        }
        else{
            username = current_user.get('username');
        }
        $.post('/checkLogin',
          {
              'user': username
          }).done(
          function(response){
              $("a#logouta").attr("href", "/signUp")
              document.getElementById('logout').innerText = "Login & Sign Up"
          });
        // document.getElementById('result').innerText='logout successfully';
    }
    else{
            // document.getElementById('result').innerText='not already login';
        alert('not already login');
    }
    //console.log('logout successfully');
}

function getLoginState(){
  return AV.User.current()
}

function checkLoginState(){
  return !!AV.User.current();
}


function changeInfo(username,phone,email){
    if(getLoginState()!=null){
        const currentUser = AV.User.current();
        if(username!==''){
            currentUser.setUsername(username);
        }
        if(phone!==''){
            currentUser.setMobilePhoneNumber(phone);
        }
        if(email!==''){
            currentUser.setEmail(email);
        }
        currentUser.save().then((currentUser) => {
  // 成功保存之后，执行其他逻辑
  console.log(`保存成功。objectId：${currentUser.id}`);
  document.getElementById('result').innerText='successfully change';
}, (error) => {
  // 异常处理
            document.getElementById('result').innerText='fail to change';
            console.log(`保存失败。objectId：${currentUser.id}`);
});
    }
    else{
          document.getElementById('result').innerText='not already login';
    }
}

function reset(email) {
    AV.User.requestPasswordReset(email);
      document.getElementById('result').innerText='email has been sent';
}