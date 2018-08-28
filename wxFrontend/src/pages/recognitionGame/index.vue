<template>
  <div>
    <div class="answer">
      <toast :message="msg" :visible.sync="visible"></toast>
      <div class="word">
        <img :src="rimg" />
      </div>
      <div class="btn_group">
        <div class="btn_container">
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
        </div>
      </div>
    </div>
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
    right: 0;
    bottom: 0;
    left: 0;
    z-index: 20;
    background: rgba(0,0,0,0.2);
}

.auth .modal_IOS {
    position: absolute;
    top: 50%;
    left: 50%;
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    width: 620rpx;
    height: 516rpx;
    margin-top: -358rpx;
    margin-left: -310rpx;
    background: #fff;
    border-radius: 10rpx;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -webkit-box-pack: justify;
    -webkit-box-align: center;
}

.auth .modal_IOS .title {
    box-sizing: border-box;
    width: 100%;
    height: 98rpx;
    font-size: 36rpx;
    font-weight: bold;
    line-height: 98rpx;
    color: #000;
    text-align: center;
    letter-spacing: 1.8rpx;
    border-bottom: 1rpx solid #C7C6C8;
}

.auth .modal_IOS image {
    width: 70rpx;
    height: 70rpx;
    margin-top: 35rpx;
}

.auth .modal_IOS .des {
    box-sizing: border-box;
    width: 500rpx;
    height: 97rpx;
    font-size: 30rpx;
    line-height: 97rpx;
    color: #000;
    border-bottom: 1rpx solid #DADADA;
}

.auth .modal_IOS .con {
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
    flex: 1;
    width: 500rpx;
    margin-top: 35rpx;
    font-size: 28rpx;
    color: #888888;
    text-align: center;
    -webkit-box-flex: 1;
}

.auth .modal_IOS .con::before {
    display: block;
    width: 10rpx;
    height: 10rpx;
    margin: 14rpx 19rpx 0 0;
    content: '';
    background: #888;
    border-radius: 50%;
}

.auth .modal_IOS .operator {
    box-sizing: border-box;
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
    width: 100%;
    height: 88rpx;
    margin-bottom: 0;
    font-size: 34rpx;
    color: #000;
    border-top: 1rpx solid #CAC9CB;
}

.auth .modal_IOS .operator .refuse {
    flex: 1;
    height: 100%;
    line-height: 86rpx;
    text-align: center;
    -webkit-box-flex: 1;
}

.auth .modal_IOS .operator .agree {
    box-sizing: border-box;
    flex: 1;
    height: 100%;
    line-height: 86rpx;
    color: #2FB922;
    text-align: center;
    border-left: 1rpx solid #CAC9CB;
    -webkit-box-flex: 1;
}

.auth .modal {
    position: absolute;
    top: 50%;
    left: 50%;
    box-sizing: border-box;
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 550rpx;
    height: 490rpx;
    padding: 60rpx 50rpx 50rpx 50rpx;
    margin-top: -245rpx;
    margin-left: -285rpx;
    background: #fff;
    border-radius: 3rpx;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -webkit-box-pack: justify;
}

.auth .modal .title {
    font-size: 38rpx;
    font-weight: bold;
    color: #353535;
}

.auth .modal .wrap {
    box-sizing: border-box;
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
    align-items: center;
    height: 150rpx;
    border-bottom: 1rpx solid #DADADA;
    -webkit-box-align: center;
}

.auth .modal .wrap image {
    width: 80rpx;
    height: 80rpx;
}

.auth .modal .wrap .des {
    flex: 1;
    margin-left: 25rpx;
    font-size: 28rpx;
    color: #353535;
    letter-spacing: 1.4rpx;
    -webkit-box-flex: 1;
}

.auth .modal .con {
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
    flex: 1;
    margin-top: 40rpx;
    font-size: 28rpx;
    color: #888888;
    text-align: center;
    -webkit-box-flex: 1;
}

