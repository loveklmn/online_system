<template>
<div>
  <div v-if="src !== null" class="pic_block">
    <img
      :class="getimgclass"
      :src="src"
      v-on:click="select"
      />
  </div>
  <div v-else class="pic_block">
    <p
      :class="getpclass"
      v-on:click="select">{{word}}</p>
  </div>
</div>
</template>

<script>
export default {
  data: function () {
    return {
    }
  },
  computed: {
    getimgclass: function () {
      return this.selected ? 'pic-selected' : 'pic'
    },
    getpclass: function () {
      return this.selected ? 'word-selected' : 'word'
    }
  },
  props: ['id', 'src', 'word', 'value', 'inmatch', 'selected'],
  methods: {
    select: function (event) {
      if (!this.inmatch) {
        this.$emit('isselect', this.id)
      }
    }
  }
}
</script>

<style>
.pic {
  display: block;
  width: 200rpx;
  height: 200rpx;
  margin: auto;
  padding: auto;
}
.pic-selected {
  width: 180rpx;
  height: 180rpx;
  margin: 10rpx;
  padding: 0;
  float: center;
  border: 2rpx solid #dddddd;
  border-radius: 15rpx;
  box-shadow: 8rpx 2rpx 2rpx #cccccc;
}
.word {
  height: 33%;
  display: block;
  margin: auto;
  padding: 10rpx;
}
.word-selected {
  height: 33%;
  padding: 10rpx;
  float: center;
  border: 2rpx solid #dddddd;
  border-radius: 15rpx;
  box-shadow: 8rpx 2rpx 2rpx #cccccc;
}
.pic_block {
  width: 100%;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-around;
}
</style>
