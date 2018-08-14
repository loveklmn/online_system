<template>
<div>
 
    <image class="weui-grid__icon" :src="src" />
    <div class="weui-grid__label"> {{name}} </div>
    <div class="weui-grid__label"> bookid: {{id}} </div>

<i-button bind:click="handleClick" shape="circle" type="info">亲子阅读指导</i-button>
<i-button bind:click="handleClick" shape="circle" type="success">E-book</i-button>
<i-button bind:click="handleClick" shape="circle" type="warning">课后练习</i-button>
<i-button bind:click="handleClick" shape="circle" type="error">阅读拓展</i-button>

  </div>
</template>

<script>

export default {
  components: {
  },

  data () {
    return {
      id: null,
      name: null,
      src: null
    }
  },

  created () {

  },
  onLoad (options) {
    this.id = options.id
    this.name = options.name
    this.src = options.src
  }
}
</script>

<style>
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
