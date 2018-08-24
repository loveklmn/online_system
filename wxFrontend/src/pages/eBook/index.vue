<template>
  <div class="container">
    <div class="main">
      <div class="box">
        <div class="translate-warp" v-if="isTranslate&&translate!==''">{{translate}}</div>
        <swiper :current="currentPage" class="cont" duration="100" skip-hidden-item-layout="true" @change="changePage">
          <swiper-item v-for="page in pages" :key="page.number">
            <div class="item" v-for="(sen,index1) in page.sentences" :key="index1">
              <image @click="clickme" class="slide-image" :src="page.picture" />
              <label @click="activate(sen)" :class="sen.class" :style="sen.style"></label>
            </div>
          </swiper-item>
        </swiper>
        <div class="footer">
          <div class="item min foot_item" >
            <image @click="refresh" class="btn-min" :src="refreshIconSrc" />
            <div class="text">刷新</div>
          </div>
          <div class="item foot_item" >
            <image @click="record" class="play-btn" :src="playIconSrc" />
            <div class="text">录音</div>
          </div>
          <div class="item min">
            <image @click="setTranslate" class="btn-min" :src="translateIcon" />
            <div class="text">翻译</div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </template>
<script>
import request from '@/utils/request'
export default {
  data () {
    return {
      isTranslate: true,
      translate: '',
      voice: '',
      current: '',
      recordState: false,
      playState: false,
      pages: [
        {
          number: 0,
          picture: 'https://i.loli.net/2018/08/20/5b7aa40cb1bab.png',
          sentences: [
            {
              content: 'It is dark',
              audio: '',
              translated: '天黑了',
              x1: 188,
              y1: 114,
              x2: 230,
              y2: 210,
              class: ''
            },
            {
              content: 'It is dark in the park',
              audio: '',
              translated: '公园里天黑了',
              x1: 600,
              y1: 500,
              x2: 200,
              y2: 200,
              class: ''
            }
          ]
        },
        {
          number: 1,
          picture: 'https://i.loli.net/2018/08/20/5b7a3c66ef933.png',
          sentences: [
            {
              content: 'I do something',
              audio: '',
              translated: '公园里天黑了',
              x1: 300,
              y1: 260,
              x2: 350,
              y2: 332,
              class: ''
            }
          ]
        }
      ]
    }
  },
  onLoad (options) {
    this.id = options.id
    this.current = options.page
    this.countBox()
    this.current = wx.getStorageSync('current')
  },

  computed: {
    playIconSrc: function () {
      if (this.playState === true) {
        return '../../static/images/play_play.png'
      }
      if (this.recordState === true) {
        return '../../static/images/play_recording.png'
      }
      return '../../static/images/play_toberecord.png'
    },
    refreshIconSrc: function () {
      if (this.playState === true) {
        return '../../static/images/refresh_active.png'
      } else {
        return '../../static/images/refresh_default.png'
      }
    },
    translateIcon: function () {
      if (this.isTranslate === true) {
        return '../../static/images/translate_active.png'
      } else {
        return '../../static/images/translate_default.png'
      }
    },
    currentPage: function () {
      return this.current
    }
  },
  methods: {
    countBox: function () {
      this.pages.forEach(
        function (page) {
          page.sentences.forEach(
            function (sen) {
              sen.class = ''
              sen.style = `position:absolute; top:${sen.x1}rpx; left:${sen.y1}rpx; width:${sen.x2 - sen.x1}rpx;height:${sen.y2 - sen.y1}rpx`
            })
        })
    },
    setTranslate () {
      this.isTranslate = !this.isTranslate
    },
    activate (sen) {
      let vm = this
      let url = 'https://sp0.baidu.com/-rM1hT4a2gU2pMbgoY3K/gettts?lan=uk&text=' + sen.content.replace(/ /g, '%20') + '&spd=2&source=alading'
      wx.playBackgroundAudio({dataUrl: url})
      this.pages.forEach(
        function (page) {
          page.sentences.forEach(
            function (sen) {
              sen.class = ''
            })
          sen.class = 'active'
          vm.translate = sen.translated
        })
    },
    changePage (e) {
      this.translate = ''
      this.current = e.target.current
      this.refresh()
      let url = 'books/' + this.id + '/progress/'
      request.post(url, {
        current_page: this.current
      })
      wx.setStorageSync('current', this.current)
    },
    record () {
      let vm = this
      if (this.playState === true) {
        wx.playVoice({
          filePath: this.voice
        })
      } else if (this.recordState === false) {
        this.recordState = true
        wx.startRecord({
          success: function (e) {
            vm.voice = e.tempFilePath
          }
        })
      } else {
        this.recordState = false
        wx.stopRecord()
        this.playState = true
      }
    },
    refresh () {
      this.recordState = false
      this.playState = false
    }
  }
}
</script>

