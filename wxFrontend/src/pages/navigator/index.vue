<template>
  <div class="container">
    <image class="main-bg" src="../../static/images/main-bg.png"/>
    <image class="weui-grid__icon" :src="cover" />
    <div class="weui-grid__label"> {{title}} </div>
    <div @click="punch" v-if="punched==='false'">
      <label class="punch" >打<br>卡</label>
    </div>
    <i-button @click="navToReadGuide" shape="circle" type="primary">亲子阅读指导</i-button>
    <i-button @click="navToEBook" shape="circle" type="primary">E-book</i-button>
    <i-button @click="navToPractice" shape="circle" type="primary">课后练习</i-button>
    <i-button @click="navToFurtherRead" shape="circle" type="primary">阅读拓展</i-button>
  </div>
</template>

<script>
import request from '@/utils/request'
export default {
  methods: {
    navToReadGuide () {
      let url = '/pages/readingGuide/main?id=' + this.id
      wx.navigateTo({url: url})
    },
    navToEBook () {
      let url = '/pages/eBook/main?id=' + this.id + '&page=' + this.page
      wx.navigateTo({url: url})
    },
    navToPractice () {
      let url = '/pages/practice/main?id=' + this.id + '&title=' + this.title + '&cover=' + this.cover
      wx.navigateTo({url: url})
    },
    navToFurtherRead () {
      let url = '/pages/furtherReading/main?id=' + this.id
      wx.navigateTo({url: url})
    },
    punch () {
      wx.showModal({
        title: '您确定要打卡吗?',
        content: '您的作业将会出现在小伙伴中,您的书名将变为绿色',
        confirmText: '确定',
        cancelText: '取消',
        success: function (res) {
          if (res.confirm) {
            // punch api
            wx.switchTab({ url: '/pages/friendCircle/main' })
          }
        }
      })
    }
  },
  data () {
    return {
      id: null,
      title: null,
      cover: null,
      page: null,
      punched: true
    }
  },
  onLoad (options) {
    this.id = options.id
    this.title = options.title
    this.cover = options.cover
    this.punched = options.punched
    wx.setStorageSync('current', options.page)
    let url = 'books/' + this.id + '/progress/'
    request
      .post(url, {
        current_page: this.current
      })
  }
}
</script>

<style>
.container {
  padding-top: 100rpx;
  padding-bottom: 100rpx;
}

.weui-grid__icon {
  display: block;
  width: 170rpx;
  height: 240rpx;
  margin: 0 auto;
}

.weui-grid__label {
  margin-top: 5px;
  display: block;
  text-align: center;
  color: #000;
  font-size: 14px;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}

.punch {
  position: fixed;
  left: 690rpx;
  padding-left: 20rpx;
  top: 110rpx;
  padding-top: 10rpx;
  width: 80rpx;
  height: 100rpx;
  color: #6db0eb;
  font-size: 30rpx;
  background-color: #ebf9fe;
  border: none;
  z-index: 9999;
  border-radius: 20%;
}
</style>
