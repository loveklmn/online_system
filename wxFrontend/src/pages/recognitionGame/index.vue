<template>
  <div>
    <view class="answer">
    <toast :message="msg" :visible.sync="visible"></toast>
    <view class="word">
      <img :src="rimg" />
    </view>
    <view class="btn_group">
        <view class="btn_container" >
          <button @click="right" class="answer word" v-if="rand === 0">
            A.　　{{correct_word}}
          </button>
          <button @click="wrong" class="answer word">
            {{choice[rand][0]}}.　　{{wrong_word_1}}
          </button>
          <button @click="right" class="answer word" v-if="rand === 1">
            B.　　{{correct_word}}
          </button>
          <button @click="wrong" class="answer word">
            {{choice[rand][1]}}.　　{{wrong_word_2}}
          </button>
          <button @click="right" class="answer word" v-if="rand === 2">
            C.　　{{correct_word}}
          </button>
        </view>
    </view>
</view>

  </div>
</template>

<script>
import toast from 'mpvue-toast'
import request from '@/utils/request'
export default {
  data () {
    return {
      img: '',
      correct_word: '',
      wrong_word_1: '',
      wrong_word_2: '',
      wrong_word_3: '',
      msg: '',
      visible: false,
      choice: [
        ['B', 'C'],
        ['A', 'C'],
        ['A', 'B']
      ],
      correct1src: '/static/audios/correct1.mp3',
      wrongsrc: '/static/audios/wrong.mp3'
    }
  },
  components: {
    toast
  },
  methods: {
    setVisible () {
      this.visible = !this.visible
      setTimeout(() => {
        this.visible = !this.visible
      }, 1000)
    },
    right () {
      this.msg = '恭喜你,答对了!'
      this.setVisible()
      this.make_correct_sound()
    },
    wrong () {
      this.msg = '不正确哦,再想想'
      this.setVisible()
      this.make_wrong_sound()
    },
    make_correct_sound: function () {
      this.innerAudioContext.src = this.correct1src
      this.innerAudioContext.play()
    },
    make_wrong_sound: function () {
      this.innerAudioContext.src = this.wrongsrc
      this.innerAudioContext.play()
    }
  },
  computed: {
    rand: function () {
      return Math.floor(Math.random() * 3)
    },
    rimg: function () {
      return request.baseURL + this.img
    }
  },
  onLoad (options) {
    let url = 'books/' + options.id + '/RecognitionGame/'
    let vm = this
    request.get(url)
      .then(res => {
        vm.img = res.data.img
        vm.correct_word = res.data.correct_word
        vm.wrong_word_1 = res.data.wrong_word_1
        vm.wrong_word_2 = res.data.wrong_word_2
      })
  },
  mounted () {
    this.innerAudioContext = wx.createInnerAudioContext()
  }
}
</script>

<style>
page {
  padding-top: 100rpx;
}

.auth {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0,0,0,0.2);
    z-index: 20;
}

.auth .modal_IOS {
    width: 620rpx;
    height: 516rpx;
    background: #fff;
    border-radius: 10rpx;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-left: -310rpx;
    margin-top: -358rpx;
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    flex-direction: column;
    -webkit-box-pack: justify;
    justify-content: space-between;
    -webkit-box-align: center;
    align-items: center;
}

.auth .modal_IOS .title {
    font-weight: bold;
    height: 98rpx;
    line-height: 98rpx;
    width: 100%;
    text-align: center;
    font-size: 36rpx;
    color: #000;
    box-sizing: border-box;
    letter-spacing: 1.8rpx;
    border-bottom: 1rpx solid #C7C6C8;
}

.auth .modal_IOS image {
    width: 70rpx;
    height: 70rpx;
    margin-top: 35rpx;
}

.auth .modal_IOS .des {
    width: 500rpx;
    font-size: 30rpx;
    color: #000;
    line-height: 97rpx;
    box-sizing: border-box;
    height: 97rpx;
    border-bottom: 1rpx solid #DADADA;
}

