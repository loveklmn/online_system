<template>
  <div>
    <toast :message="msg" :visible.sync="visible"></toast>
    <div class="login-icon">
      <image class="login-img" src="../../static/images/loginLog.jpg" />
    </div>
    <div class="login-from">
      <div class="inputView">
        <image class="nameImage" src="../../static/images/name.png" />
        <label class="loginLab">账号</label>
        <input class="inputText" v-model='username' type="text" placeholder="请输入用户名" />
      </div>
    </div>
    <div class="login-from">
      <div class="inputView">
        <image class="keyImage" src="../../static/images/password.png" />
        <label class="loginLab">密码</label>
        <input class="inputText" v-model='password' type="password" placeholder="请输入密码" />
      </div>
    </div>
    <div class="instruction">
      <a href="/pages/register/main">还没有账户?来注册一下~</a>
    </div>
    <button class="loginBtn" @click="login">确定</button>
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

      msg: '',
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
    login () {
      request.login(this.username, this.password).then(() => {
        wx.switchTab({url: '../../pages/index/main'})
      }).catch((err) => {
        this.msg = err.message
        this.setVisible()
      })
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
  margin-top: 15px;
  margin-left: 22px;
  width: 14px;
  height: 14px
}

.loginLab {
  margin: 0px 15px 15px 10px;
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
  padding-top: 20rpx;
  display:flex;
  font-size: 20rpx;
}

.instruction a {
  display:flex;
  font-size: 20rpx;
  color: gray;
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
  width: 90%;
  margin-top: 35px;
  color: white;
  background-color:#f28d01;
}
</style>
