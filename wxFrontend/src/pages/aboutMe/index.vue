<template>
  <div>
    <i-card full :title="nickname" @click="navToUserinfo" :thumb="avatarurl"></i-card>
    <i-panel class="cell-panel-demo" title="账户">
      <i-cell-group>
        <i-cell title="修改密码" isLink url="/pages/changePassword/main" />
        <i-cell title="消息" isLink url="/pages/notice/main"/>
      </i-cell-group>
    </i-panel>

    <i-panel class="cell-panel-demo" title="关于">
      <i-cell title="关于弗恩英语" is-link url="/pages/aboutVron/main" />
    </i-panel>

    <i-button class="sign-out-button" @click="readyToExit" type="error">退出</i-button>

  </div>
</template>

<script>
import request from '@/utils/request'
export default {
  data () {
    return {
      nickname: '',
      avatar: ''
    }
  },
  computed: {
    avatarurl: function () {
      return request.baseURL + this.avatar
    }
  },
  methods: {
    navToUserinfo () {
      wx.navigateTo({url: '/pages/userinfo/main'})
    },
    readyToExit () {
      wx.showModal({
        title: '您确认退出吗?',
        content: '您的账户将会被注销',
        confirmText: '确定',
        cancelText: '取消',
        success: function (res) {
          if (res.confirm) {
            wx.clearStorage()
            wx.redirectTo({ url: '/pages/login/main' })
          }
        }
      })
    }
  },
  onShow () {
    let url = 'userinfo/'
    request
      .get(url)
      .then(res => {
        if (res.statusCode === 200) {
          this.nickname = res.data.nickname
          this.avatar = res.data.avatar
        }
      })
  }
}
</script>
<style scoped>
.sign-out-button {
  padding-top: 100rpx;
}
</style>
