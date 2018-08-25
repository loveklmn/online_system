<template>
<div>
  <image class="weui-grid__icon" :src="cover" />
  <div class="weui-grid__label"> {{title}} </div>
  <image class="main-bg" src="../../static/images/main-bg.png"/>

<i-button @click="navToGame1(id)" shape="circle" type="info">连线游戏</i-button>
<!-- <i-button @click="navToGame2(id)" shape="circle" type="success">识别单词游戏</i-button> -->
<i-button @click="navToGame3(id)" shape="circle" type="info">拼图游戏</i-button>
<!-- <i-button @click="navToGame4(id)" shape="circle" type="error">选词填空</i-button> -->

  </div>
</template>

<script>

export default {
  methods: {
    navToGame1: function () {
      let url = '/pages/matchingGame/main'
      wx.navigateTo({url: url})
    },
    navToGame3: function () {
      let url = '/pages/jigsawPuzzles/main'
      wx.navigateTo({url: url})
    }
  },
  data () {
    return {
      id: null,
      cover: '',
      title: ''
    }
  },
  onLoad (options) {
    this.id = options.id
    this.title = options.title
    this.cover = options.cover
  }
}
</script>

<style>
.weui-grid__icon {
  display: block;
  width: 170rpx;
  height: 240rpx;
  margin: auto;
  padding-top: 100rpx;
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