.auth .modal_IOS .con {
    width: 500rpx;
    font-size: 28rpx;
    color: #888888;
    text-align: center;
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
    margin-top: 35rpx;
    -webkit-box-flex: 1;
    flex: 1;
}

.auth .modal_IOS .con::before {
    content: '';
    display: block;
    width: 10rpx;
    height: 10rpx;
    background: #888;
    border-radius: 50%;
    margin: 14rpx 19rpx 0 0;
}

.auth .modal_IOS .operator {
    width: 100%;
    height: 88rpx;
    font-size: 34rpx;
    color: #000;
    box-sizing: border-box;
    border-top: 1rpx solid #CAC9CB;
    margin-bottom: 0;
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
}

.auth .modal_IOS .operator .refuse {
    text-align: center;
    -webkit-box-flex: 1;
    flex: 1;
    height: 100%;
    line-height: 86rpx;
}

.auth .modal_IOS .operator .agree {
    text-align: center;
    -webkit-box-flex: 1;
    flex: 1;
    box-sizing: border-box;
    border-left: 1rpx solid #CAC9CB;
    color: #2FB922;
    line-height: 86rpx;
    height: 100%;
}

.auth .modal {
    padding: 60rpx 50rpx 50rpx 50rpx;
    width: 550rpx;
    height: 490rpx;
    background: #fff;
    box-sizing: border-box;
    border-radius: 3rpx;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-left: -285rpx;
    margin-top: -245rpx;
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    flex-direction: column;
    -webkit-box-pack: justify;
    justify-content: space-between;
}

.auth .modal .title {
    font-size: 38rpx;
    color: #353535;
    font-weight: bold;
}

.auth .modal .wrap {
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
    height: 150rpx;
    -webkit-box-align: center;
    align-items: center;
    border-bottom: 1rpx solid #DADADA;
    box-sizing: border-box;
}

.auth .modal .wrap image {
    width: 80rpx;
    height: 80rpx;
}

.auth .modal .wrap .des {
    font-size: 28rpx;
    color: #353535;
    letter-spacing: 1.4rpx;
    margin-left: 25rpx;
    -webkit-box-flex: 1;
    flex: 1;
}

.auth .modal .con {
    font-size: 28rpx;
    color: #888888;
    text-align: center;
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
    margin-top: 40rpx;
    -webkit-box-flex: 1;
    flex: 1;
}

.auth .modal .con::before {
    content: '';
    display: block;
    width: 10rpx;
    height: 10rpx;
    background: #888;
    border-radius: 50%;
    margin: 14rpx 19rpx 0 0;
}

.auth .modal .operator {
    font-size: 28rpx;
    color: #000;
    box-sizing: border-box;
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
    -webkit-box-pack: end;
    justify-content: flex-end;
}

.auth .modal .operator .refuse {
    margin-right: 55rpx;
}

.auth .modal .operator .agree {
    color: #2FB922;
    margin-right: 20rpx;
}

.player .voice {
    position: relative;
    height: 90rpx;
    display: -webkit-box;
    display: flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    display: -webkit-flex;
    width: 140rpx;
    margin: 0 auto;
    text-align: center;
    box-sizing: border-box;
}

.player .voice image {
    width: 40rpx;
    height: 40rpx;
}

.horizon-progress .progress {
    margin: 36rpx auto;
    width: 630rpx;
    height: 16rpx;
    background: #F6F6F6;
    border-radius: 100rpx;
    position: relative;
    box-sizing: border-box;
}

