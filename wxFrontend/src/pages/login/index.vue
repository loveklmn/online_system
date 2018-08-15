<template>
  <div>
    <toast :message="msg" :visible.sync="visible"></toast>
    <i-panel style="padding:15 rpx" title="用户名">
      <input  v-model='username' type="text" placeholder="请输入用户名" />
    </i-panel>
    <i-panel style="padding:15 rpx" title="密码">
      <input v-model='password' type="password" placeholder="请输入密码" />
    </i-panel>
    <button @click="login">确定</button>
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
      console.log('requests start')
      request.post('/get-token/', {
        username: this.username,
        password: this.password
      }).then((res) => {
        console.log(res)
        if (res.statusCode === 200 && res.data.token) {
          console.log(res)
          this.$store.commit('setToken', res.data.token)
          wx.switchTab({url: '../../pages/index/main'})
        } else {
          this.msg = '用户名或密码错误'
          this.setVisible()
        }
      }).catch((err) => {
        this.msg = '网络错误'
        console.log(err)
      })
    }
  }
}
</script>

<style>
input{
  padding: 20rpx
}
</style>
