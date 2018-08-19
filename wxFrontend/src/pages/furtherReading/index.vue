<template>
  <div class="weui-article">
    <div>
      <wxParse :content="assignment" />
    </div>
    <div class="weui-uploader__title">编辑作业</div>
    <textarea v-model.lazy="homework.content" placeholder="请输入作业内容" />
    <div class="weui-uploader">
      <div class="weui-uploader__hd">
        <div class="weui-uploader__title">图片上传</div>
        <div class="weui-uploader__info">{{homework.attachments.image.length}}/9</div>
      </div>
      <div class="weui-uploader__bd">
        <div class="weui-uploader__files" id="uploaderFiles">
          <div v-for="item in previewImages" :key="item">
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
    <div class="submit-button">
      <i-alert type="error" v-if="full === true">
        已经不能再上传了哦
        <view slot="desc">您最多上传9张图片</view>
      </i-alert>
      <i-button type="success" @click="submit" long="true">提交</i-button>
    </div>
  </div>
</template>

<script>
import wxParse from 'mpvue-wxparse'
import request from '@/utils/request'

export default {
  components: {
    wxParse
  },
  data () {
    return {
      previewImages: [],
      id: null,
      full: null,
      assignment: null,
      homework: {
        content: '',
        attachments: {
          audio: [],
          video: [],
          image: []
        }
      },
      submitted: false
    }
  },
  onLoad (options) {
    this.id = options.id
    let url = 'books/' + this.id + '/homework/'
    request.get(url).then((res) => {
      if (res.statusCode === 200) {
        this.assignment = res.data.assignment || '<h1>本书无阅读拓展</h1>'
        if (res.data.homework && res.data.homework.content !== undefined) {
          this.homework = res.data.homework
          this.submitted = true
        }
      } else {
        console.log('请求错误')
      }
    }).catch((err) => {
      console.log(err)
    })
  },
  onShow () {
  },
  methods: {
    chooseImage (e) {
      let vm = this
      if (vm.homework.attachments.image.length === 9) {
        this.full = true
        return
      }
      wx.chooseImage({
        count: 9,
        sizeType: ['original', 'compressed'],
        sourceType: ['album', 'camera'],
        success: function (res) {
          for (let i = 0; i < res.tempFilePaths.length; i++) {
            let currentFile = res.tempFilePaths[i]
            request.upload(currentFile).then((url) => {
              console.log(url)
              vm.homework.attachments.image.push(url)
              vm.previewImages.push(request.baseURL + url)
            })
          }
        },
        fail: function () {
        },
        complete: function () {
        }
      })
    },
    predivImage (e) {
      console.log(e)
      wx.previewImage({
        current: e.currentTarget.id, // 当前显示图片的http链接
        urls: this.previewImages // 需要预览的图片http链接列表
      })
    },
    deleteImg (e) {
      let url = e.currentTarget.id
      let index = this.previewImages.indexOf(url)
      this.previewImages.splice(index, 1)
      this.homework.attachments.image.splice(index, 1)
    },
    submit () {
      console.log(this.homework)
      let url = 'books/' + this.id + '/homework/'
      request.post(url, this.homework).then((res) => {
        console.log(res)
        this.submitted = true
      })
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

.homework_text {
  height: 30px;
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
