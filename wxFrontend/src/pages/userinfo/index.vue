<template>
  <div>
    <div class="container">
      <div class="userinfo">
        <block >
          <image @click="changeAvatar" class="userinfo-avatar" :src="avatarurl" background-size="cover"/>
          <div class="usermotto">
            <input @blur="changeName" class="user-motto" :placeholder="nickname" />
          </div>
        </block>
      </div>
    </div>
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
    changeAvatar () {
      let vm = this
      wx.chooseImage({
        count: 1,
        sizeType: ['compressed'],
        sourceType: ['album', 'camera'],
        success: function (res) {
          var tempFilePaths = res.tempFilePaths[0]
          request.upload(tempFilePaths).then((url) => {
            vm.avatar = url
            vm.showConfirm()
          })
        }
      })
    },
    showConfirm () {
      let vm = this
      wx.showModal({
        title: '您确认更改吗?',
        content: '将会更新您的头像和名称',
        confirmText: '确定',
        cancelText: '取消',
        success: function (res) {
          if (res.confirm) {
            vm.change()
          }
        }
      })
    },
    change () {
      let vm = this
      request
        .post('userinfo/', {
          nickname: vm.nickname,
          avatar: vm.avatar
        })
    },
    changeName (e) {
      this.nickname = e.target.value
      this.showConfirm()
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

.container {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 200rpx 0;
  box-sizing: border-box;
}

.userinfo {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.userinfo-avatar {
  width: 512rpx;
  height: 512rpx;
  margin: 20rpx;
  border-radius: 50%;
}

.userinfo-nickname {
  color: #aaa;
}

.usermotto {
  margin-top: 20px;
  text-align: center;
}
</style>
