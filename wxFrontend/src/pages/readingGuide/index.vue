<template>
  <div>
    <i-cell-group v-if="guidance">
      <div class="display_box">
        <wxParse :content="guidance" />
      </div>
    </i-cell-group>
    <i-panel title="词汇表" v-if="vocabulary.length">
      <i-cell-group>
        <block v-for="(item,index) in vocabulary" :key="index">
          <i-cell :title="'　'+item.word" :label="'　'+item.meaning" @click="play(item.word)"></i-cell>
        </block>
      </i-cell-group>
    </i-panel>
  </div>
</template>

<script>
import request from '@/utils/request'
import wxParse from 'mpvue-wxparse'
export default {
  components: {
    wxParse
  },
  data () {
    return {
      id: null,
      guidance: '',
      vocabulary: []
    }
  },
  onShow () {
    let url = 'books/' + this.id + '/guidance/'
    request
      .get(url)
      .then(res => {
        if (res.statusCode === 200) {
          this.vocabulary = res.data.words
          this.guidance = res.data.guidance
        }
      })
  },
  onLoad (options) {
    this.id = options.id
  },
  methods: {
    src (str) {
      let audiosrc = 'https://sp0.baidu.com/-rM1hT4a2gU2pMbgoY3K/gettts?lan=uk&text=' + str + '&spd=2&source=alading'
      return audiosrc
    },
    play (str) {
      wx.playBackgroundAudio({
        dataUrl: this.src(str)
      })
    }
  }
}
</script>

<style scoped>
@import url("~mpvue-wxparse/src/wxParse.css");

.display_box{
  padding:40rpx;
}

.weui-grid__icon {
  display: block;
  width: 170rpx;
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

.placeholder {
  height: 2.3em;
  padding: 0 10px;
  margin: 5px;
  line-height: 2.3em;
  color: #cfcfcf;
  text-align: center;
  background-color: #ebebeb;
}

.weui-flex__item {
  -webkit-box-flex: 1;
  -webkit-flex: 1;
  flex: 1;
  font-size: 30rpx;
}

.weui-flex {
  display: -webkit-box;
  display: -webkit-flex;
  display: flex;
}

.flex_item{
  padding: 40rpx 80rpx;
  font-size: 30rpx;
  vertical-align: middle;
}

.flex_button{
  width: 30rpx;
  height: 30rpx;
}

.cell-panel-demo{
    display: block;
    margin-top: 15px;
}
</style>
