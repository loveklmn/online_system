<template>
  <div>
    <toast message="错误" :visible.sync="visible"></toast>
    <i-panel style="padding:15 rpx" title="旧密码">
      <input  v-model='oldpwd' type="password" placeholder="请输入旧密码" />
      </i-panel>
      <i-panel style="padding:15 rpx" title="新密码">
      <input v-model='newpwd1' type="password" placeholder="请输入新密码" />
      <input v-model='newpwd2' type="password" placeholder="再次输入新密码" />
    </i-panel>
    <i-button @click="change">确定</i-button>
    <i-alert type="error" v-if="visible === false">
    您的输入有误
    <view slot="desc">新密码不能为空或与老密码相同,\n请保持新密码两次输入一致</view>
</i-alert>
  </div>
</template>

<script>
import toast from 'mpvue-toast'

export default {
  data () {
    return {
      oldpwd: '',
      newpwd1: '',
      newpwd2: '',
      visible: null
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
      // if oldpwd is right
      if (this.newpwd1 === this.newpwd2 && this.newpwd1 !== '' && this.oldpwd !== this.newpwd1) {
        // implement change password function
      } else {
        this.setVisible(false)
      }
    }
  },
  created () {}
}
</script>

<style>
  input{padding:7px 15px;color:#495060}
  .input-title{color:#495060;min-width:65px;padding-right:10px}
</style>
