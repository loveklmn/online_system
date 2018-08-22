<template>
  <div>
    <div
      v-for="(notice,index) in reverse" :key="index" class="card" @click="read(notice)">
      <i-card :title="notice.title">
        <view slot="content">{{notice.content}}</view>
      </i-card>
    </div>
  </div>
</template>

<script>
import { formatFullTime } from '@/utils/index'
import request from '@/utils/request'
export default {
  data () {
    return {
      notices: null
    }
  },
  computed: {
    reverse () {
      if (this.notices !== null) {
        return this.notices.reverse()
      }
    }
  },
  methods: {
    getData () {
      let url = 'notices/'
      request.get(url)
        .then((res) => {
          this.notices = res.data
          this.notices.forEach((item) => {
            item.title = formatFullTime(item.created_time) + this.haveRead(item.have_read)
          })
        })
    },
    haveRead (flag) {
      return flag ? '(已读)' : ''
    },
    read (notice) {
      let url = 'notices/readed/'
      let that = this
      request.post(url, {id: notice.id})
        .then((res) => {
          notice.have_read = true
          notice.title = formatFullTime(notice.created_time) + that.haveRead(notice.have_read)
        })
    }
  },
  onLoad () {
    this.getData()
  },
  created () {}
}
</script>

<style scoped>
.card {
    border: 2rpx solid #ffffff;
    border-radius: 15rpx;
    background-color: #ffffff;
    box-shadow: 8rpx 2rpx 2rpx #cccccc;
    margin: 20rpx;
    position: relative;
}
</style>
