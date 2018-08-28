<script>
export default {
  created () {
    // 调用API从本地缓存中获取数据
    const logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    // console.log('app created and cache logs by setStorageSync')
  }
}
</script>

<style>
.main-bg {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 750rpx;
    height: 1214rpx;
    z-index: -1;
}
</style>
