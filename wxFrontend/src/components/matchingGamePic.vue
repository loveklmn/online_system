<template>
  <div class="pic_block">
    <img
      class="pic"
      :src="src"
      />
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      selected: false
    }
  },
  props: ['src'],
  methods: {
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
.pic_block {
  width: 100%;
  margin: auto;
  padding: auto;
}
</style>
