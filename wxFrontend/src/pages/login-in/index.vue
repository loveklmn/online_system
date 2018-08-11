<template>
  <div>
    <button class="login" @click="login"> login </button>
  </div>
</template>

<script>
export default {
  data () {
    return {}
  },

  methods: {
    login () {
      // implement verification
      // if passed
      wx.switchTab({
        url: '/pages/index/main'
      })
    }
  },

  created () {}
}
</script>

<style scoped>
.login {
  margin-top : 100%
}
</style>
