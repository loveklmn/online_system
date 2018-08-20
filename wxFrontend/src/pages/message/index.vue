<template>
  <div>
    <div
      v-for="y in x"
      :key="index"
      class="card">
      <i-card :title="y.created_time">
        <view slot="content">{{y.content}}</view>
      </i-card>
    </div>

  </div>
</template>

<script>
export default {
  data () {
    return {
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

  methods: {},

  created () {}
}
</script>

<style scoped>
.card {
  border: 2rpx solid #AAAAAA;
  width: 90%;
  margin: 30rpx auto;
}
</style>
