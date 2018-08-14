<template>
  <div>
    readingGuide page
    <div class="weui-grid__label"> bookid: {{id}} </div>
  </div>
</template>

<script>

export default {
  components: {
  },
  methods: {

  },
  data () {
    return {
      id: null
    }
  },

  created () {

  },
  onLoad (options) {
    this.id = options.id
  }
}
</script>

<style scoped>
.weui-grid__icon {
  display: block;
  width: 170rpx;
  height: 240rpx;
  margin: 0 auto;
}

.weui-grid__label {
  margin-top: 5px;
  display: block;
  text-align: center;
  color: #000;
  font-size: 14px;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}
</style>
