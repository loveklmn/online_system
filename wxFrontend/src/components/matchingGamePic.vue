<template>
  <div class="pic_block" >
    <img
      :class="getclass"
      :src="src"
      v-on:click="select"
      />
  </div>
</template>

<script>
export default {
  data: function () {
    return {
    }
  },
  computed: {
    getclass: function () {
      return this.selected ? 'pic_selected' : 'pic'
    }
  },
  props: ['id', 'src', 'value', 'inmatch', 'selected'],
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
.pic_selected {
  width: 180rpx;
  height: 180rpx;
  margin: 10rpx;
  padding: 0;
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