.auth .modal .con::before {
    display: block;
    width: 10rpx;
    height: 10rpx;
    margin: 14rpx 19rpx 0 0;
    content: '';
    background: #888;
    border-radius: 50%;
}

.auth .modal .operator {
    box-sizing: border-box;
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
    justify-content: flex-end;
    font-size: 28rpx;
    color: #000;
    -webkit-box-pack: end;
}

.auth .modal .operator .refuse {
    margin-right: 55rpx;
}

.auth .modal .operator .agree {
    margin-right: 20rpx;
    color: #2FB922;
}

.player .voice {
    position: relative;
    box-sizing: border-box;
    display: -webkit-box;
    display: flex;
    display: -webkit-flex;
    align-items: center;
    justify-content: center;
    width: 140rpx;
    height: 90rpx;
    margin: 0 auto;
    text-align: center;
    -webkit-box-align: center;
    -webkit-box-pack: center;
}

.player .voice image {
    width: 40rpx;
    height: 40rpx;
}

.horizon-progress .progress {
    position: relative;
    box-sizing: border-box;
    width: 630rpx;
    height: 16rpx;
    margin: 36rpx auto;
    background: #F6F6F6;
    border-radius: 100rpx;
}

.horizon-progress .progress .curr_progress {
    position: absolute;
    top: 50%;
    left: 0;
    height: 8rpx;
    background-image: linear-gradient(135deg,#FFD600 0,#FF702B 100%);
    border-radius: 100rpx;
    transform: translateY(-50%);
}

.warn-modal {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 11;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.16);
}

.warn-modal .modal {
    position: fixed;
    top: 330rpx;
    left: 50%;
    z-index: 3;
    width: 560rpx;
    height: 380rpx;
    background: #fff;
    border-radius: 8rpx;
    transform: translateX(-50%);
}

.warn-modal .modal .topnav {
    overflow: hidden;
    text-align: right;
}

.warn-modal .modal .topnav .close_container {
    box-sizing: border-box;
    float: right;
    width: 82rpx;
    height: 72rpx;
    padding-right: 31rpx;
}

.warn-modal .modal .topnav .close_container .close {
    display: none;
    width: 30rpx;
    height: 30rpx;
    margin-top: 30rpx;
}

.warn-modal .modal .rest {
    box-sizing: border-box;
    padding: 30rpx 47rpx;
}

.warn-modal .modal .rest .winner {
    display: block;
    width: 82rpx;
    height: 82rpx;
    margin: 0 auto;
}

.warn-modal .modal .rest .nickname {
    margin-top: 34rpx;
    font-size: 36rpx;
    color: #322A22;
    text-align: center;
}

.warn-modal .modal .rest .desc {
    margin-top: 30rpx;
    font-size: 30rpx;
    color: #B1A79D;
    text-align: center;
}

.warn-modal .modal .rest .introduce-item {
    box-sizing: border-box;
    display: -webkit-box;
    display: flex;
    display: -webkit-flex;
    padding: 0 40rpx;
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
    font-size: 30rpx;
    color: #322A20;
}

.warn-modal .modal .rest .introduce-item .introduce-container .introduce-desc {
    margin: 0;
    font-size: 24rpx;
    color: #B1A79C;
}

.warn-modal .modal .rest button {
    width: 240rpx;
    height: 90rpx;
    margin: 35rpx auto;
    font-size: 30rpx;
    line-height: 90rpx;
    color: #322A22;
    background: #FFD600;
    border-radius: 100rpx;
    box-shadow: 0 1rpx 15rpx 0 rgba(236,205,46,0.5);
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
    box-sizing: border-box;
    display: -webkit-box;
    display: flex;
    display: -webkit-flex;
    align-items: center;
    justify-content: flex-start;
    padding: 35rpx 53rpx;
    -webkit-box-pack: start;
    -webkit-box-align: center;
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
    z-index: 10;
    width: 100%;
    height: 100%;
    text-align: center;
    background: rgba(255,255,255,0);
}

