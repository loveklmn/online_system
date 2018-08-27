<template>
  <div>
    <toast :message="msg" :visible.sync="visible"></toast>
    <div class="login-icon"></div>

    <div class="login-from">
      <div class="inputView">
        <label class="loginLab">账号</label>
        <input class="inputText" v-model='username' type="text" placeholder="请输入用户名" />
      </div>
    </div>

    <div class="login-from">
      <div class="inputView">
        <label class="loginLab">密码</label>
        <input class="inputText" v-model='password' type="password" placeholder="请输入密码" />
      </div>
    </div>

    <div class="login-from">
      <div class="inputView">
        <label class="loginLab">密码</label>
        <input class="inputText" v-model='Rpassword' type="password" placeholder="再次输入密码" />
      </div>
    </div>

    <div class="login-from">
      <div class="inputView">
        <label class="loginLab">Key</label>
        <input class="inputText" v-model='key' type="text" placeholder="请输入key" />
      </div>
    </div>

  <button class="loginBtn" @click="check">确定</button>
 </div>
</template>

<script>
import toast from 'mpvue-toast'
import request from '@/utils/request'

export default {
  data () {
    return {
      username: '',
      password: '',
      Rpassword: '',
      msg: '',
      key: '',
      visible: false
    }
  },
  components: {
    toast
  },
  methods: {
    setVisible () {
      this.visible = !this.visible
    },
    register () {
      request.register(this.username, this.password, this.key).then(() => {
        wx.redirectTo({url: '../../pages/login/main'})
      }).catch((err) => {
        this.msg = err.message
        this.setVisible()
      })
    },
    check () {
      if (this.password === this.Rpassword && this.username !== '' && this.password !== '' && this.key !== '') {
        this.register()
      } else {
        this.msg = '您的注册格式有误,请保证账号密码不为空且两次密码输入一致'
        this.setVisible()
      }
    }
  }
}
</script>


<style>
input {
  padding: 20rpx
}

page {
  height: 100%;
}

.container {
  height: 100%;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  background-color: #f2f2f2
}

.login-icon {
  flex: none;
}

.login-img {
  width: 750rpx;
}

.login-from {
  margin-top: 20px;
  flex: auto;
  height:100%;
}

.inputView {
  background-color: #fff;
  line-height: 44px;
}

.nameImage, .keyImage {
  margin-left: 22px;
  width: 14px;
  height: 14px
}

.loginLab {
  padding-left: 40rpx;
  margin: 15px 15px 15px 10px;
  color: #545454;
  font-size: 14px
}

.inputText {
  flex: block;
  float: right;
  text-align: right;
  margin-right: 22px;
  color: #cccccc;
  font-size: 14px
}

.instruction {
  padding-left: 40rpx;
  padding-top: 30rpx;
  display: flex;
  font-size: 12px;
}

.instruction p{
  display: flex;
  color: gray;
}

.instruction a{
  color: green;
  display: flex;
}

.line {
  width: 100%;
  height: 1px;
  background-color: #cccccc;
  margin-top: 1px;
}

.loginBtnView {
  width: 100%;
  height: auto;
  background-color: #f2f2f2;
}

.loginBtn {
  width: 85%;
  margin-top: 35px;
  color: white;
  background-color: deepskyblue;
}
</style>
