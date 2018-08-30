<template>
  <div class="container">
    <image class="weui-grid__icon" :src="cover" />
    <div class="weui-grid__label"> {{title}} </div>
    <i-button @click="navToReadGuide" shape="circle" type="info">亲子阅读指导</i-button>
    <i-button @click="navToEBook" shape="circle" type="info">E-book</i-button>
    <i-button @click="navToPractice" shape="circle" type="info">课后练习</i-button>
    <i-button @click="navToFurtherRead" shape="circle" type="info">阅读拓展</i-button>
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
      this.navToFurtherRead()
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
  width: 240rpx;
  height: 240rpx;
  margin: 0 auto;
}

.weui-grid__label {
  display: block;
  margin-top: 5px;
  overflow: hidden;
  font-size: 14px;
  color: #000;
  text-align: center;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.punch {
  position: fixed;
  top: 110rpx;
  left: 690rpx;
  z-index: 9999;
  width: 80rpx;
  height: 100rpx;
  padding-top: 10rpx;
  padding-left: 20rpx;
  font-size: 30rpx;
  color: #6db0eb;
  background-color: #ebf9fe;
  border: none;
  border-radius: 20%;
}
</style>
