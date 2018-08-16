<template>
  <div class="weui-article">
    <div>
      <wxParse :content="article" />
    </div>
    <!-- <div class="page__bd">
        <div class="weui-article">
            <div class="weui-article__h1">阅读拓展</div>
            <div class="weui-article__section">
                <div class="weui-article__title">文本作业描述</div>
                <div class="weui-article__section">
                    <div class="weui-article__p">
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
                        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
                        consequat.
                    </div>
                    <div class="weui-article__p">
                        <image class="weui-article__img" src="https://i.loli.net/2018/08/14/5b727adea773a.png" mode="aspectFit" style="height: 180px" />
                        <image class="weui-article__img" src="https://i.loli.net/2018/08/14/5b727adea773a.png" mode="aspectFit" style="height: 180px" />
                    </div>
                </div>
            </div>
        </div>
    </div> -->
    <div class="weui-uploader">
              <div class="weui-uploader__hd">
                <div class="weui-uploader__title">图片上传</div>
                <div class="weui-uploader__info">{{files.length}}/9</div>
              </div>
              <div class="weui-uploader__bd" >
                <div class="weui-uploader__files" id="uploaderFiles">
                  <div v-for="(item ,index) in files" :key="index">
                    <div class="weui-uploader__file">
                      <image class="weui-uploader__img" :src="item" mode="aspectFill" @click="predivImage" :id="item" />
                      <div class="delete-icon" @click="deleteImg" :id="item"></div>
                    </div>
                  </div>  
                </div>
                <div class="weui-uploader__input-box">
                  <div class="weui-uploader__input" @click="chooseImage"></div>
                </div>
              </div>
            </div>
            <div class="submit-button" >
            <i-alert type="error" v-if="full === true">
    已经不能再上传了哦
    <view slot="desc">您最多上传9张图片</view>
</i-alert>
    <i-button type="success" @click="1" long="true">提交</i-button>
    </div>
  </div>
</template>

<script>
import wxParse from 'mpvue-wxparse'

export default {
  components: {
    wxParse
  },
  data () {
    return {
      files: [],
      id: null,
      full: null,
      article: '<div><h1>Draw a cat.</h1><p>homework: Cat is cute.Draw a cat like this.</p></div><img class="weui-article__img" src="https://i.loli.net/2018/08/14/5b727adea773a.png"/>'
    }
  },
  onLoad (options) {
    this.id = options.id
  },
  methods: {
    chooseImage (e) {
      let _this = this
      if (_this.files.length === 9) {
        this.full = true
        return
      }
      wx.chooseImage({
        count: 1, // 默认9
        sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
        sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
        success: function (res) {
          // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
          _this.files = _this.files.concat(res.tempFilePaths)
        },
        fail: function () {
          // console.log('fail')
        },
        complete: function () {
        }
      })
    },
    predivImage (e) {
      console.log(e)
      wx.previewImage({
        current: e.currentTarget.id, // 当前显示图片的http链接
        urls: this.files // 需要预览的图片http链接列表
      })
    },
    deleteImg (e) {
      Array.prototype.indexOf = function(val) { // eslint-disable-line
        for (let i = 0; i < this.length; i++) {
          if (this[i] === val) return i
        }
        return -1
      }
      Array.prototype.remove = function (val) { // eslint-disable-line
        let index = this.indexOf(val)
        if (index > -1) {
          this.splice(index, 1)
        }
      }
      this.files.remove(e.currentTarget.id)
    }
  }
}
</script>

<style scoped>
@import url("~mpvue-wxparse/src/wxParse.css");
page {
    background-color: #F8F8F8;
    font-size: 16px;
    font-family: -apple-system-font, Helvetica Neue, Helvetica, sans-serif;
}

.submit-button{
  clear:both;
  padding : 20rpx 10rpx;
}

.page__hd {
    padding: 40px;
}

.page__bd {
    padding-bottom: 40px;
}

.page__bd_spacing {
    padding-left: 15px;
    padding-right: 15px;
}

.page__ft {
    padding-bottom: 10px;
    text-align: center;
}

.page__title {
    text-align: left;
    font-size: 20px;
    font-weight: 400;
}

.page__desc {
    margin-top: 5px;
    color: #888888;
    text-align: left;
    font-size: 14px;
}


.weui-article {
  padding: 20px 15px;
  font-size: 15px;
}

.weui-article__section {
  margin-bottom: 1.5em;
}

.weui-article__h1 {
  font-size: 18px;
  font-weight: 400;
  margin-bottom: 0.9em;
}

.weui-article__h2 {
  font-size: 16px;
  font-weight: 400;
  margin-bottom: 0.34em;
}

.weui-article__h3 {
  font-weight: 400;
  font-size: 15px;
  margin-bottom: 0.34em;
}

.weui-article__p {
  margin: 0 0 0.8em;
}



.weui-uploader__hd {
  display: -webkit-box;
  display: -webkit-flex;
  display: flex;
  padding-bottom: 10px;
  -webkit-box-align: center;
  -webkit-align-items: center;
  align-items: center;
}

.weui-uploader__title {
  -webkit-box-flex: 1;
  -webkit-flex: 1;
  flex: 1;
}

.weui-uploader__info {
  color: #b2b2b2;
}

.weui-uploader__bd {
  margin-bottom: -4px;
  margin-right: -9px;
  overflow: hidden;
}

.weui-uploader__file {
  float: left;
  margin-right: 9px;
  margin-bottom: 9px;
}

.weui-uploader__img {
  display: block;
  width: 79px;
  height: 79px;
}

.weui-uploader__file_status {
  position: relative;
}

.weui-uploader__file_status:before {
  content: " ";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.5);
}

.weui-uploader__file-content {
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  color: #fff;
}

.weui-uploader__input-box {
  float: left;
  position: relative;
  margin-right: 9px;
  margin-bottom: 9px;
  width: 77px;
  height: 77px;
  border: 1px solid #d9d9d9;
}

.weui-uploader__input-box:after,
.weui-uploader__input-box:before {
  content: " ";
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  background-color: #d9d9d9;
}

.weui-uploader__input-box:before {
  width: 2px;
  height: 39.5px;
}

.weui-uploader__input-box:after {
  width: 39.5px;
  height: 2px;
}

.weui-uploader__input-box:active {
  border-color: #999;
}

.weui-uploader__input-box:active:after,
.weui-uploader__input-box:active:before {
  background-color: #999;
}

.weui-uploader__input {
  position: absolute;
  z-index: 1;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
}

.weui-uploader__file {
  position: relative;
}
.weui-uploader__bd {
  overflow: visible;
}
.delete-icon {
  display: block;
  position: absolute;
  width: 40rpx;
  height: 40rpx;
  background: #f43530;
  right: 0;
  top: -20rpx;
  border-radius: 40rpx;
  z-index: 5;
}
.delete-icon::before {
  display: block;
  content: '';
  width: 26rpx;
  height: 4rpx;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #fff;
}

</style>
