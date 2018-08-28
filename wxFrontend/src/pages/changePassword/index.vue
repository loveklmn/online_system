<template>
  <div>
    <toast :message="msg" :visible.sync="visible"></toast>
    <div class="login-icon">
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

    <button class="loginBtn" @click="check">确定</button>
</div>
</template>

<script>
import toast from 'mpvue-toast'
import request from '@/utils/request'

export default {
  data () {
    return {
      password: '',
      Rpassword: '',
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
    change () {
      let url = 'userinfo/change-password/'
      request.post(url, {password: this.password}).then((res) => {
        if (res.statusCode === 200) {
          wx.redirectTo({url: '../../pages/login/main'})
        } else {
          this.msg = res.data.msg
          this.setVisible()
        }
      }).catch((err) => {
        this.msg = err.message
        this.setVisible()
      })
    },
    check () {
      if (this.password === this.Rpassword && this.password !== '') {
        this.change()
      } else {
        this.msg = '密码不为空且两次密码输入一致'
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
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  height: 100%;
  background-color: #f2f2f2
}

.login-icon {
  flex: none;
}

.login-img {
  width: 750rpx;
}

.login-from {
  flex: auto;
  height:100%;
  margin-top: 20px;
}

.inputView {
  line-height: 44px;
  background-color: #fff;
}

.nameImage, .keyImage {
  width: 14px;
  height: 14px;
  margin-left: 22px
}

.loginLab {
  padding-left: 40rpx;
  margin: 15px 15px 15px 10px;
  font-size: 14px;
  color: #545454
}

.inputText {
  flex: block;
  float: right;
  margin-right: 22px;
  font-size: 14px;
  color: #cccccc;
  text-align: right
}

.instruction {
  display: flex;
  padding-top: 30rpx;
  padding-left: 40rpx;
  font-size: 12px;
}

.instruction p{
  display: flex;
  color: gray;
}

.instruction a{
  display: flex;
  color: green;
}

.line {
  width: 100%;
  height: 1px;
  margin-top: 1px;
  background-color: #cccccc;
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
