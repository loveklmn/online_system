<template>
  <div>
    <image class="weui-grid__icon" :src="cover" />
    <div class="weui-grid__label"> {{title}} </div>
    <i-button @click="navToGame1(id)" shape="circle" type="primary">连线游戏</i-button>
    <i-button @click="navToGame2(id)" shape="circle" type="primary">识别单词游戏</i-button>
    <i-button @click="navToGame3(id)" shape="circle" type="primary">拼图游戏</i-button>
    <i-button @click="navToGame4(id)" shape="circle" type="primary">选词填空</i-button>
  </div>
</template>

<script>
export default {
  methods: {
    navToGame1: function () {
      let url = '/pages/matchingGame/main?id=' + this.id
      wx.navigateTo({url: url})
    },
    navToGame2: function () {
      let url = '/pages/recognitionGame/main?id=' + this.id
      wx.navigateTo({url: url})
    },
    navToGame3: function () {
      let url = '/pages/jigsawPuzzles/main?id=' + this.id
      wx.navigateTo({url: url})
    },
    navToGame4: function () {
      let url = '/pages/clozeGame/main?id=' + this.id
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
  width: 240rpx;
  height: 240rpx;
  padding-top: 100rpx;
  margin: auto;
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
</style>
