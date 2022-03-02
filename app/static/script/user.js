AV.init({
  appId: "pPObpvTV7pQB9poQHO1NJoMP-MdYXbMMI",
  appKey: "pShwYQQ4JVfSStc56MvkHNrr",
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
  AV.User.logIn(username, password).then((user) => {
      // 登录成功
    onSuccess(user)
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
        document.getElementById('result').innerText='logout successfully';
    }
    else{
            document.getElementById('result').innerText='not already login';
    }
    //console.log('logout successfully');


}

function getLoginState(){
  return AV.User.current()
}

function checkLoginState(){
  return !!AV.User.current();
}