.horizon-progress .progress .curr_progress {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    left: 0;
    height: 8rpx;
    background-image: linear-gradient(135deg,#FFD600 0,#FF702B 100%);
    border-radius: 100rpx;
}

.warn-modal {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    background: rgba(0,0,0,0.16);
    z-index: 11;
}

.warn-modal .modal {
    width: 560rpx;
    height: 380rpx;
    position: fixed;
    z-index: 3;
    background: #fff;
    border-radius: 8rpx;
    top: 330rpx;
    left: 50%;
    transform: translateX(-50%);
}

.warn-modal .modal .topnav {
    text-align: right;
    overflow: hidden;
}

.warn-modal .modal .topnav .close_container {
    width: 82rpx;
    height: 72rpx;
    padding-right: 31rpx;
    box-sizing: border-box;
    float: right;
}

.warn-modal .modal .topnav .close_container .close {
    display: none;
    margin-top: 30rpx;
    width: 30rpx;
    height: 30rpx;
}

.warn-modal .modal .rest {
    padding: 30rpx 47rpx;
    box-sizing: border-box;
}

.warn-modal .modal .rest .winner {
    width: 82rpx;
    height: 82rpx;
    display: block;
    margin: 0 auto;
}

.warn-modal .modal .rest .nickname {
    font-size: 36rpx;
    color: #322A22;
    margin-top: 34rpx;
    text-align: center;
}

.warn-modal .modal .rest .desc {
    font-size: 30rpx;
    color: #B1A79D;
    text-align: center;
    margin-top: 30rpx;
}

.warn-modal .modal .rest .introduce-item {
    padding: 0 40rpx;
    box-sizing: border-box;
    display: -webkit-box;
    display: flex;
    display: -webkit-flex;
    margin-bottom: 50rpx;
}

.warn-modal .modal .rest .introduce-item image {
    width: 120rpx;
    height: 120rpx;
}

.warn-modal .modal .rest .introduce-item .introduce-container {
    -webkit-box-flex: 1;
    flex: 1;
    height: 100%;
    margin-left: 46rpx;
    text-align: left;
}

.warn-modal .modal .rest .introduce-item .introduce-container .title {
    color: #322A20;
    font-size: 30rpx;
}

.warn-modal .modal .rest .introduce-item .introduce-container .introduce-desc {
    margin: 0;
    font-size: 24rpx;
    color: #B1A79C;
}

.warn-modal .modal .rest button {
    width: 240rpx;
    height: 90rpx;
    background: #FFD600;
    box-shadow: 0 1rpx 15rpx 0 rgba(236,205,46,0.5);
    border-radius: 100rpx;
    margin: 35rpx auto;
    font-size: 30rpx;
    line-height: 90rpx;
    color: #322A22;
}

.warn-modal .modal .rest button::after {
    border: none;
}

.book_container {
    position: relative;
    width: 100%;
    height: 205rpx;
    margin-bottom: 37rpx;
    box-shadow: 0 2rpx 16rpx 0 rgba(210,210,210,0.6);
}

.book_container .bookinfo {
    display: -webkit-box;
    display: flex;
    -webkit-box-pack: start;
    justify-content: flex-start;
    -webkit-box-align: center;
    align-items: center;
    display: -webkit-flex;
    box-sizing: border-box;
    padding: 35rpx 53rpx;
}

.book_container .bookinfo .image {
    width: 116rpx;
    height: 116rpx;
    margin-right: 52rpx;
}

.book_container .bookinfo .bookname {
    font-size: 36rpx;
}

.choose {
    position: absolute;
    right: 0;
    bottom: 0;
    width: 40rpx;
    height: 40rpx;
}

.transparentmodal {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255,255,255,0);
    z-index: 10;
    text-align: center;
}

.transparentmodal image {
    margin-top: 442rpx;
    width: 180rpx;
    height: 180rpx;
}

.answer .word {
    font-weight: bold;
    font-size: 80rpx;
    color: #322A22;
    text-align: center;
}

.answer .wordb {
    font-size: 30rpx;
    font-weight: bold;
    color: #554C44;
    text-align: center;
    margin-bottom: 25rpx;
}

.answer .btn_group {
    width: 630rpx;
    margin: 40rpx auto;
}

.answer .btn_group .btn_container {
    position: relative;
}

.answer .btn_group .btn_container button {
    width: 100%;
    height: 100rpx;
    border-radius: 100rpx;
    box-shadow: 0 2rpx 16rpx 0 rgba(210,210,210,0.6);
    background: #fff;
    font-size: 30rpx;
    color: #554C44;
    text-indent: 126rpx;
    text-align: left;
    line-height: 100rpx;
    box-sizing: border-box;
    margin-bottom: 40rpx;
}

