<template>
  <div>
    <div
      v-for="y in x"
      :key="index"
      class="card">
      <i-card :title="y.title">
        <view slot="content">{{y.content}}</view>
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
      theData: null,
      x: [
        {
          id: 1,
          content: '今天不上课',
          have_read: false,
          created_time: '一年前'
        },
        {
          id: 2,
          content: '今天停电',
          have_read: true,
          created_time: '今天'
        }
      ]
    }
  },
  methods: {
    getData () {
      let url = 'notices/'
      request.get(url)
        .then((res) => {
          console.log(res.data)
          this.theData = res.data
        }).catch((err) => {
          console.log(err)
        })
    }
  },
  onLoad () {
    this.getData()
    this.x.forEach((item) => {
      item.title = formatFullTime(item.created_time)
    })
    console.log(this.x)
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