.transparentmodal image {
    width: 180rpx;
    height: 180rpx;
    margin-top: 442rpx;
}

.answer .word {
    font-size: 80rpx;
    font-weight: bold;
    color: #322A22;
    text-align: center;
}

.answer .wordb {
    margin-bottom: 25rpx;
    font-size: 30rpx;
    font-weight: bold;
    color: #554C44;
    text-align: center;
}

.answer .btn_group {
    width: 630rpx;
    margin: 40rpx auto;
}

.answer .btn_group .btn_container {
    position: relative;
}

.answer .btn_group .btn_container button {
    box-sizing: border-box;
    width: 100%;
    height: 100rpx;
    margin-bottom: 40rpx;
    font-size: 30rpx;
    line-height: 100rpx;
    color: #554C44;
    text-align: left;
    text-indent: 126rpx;
    background: #fff;
    border-radius: 100rpx;
    box-shadow: 0 2rpx 16rpx 0 rgba(210,210,210,0.6);
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
    font-size: 30rpx;
    transform: translateY(-50%);
}

.answer .btn_group .btn_container #options.check {
    color: #fff;
}

.answer .desc-group {
    position: relative;
    height: 520rpx;
    padding: 40rpx 0;
    margin: 0 auto;
}

.answer .desc-group .tobottom {
    position: absolute;
    bottom: 10rpx;
    left: 50%;
    width: 76rpx;
    height: 76rpx;
    transform: translateX(-50%);
}

.answer .desc-group .about_item {
    display: -webkit-box;
    display: flex;
    display: -webkit-flex;
    justify-content: space-around;
    padding-right: 60rpx;
    margin-top: 50rpx;
    font-size: 34rpx;
    color: #554C44;
}

.answer .desc-group .about_item .icon {
    width: 14rpx;
    height: 14rpx;
    margin: 16rpx 40rpx 0;
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
    margin-bottom: 15rpx;
    font-size: 28rpx;
    color: #554C44;
}

.answer .desc-group .about_item .paragraph .b {
    font-size: 30rpx;
    color: #322A22;
}

.answer .desc-group .about_item .paragraph .desc {
    margin-top: 10rpx;
    font-size: 28rpx;
    color: #554C44;
    opacity: .6;
}

.nosure {
    position: relative;
    box-sizing: border-box;
    width: 630rpx;
    height: 100rpx;
    font-size: 30rpx;
    line-height: 100rpx;
    color: #554C44;
    text-align: left;
    text-indent: 160rpx;
    background: #fff;
    border-radius: 100rpx;
    box-shadow: 0 2rpx 16rpx 0 rgba(210,210,210,0.6);
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
    top: 50%;
    right: 45rpx;
    font-size: 30rpx;
    font-weight: bold;
    color: #44D878;
    transform: translateY(-50%);
}

.circle-container {
    position: absolute;
    top: 31rpx;
    left: 83rpx;
    box-sizing: border-box;
    width: 36rpx;
    height: 36rpx;
    border: 8rpx solid #44D878;
    border-radius: 50%;
}

#cir {
    position: absolute;
    top: 31rpx;
    left: 83rpx;
    box-sizing: border-box;
    width: 36rpx;
    height: 36rpx;
    border: 8rpx solid #F0F0F0;
    border-radius: 50%;
}

.left {
    clip: rect(0,18rpx,36rpx,0);
}

.right {
    clip: rect(0,36rpx,36rpx,18rpx);
}

.stable-right {
    position: absolute;
    top: 31rpx;
    left: 83rpx;
    box-sizing: border-box;
    width: 36rpx;
    height: 36rpx;
    clip: rect(0,36rpx,36rpx,18rpx);
    border: 8rpx solid #44D878;
    border-radius: 50%;
}

.warn-style {
    color: #FF536E;
}
</style>