<style scoped>
.contain{
  background-color: #f7fbfe;
}

swiper {
    width: 100%;
    height: 100%;
}

swiper-item {
    position: relative;
    height: 100%;
}

.slide-image {
    width: 100%;
    height: 100%;
    display: block;
}

swiper-item label {
    position: absolute;
    box-sizing: border-box;
    border-radius: 3px;
}

swiper-item label.active {
    border: 2px solid #5187e8;
}

.item {
  width: 100%;
  height: 100%;
}
.cont {
width: 93%;
height: 920rpx;
padding: 25rpx;
padding-top: 80rpx;
font-size: 28rpx;
}

.banner {
  width: 100%;
  height: auto;
  display: block;
}

.slide-image {
  width: 100%;
  height: auto;
}
.weui-grid__icon {
  display: block;
  width: 170rpx;
  height: 240rpx;
  margin: 0 auto;
}

.weui-grid__label {
  padding-top: 50rpx;
  margin-top: 5px;
  display: block;
  text-align: center;
  color: #000;
  font-size: 14px;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}

.foot_item {
  margin-right: 126rpx;
}
page {
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: #fff;
    -webkit-overflow-scrolling: auto;
    position: fixed;
}

.container {
    width: 100%;
    height: 100%;
}

.main {
    box-sizing: border-box;
    width: 100%;
    height: 100%;
    padding: 0 8px 86px;
}

.main .box {
    width: 100%;
    height: 100%;
    position: relative;
}

.main .box .locked {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: transparent;
}

swiper {
    width: 100%;
    height: 100%;
}

swiper-item {
    position: relative;
}

.slide-image {
    width: 100%;
    height: 100%;
    display: block;
}

swiper-item label {
    position: absolute;
    box-sizing: border-box;
    border-radius: 3px;
}

swiper-item label.active {
    border: 2px solid #f23442;
}

.footer {
    box-sizing: border-box;
    position: fixed;
    bottom: 0;
    width: 100%;
    padding: 0 104rpx;
    height: 82px;
    background: url('https://ddbcdn.kingsunedu.com/wx/v2/book_bg.png') center top no-repeat;
    background-size: cover;
    font-size: 24rpx;
    color: #888;
}

.footer .item {
    display: inline-block;
    width: 97rpx;
    height: 97rpx;
    padding-top: 8px;
    text-align: center;
}

.footer .item .text {
    padding-top: 4px;
}

.play-btn {
    width: 97rpx;
    height: 97rpx;
    vertical-align: top;
}

.btn-min {
    width: 68rpx;
    height: 68rpx;
    vertical-align: top;
}

.catalog-btn {
    position: fixed;
    top: 40rpx;
    right: 0;
    width: 66rpx;
    height: 101rpx;
}

.catalog-btn image {
    width: 100%;
    height: 100%;
}

.mask {
    position: fixed;
    z-index: 100;
    top: 0;
    right: 0;
    left: 0;
    bottom: 0;
    background: rgba(0,0,0,0.6);
}

.rightSlide .wrapper {
    position: fixed;
    right: 0;
    bottom: 0;
    width: 80%;
    height: 100%;
    overflow: auto;
    background-color: #fff;
    transform: translate(100%,0);
    backface-visibility: hidden;
    z-index: 101;
    transition: transform 0.3s;
    transition: transform 0.3s,-webkit-transform 0.3s;
}

.rightSlide .toggle {
    transform: translate(0,0);
}

.rightSlide .wrapper .bd {
    padding: 50rpx 27rpx 0 40rpx;
    position: relative;
}

.rightSlide .wrapper .bd .item {
    margin-bottom: 20rpx;
}

.rightSlide .wrapper .bd .sub {
    padding: 0 0 0 20rpx;
    line-height: 86rpx;
    font-size: 28rpx;
}

.rightSlide .locked .h3 {
    padding-right: 36rpx;
    background: url('https://ddbcdn.kingsunedu.com/wx/v2/ic_locked.png') right top no-repeat;
    background-size: 26rpx 34rpx;
}

.rightSlide .locked:first-child .h3,.rightSlide .item:first-child .h3 {
    background: none;
    padding-right: 145rpx;
}

.rightSlide .translate {
    position: absolute;
    right: 27rpx;
    top: 40rpx;
    width: 139rpx;
    height: 49rpx;
}

.rightSlide .translate image {
    width: 100%;
    height: 100%;
}

.translate-warp {
    box-sizing: border-box;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    text-align: center;
    background: rgba(0,0,0,0.5);
    color: #fff;
    font-size: 28rpx;
    padding: 10rpx 30rpx;
}
</style>
