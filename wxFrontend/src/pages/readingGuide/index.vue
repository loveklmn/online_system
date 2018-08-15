<template>
  <div>
    <!-- readingGuide page -->
    <div class="weui-grid__label"> bookid: {{id}} </div>

    <i-panel  title="本课重点知识">
      <i-cell-group>
       <block v-for="(item,index) in vitalKnowledge" :key="index">
          <i-cell>{{item.content}}</i-cell>
        </block>
        </i-cell-group>
      </i-panel>
      
      <i-panel  title="今日导读">
         <block v-for="(item,index) in introReading" :key="index">
          <i-cell>{{item.content}}</i-cell>
         </block>
      </i-panel>

       <i-panel  title="词汇表">
         <i-cell-group>
          <block v-for="(item,index) in vocabulary" :key="index">
              <i-cell :title="item.word" :label="item.meaning"  @click="play(item.word)"></i-cell>
         </block>
         </i-cell-group>
      </i-panel>
  </div>
</template>

<script>

export default {
  data () {
    return {
      id: null,
      vitalKnowledge: [
        {
          content: 'Cat'
        },
        {
          content: 'Dog'
        },
        {
          content: 'Moon'
        }
      ],
      introReading: [
        {
          content: 'Cat的用法'
        },
        {
          content: 'Dog的语境'
        }
      ],
      vocabulary: [
        {
          word: 'cat',
          meaning: '猫猫'
        },
        {
          word: 'dog',
          meaning: '狗狗'
        },
        {
          word: 'flower',
          meaning: '花花'
        },
        {
          word: 'grass',
          meaning: '草草'
        }
      ]
    }
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

.placeholder {
  margin: 5px;
  padding: 0 10px;
  text-align: center;
  background-color: #ebebeb;
  height: 2.3em;
  line-height: 2.3em;
  color: #cfcfcf;
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
  vertical-align: middle;
  padding: 40rpx 80rpx;
  font-size: 30rpx;
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
