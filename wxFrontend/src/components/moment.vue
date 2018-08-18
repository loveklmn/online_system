<template lang="html">
  <div class="content">

    <div class="list-header">
      <img class="avatar" v-if="x.author" :src="x.author.avatar">
      <div class="user-info">
        <h3 class="user-name" v-if="x.author">{{x.author.username}}</h3>
      </div>
      <span class="user-time">{{x.created_time}}</span>
    </div>

    <div class="list-header">
      <h3 class="book-name">Ta读了：《{{x.book.title}}》</h3>
    </div>

    <div class="list-content">
      <span class="content-text">{{x.content}}</span>
      <div  class="content-img">
        <ul  class="content-img-ul clear-fix">
          <li
            v-for="y in x.attachments.image"
            :key="index"
            class="img-li-default"
            :class= "imgClass">
            <img
              class="img-div"
              :src="y"
              ></img>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
 
<script>
export default {
  data () {
    return {
    }
  },
  props: ['x'],
  computed: {
    imgClass () {
      let size = this.x.attachments.image.length
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
    }
  },
  mounted () {
    // console.log(this.x.attachments.pic_urls)
  }
}
</script>
 
<style>
a {
    color: #007AFF;
}

.content {
    margin: 40rpx;
}

.content .list-header {
    width: 100%;
    height: 100%;
    display: flex;
    flex-flow: row;
}

.content .list-footer {
    width: 68%;
    margin-top: 35rpx;
    color: #cdcdcd;
    display: flex;
    flex-flow: row;
}

.content .list-footer .footer-tag {
    width: 100%;
    height: 65rpx;
    color: inherit;
}

.content .list-footer .footer-tag .tag-style {
    font-size: 12rpx;
}

.avatar {
    width: 150rpx;
    height: 150rpx;
    border-radius: 50%;
    border: 1rpx solid rgba(0, 0, 0, .05);
}

.content .user-info {
    margin-left: 50rpx;
    display: flex;
    flex-flow: column;
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
}

.content .list-content {
    margin-top: 35rpx;
}

.content .list-content .content-text {
    font-size: 40rpx;
    line-height: 50rpx;
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
    padding-bottom: 52%;
}

.content-img .content-img-ul .img-li-two {
    /* width: 43%;
    padding-bottom: 43%; */
    width: 200rpx;
    height: 200rpx;
    margin: 10rpx;
}

.content-img .content-img-ul .img-li-other {
    /* width: 28%; */
    width: 200rpx;
    height: 200rpx;
    margin: 10rpx;
}

.content-img .content-img-ul .img-div {
    width: 200rpx;
    height: 200rpx;
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
    font-size: 65rpx;
    line-height: 50rpx;
}
</style>