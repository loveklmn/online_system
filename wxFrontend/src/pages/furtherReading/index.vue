<template>
  <div class="weui-article">
    <div>
      <wxParse :content="assignment" />
    </div>
    <div v-if="!submitted" class="weui-uploader__title">编辑作业</div>
    <div v-else class="weui-uploader__title">已提交作业</div>
    <textarea v-if="!submitted" v-model.lazy="homework.content" :disabled="submitted" placeholder="请输入作业内容" />
    <div class="submitted_homework">
      <text v-if="submitted">{{homework.content}}</text>
    </div>
    <div class="weui-uploader">
      <div class="weui-uploader__hd" v-if="!submitted">
        <div class="weui-uploader__title">图片上传</div>
        <div class="weui-uploader__info">{{homework.attachments.image.length}}/9</div>
      </div>
      <div class="weui-uploader__bd">
        <div class="weui-uploader__files" id="uploaderFiles">
          <div v-for="item in previewImages" :key="item">
            <div class="weui-uploader__file">
              <image class="weui-uploader__img" :src="item" mode="aspectFill" @click="predivImage" :id="item" />
              <div class="delete-icon" v-if="!submitted" @click="deleteImg" :id="item"></div>
            </div>
          </div>
        </div>
        <div v-if="!submitted" class="weui-uploader__input-box">
          <div class="weui-uploader__input" @click="chooseImage"></div>
        </div>
      </div>
    </div>
    <div class="submit-button" v-if="!submitted">
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
        this.assignment = res.data.assignment
        if (res.data.homework && res.data.homework.content !== undefined) {
          this.homework = res.data.homework
          this.previewImages = this.homework.attachments.image.map(url => request.baseURL + url)
          this.submitted = true
        } else {
          this.previewImages = []
          this.homework = {
            content: '',
            attachments: {
              audio: [],
              video: [],
              image: []
            }
          }
          this.submitted = false
        }
      }
    })
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
        sizeType: ['compressed'],
        sourceType: ['album', 'camera'],
        success: function (res) {
          for (let i = 0; i < res.tempFilePaths.length; i++) {
            let currentFile = res.tempFilePaths[i]
            request.upload(currentFile).then((url) => {
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
      let vm = this
      if (this.content === '' || this.attachments === '') {
        return 0
      }
      let url = 'books/' + this.id + '/homework/'
      request.post(url, {
        content: this.homework.content,
        attachments: this.homework.attachments
      }).then((res) => {
        this.submitted = true
        wx.showModal({
          title: '您要打卡吗?',
          content: '您的作业将会出现在小伙伴中,您的书名将变为绿色',
          confirmText: '确定',
          cancelText: '取消',
          success: function (res) {
            if (res.confirm) {
              let url = 'community/'
              request.post(url, {book: vm.id}).then((res) => {
                if (res.statusCode === 201) {
                  wx.switchTab({ url: '/pages/friendCircle/main' })
                }
              })
            }
          }
        })
      })
    }
  }
}
</script>

<style scoped>
@import url("~mpvue-wxparse/src/wxParse.css");
page {
    font-family: -apple-system-font, Helvetica Neue, Helvetica, sans-serif;
    font-size: 16px;
    background-color: #F8F8F8;
}

.homework_text {
  height: 30px;
}

.submit-button{
  padding : 20rpx 10rpx;
  clear:both;
}

.page__hd {
    padding: 40px;
}

.page__bd {
    padding-bottom: 40px;
}

.page__bd_spacing {
    padding-right: 15px;
    padding-left: 15px;
}

.page__ft {
    padding-bottom: 10px;
    text-align: center;
}

.page__title {
    font-size: 20px;
    font-weight: 400;
    text-align: left;
}

.page__desc {
    margin-top: 5px;
    font-size: 14px;
    color: #888888;
    text-align: left;
}

.weui-article {
  padding: 20px 15px;
  font-size: 15px;
}

.weui-article__section {
  margin-bottom: 1.5em;
}

.weui-article__h1 {
  margin-bottom: 0.9em;
  font-size: 18px;
  font-weight: 400;
}

.weui-article__h2 {
  margin-bottom: 0.34em;
  font-size: 16px;
  font-weight: 400;
}

.submitted_homework {
  padding: 20rpx 0;
}

.weui-article__h3 {
  margin-bottom: 0.34em;
  font-size: 15px;
  font-weight: 400;
}

.weui-article__p {
  margin: 0 0 0.8em;
}

.weui-uploader__hd {
  display: -webkit-box;
  display: -webkit-flex;
  display: flex;
  -webkit-align-items: center;
  align-items: center;
  padding-bottom: 10px;
  -webkit-box-align: center;
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
  margin-right: -9px;
  margin-bottom: -4px;
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
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  content: " ";
  background-color: rgba(0, 0, 0, 0.5);
}

.weui-uploader__file-content {
  position: absolute;
  top: 50%;
  left: 50%;
  color: #fff;
  -webkit-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}

.weui-uploader__input-box {
  position: relative;
  float: left;
  width: 77px;
  height: 77px;
  margin-right: 9px;
  margin-bottom: 9px;
  border: 1px solid #d9d9d9;
}

.weui-uploader__input-box:after,
.weui-uploader__input-box:before {
  position: absolute;
  top: 50%;
  left: 50%;
  content: " ";
  background-color: #d9d9d9;
  -webkit-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
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
  top: 0;
  left: 0;
  z-index: 1;
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
  position: absolute;
  top: -20rpx;
  right: 0;
  z-index: 5;
  display: block;
  width: 40rpx;
  height: 40rpx;
  background: #f43530;
  border-radius: 40rpx;
}

.delete-icon::before {
  position: absolute;
  top: 50%;
  left: 50%;
  display: block;
  width: 26rpx;
  height: 4rpx;
  content: '';
  background: #fff;
  transform: translate(-50%, -50%);
}

</style>
