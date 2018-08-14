<template>
  <div>
    <toast :message="msg" :visible.sync="visible"></toast>
    <i-panel style="padding:15 rpx" title="旧密码">
      <input  v-model='username' type="text" placeholder="请输入用户名" />
    </i-panel>
    <i-panel style="padding:15 rpx" title="新密码">
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
      request.post('/login/', {
        username: this.username,
        password: this.password
      }).then((res) => {
        if (res.statusCode === 200 && res.data.userid) {
          console.log(res)
          this.$store.commit('setID', res.data.userid)
          this.$store.commit('setLevel', res.data.level)
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
