<template lang="html">
  <div class="content">

    <div class="list-header">
      <img class="avatar" v-if="x.author" :src="serverLink + x.author.avatar">
      <div class="user-info">
        <p class="user-name" v-if="x.author">{{x.author.username}}<br><p class="title">Ta读了:《{{x.book.title}}》</p></p>
        <div class="list-content">
      <span class="content-text">{{x.content}}</span>
      <div  class="content-img">
        <ul  class="content-img-ul clear-fix">
          <li
            v-for="y in x.attactments.image"
            :key="index"
            class="img-li-default"
            :class= "imgClass">
            <img
              class="img-div"
              :src="serverLink + y"
              @click="predivImage"
              ></img>
          </li>
        </ul>
      </div>
    </div>
      </div>
      <span class="user-time">{{getTime}}</span>
    </div>
    

    <div class="list-footer">
      <div class="footer-tag">
        <img class="footer-icon" :src="getIconSrc" @click="praise"></img>
        <span class="tag-style">{{x.vote_count}}</span>
      </div>
    </div>
  </div>
</template>

<script>
import { formatYMD } from '@/utils/index'
import request from '@/utils/request'
export default {
  data () {
    return {
      previewImages: []
    }
  },
  props: ['x'],
  computed: {
    serverLink: function () {
      return request.baseURL.slice(0, -5)
    },
    getIconSrc () {
      let path = '/static/images/friendCircle/'
      let pic = this.x.action.liked ? 'heart-active.png' : 'heart-default.png'
      return path + pic
    },
    imgClass () {
      let size = this.x.attactments.image.length
      let clazz = ''
      switch (size) {
        case 1:
          clazz = 'img-li-one'
          break
        case 2:
        case 4:
          clazz = 'img-li-two'
          break
        default:
          clazz = 'img-li-other'
          break
      }
      return clazz
    },
    getTime () {
      return formatYMD(this.x.created_time)
    }
  },
  methods: {
    getFullUrl (y) {
      return request.baseURL + y
    },
    predivImage (e) {
      wx.previewImage({
        current: e.currentTarget.id, // 当前显示图片的http链接
        urls: this.previewImages // 需要预览的图片http链接列表
      })
    },
    praise () {
      this.x.action.liked = !this.x.action.liked
      if (this.x.action.liked) {
        this.x.vote_count += 1
      } else {
        this.x.vote_count -= 1
      }
      let url = 'community/' + this.x.id + '/like/'
      request.post(url, {id: this.x.id})
    }
  },
  mounted () {
    this.x.attactments.image.forEach(element => {
      this.previewImages.push(this.getFullUrl(element))
    })
  }
}
</script>

<style>
p {
  font-size: 14px;
}

a {
    color: #007AFF;
}

.content {
    margin: 30rpx;
}

.content .list-header {
    width: 100%;
    height: 100%;
    display: flex;
    flex-flow: row;
}

.content .list-footer {
    width: 29%;
    margin-bottom: 35rpx;
    color: #cdcdcd;
    display: flex;
    flex-flow: row;
    float: right;
}

.content .list-footer .footer-tag {
    width: 49.8%;
    height: 65rpx;
    color: inherit;
    margin-left: 10rpx;
}

.content .list-footer .footer-tag .tag-style {
    margin-left: 15rpx;
    margin-top: 5rpx;
    font-size: 35rpx;
    color: black;
}

.avatar {
    width: 80rpx;
    height: 80rpx;
    border-radius: 50%;
    border: 1rpx solid rgba(0, 0, 0, .05);
}

.content .user-info {
    margin-left: 20rpx;
    display: flex;
    flex-flow: column;
    margin-right: 20rpx;
    flex: 1;
}

.content .user-time {
    font-size: 30rpx;
    color: #A4A8AC;
    height: 100%;
    display: table-cell
}

.content .user-info .user-name {
    margin: 0;
    flex: 1;
    font-size: 40rpx;
}

.book-name {
    padding: 10rpx;
    margin: 5rpx;
    flex: 1;
    font-size: 30rpx;
    float: right;
}

.content .list-content {
    margin-top: 35rpx;
}

.content .list-content .content-text {
    font-size: 15px;
    line-height: 50rpx;
    padding-right: 120rpx;
}

.content .list-content .content-at {
    color: #007AFF;
}

.clear-fix::after {
    content: '';
    display: block;
    clear: both;
}

.content .list-content .content-img .content-img-ul {
    margin: 0;
    padding: 0;
    list-style: none;
}

.content-img .content-img-ul .img-li-default {
    float: left;
    height: 0;
    margin-top: 20rpx;
    margin-right: 20rpx;
}

.content-img .content-img-ul .img-li-one {
    width: 52%;
    padding-bottom: 35%;
}

.content-img .content-img-ul .img-li-two {
    /* width: 43%;
    padding-bottom: 43%; */
    width: 160rpx;
    height: 160rpx;
    margin: 5rpx;
}

.content-img .content-img-ul .img-li-other {
    /* width: 28%; */
    width: 160rpx;
    height: 160rpx;
    margin: 5rpx;
}

.content-img .content-img-ul .img-div {
    width: 160rpx;
    height: 160rpx;
    background-position: center;
    background-repeat: no-repeat;
}

.content .list-content .content-re-content {
    width: 100%;
    margin-top: 35rpx;
    border: 1rpx solid rgba(0, 0, 0, .05);
    border-radius: 3rpx;
    background-color: #f5f5f5;
    padding: 25rpx;
}

.content .list-content .content-re-content .re-content-text {
    font-size: 14px;
    line-height: 50rpx;
}

.footer-icon {
    margin-top: 10rpx;
    height: 40rpx;
    width: 40rpx;
}
.line {
  margin: 0 auto;
  margin-top: 70rpx;
  width: 95%;
  height: 2rpx;
  background-color: #888888;
}
.title {
  font-size:14px;
}
</style>