.answer .btn_group .btn_container button::after {
    border: none;
}

.answer .btn_group .btn_container button.error {
    color: #fff;
    background: #FF6538;
}

.answer .btn_group .btn_container button.bingo {
    color: #fff;
    background: #44D878;
}

.answer .btn_group .btn_container button.nosure {
    color: #fff;
}

.answer .btn_group .btn_container #options {
    position: absolute;
    top: 50%;
    left: 70rpx;
    transform: translateY(-50%);
    font-size: 30rpx;
}

.answer .btn_group .btn_container #options.check {
    color: #fff;
}

.answer .desc-group {
    position: relative;
    padding: 40rpx 0;
    margin: 0 auto;
    height: 520rpx;
}

.answer .desc-group .tobottom {
    position: absolute;
    bottom: 10rpx;
    left: 50%;
    transform: translateX(-50%);
    width: 76rpx;
    height: 76rpx;
}

.answer .desc-group .about_item {
    padding-right: 60rpx;
    display: -webkit-box;
    display: flex;
    display: -webkit-flex;
    margin-top: 50rpx;
    justify-content: space-around;
    font-size: 34rpx;
    color: #554C44;
}

.answer .desc-group .about_item .icon {
    margin: 16rpx 40rpx 0;
    width: 14rpx;
    height: 14rpx;
    background: #5FBFFB;
    border-radius: 50%;
}

.answer .desc-group .about_item .icon.green {
    background: #44D878;
}

.answer .desc-group .about_item .icon.red {
    background: #FF5E77;
}

.answer .desc-group .about_item .icon.blue {
    background: #5FBFFB;
}

.answer .desc-group .about_item .paragraph {
    -webkit-box-flex: 1;
    flex: 1;
}

.answer .desc-group .about_item .paragraph .title {
    color: #554C44;
    font-size: 28rpx;
    margin-bottom: 15rpx;
}

.answer .desc-group .about_item .paragraph .b {
    font-size: 30rpx;
    color: #322A22;
}

.answer .desc-group .about_item .paragraph .desc {
    opacity: .6;
    font-size: 28rpx;
    color: #554C44;
    margin-top: 10rpx;
}

.nosure {
    position: relative;
    width: 630rpx;
    height: 100rpx;
    border-radius: 100rpx;
    box-shadow: 0 2rpx 16rpx 0 rgba(210,210,210,0.6);
    background: #fff;
    font-size: 30rpx;
    color: #554C44;
    text-indent: 160rpx;
    text-align: left;
    line-height: 100rpx;
    box-sizing: border-box;
}

.nosure::after {
    border: none;
}

.nosure.select {
    color: #fff;
    background-image: linear-gradient(135deg,#FFE00C 0,#FFD100 100%);
}

.nosure.selectContinue {
    color: #fff;
    background-image: linear-gradient(135deg,#FFE00C 0,#FFD100 100%);
}

.nosure .time {
    position: absolute;
    font-size: 30rpx;
    right: 45rpx;
    top: 50%;
    transform: translateY(-50%);
    color: #44D878;
    font-weight: bold;
}

.circle-container {
    width: 36rpx;
    height: 36rpx;
    border-radius: 50%;
    border: 8rpx solid #44D878;
    box-sizing: border-box;
    position: absolute;
    top: 31rpx;
    left: 83rpx;
}

#cir {
    top: 31rpx;
    left: 83rpx;
    box-sizing: border-box;
    position: absolute;
    width: 36rpx;
    height: 36rpx;
    border-radius: 50%;
    border: 8rpx solid #F0F0F0;
}

.left {
    clip: rect(0,18rpx,36rpx,0);
}

.right {
    clip: rect(0,36rpx,36rpx,18rpx);
}

.stable-right {
    width: 36rpx;
    height: 36rpx;
    border-radius: 50%;
    border: 8rpx solid #44D878;
    position: absolute;
    top: 31rpx;
    left: 83rpx;
    box-sizing: border-box;
    clip: rect(0,36rpx,36rpx,18rpx);
}

.warn-style {
    color: #FF536E;
}
</style>
