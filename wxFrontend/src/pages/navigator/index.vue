<template>
<div>
  <image class="weui-grid__icon" :src="cover" />
  <div class="weui-grid__label"> {{title}} </div>
  <i-button @click="navToReadGuide" shape="circle" type="info">亲子阅读指导</i-button>
  <i-button @click="navToEBook" shape="circle" type="success">E-book</i-button>
  <i-button @click="navToPractice" shape="circle" type="warning">课后练习</i-button>
  <i-button @click="navToFurtherRead" shape="circle" type="error">阅读拓展</i-button>
</div>
</template>

<script>

export default {
  components: {
  },
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
      let url = '/pages/practice/main?id=' + this.id
      wx.navigateTo({url: url})
    },
    navToFurtherRead () {
      let url = '/pages/furtherReading/main?id=' + this.id
      wx.navigateTo({url: url})
    }
  },
  data () {
    return {
      id: null,
      title: null,
      cover: null,
      page: null
    }
  },
  onLoad (options) {
    this.id = options.id
    this.title = options.title
    this.cover = options.cover
    this.page = options.page
  }
}
</script>

<style>
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
</style>
