<template>
<div>
  <a class="float">
    <router-link :to="backRoute">
      <i class="fa fa-envelope my-float">{{ backName }}</i>
    </router-link>
  </a>
</div>
</template>
<script>
export default {
  name: 'backhomeBtn',
  props: {
    back: {
      type: String,
      default: ''
    },
    name: {
      type: String,
      default: ''
    }
  },
  data () {
    return {
      backRoute: '',
      backName: ''
    }
  },
  created () {
    this.backRoute = this.back
    this.backName = this.name
  }
}
</script>
<style scoped>
.float{
  position:fixed;
  width:60px;
  height:60px;
  bottom:40px;
  right:40px;
  background-color:#47494c;
  color:#FFF;
  border-radius:50px;
  text-align:center;
  box-shadow: 2px 2px 3px #999;
  padding-top: 21px;
}

.my-float{
  font-size: 10px;
  margin-top:18px;
  color: white;
}

</style>
