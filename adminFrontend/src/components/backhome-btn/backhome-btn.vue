<template>
<div>
  <a class="float">
    <router-link to="/home">
      <i class="fa fa-envelope my-float">回首页</i>
    </router-link>
  </a>
</div>
</template>
<script>
export default {
  name: 'backhomeBtn'
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
