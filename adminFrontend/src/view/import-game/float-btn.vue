<template>
  <div>
    <a id="menu-share">
      <router-link class="float" :to="backRoute" id="menu-share">
        <i class="fa fa-share my-float">返回</i>
      </router-link>
    </a>
    <ul>
      <li>
        <router-link :to="assignmentRoute">
          <i class="fa fa-facebook my-float">阅读拓展</i>
        </router-link>
      </li>
      <li>
        <router-link :to="guidanceRoute">
          <i class="fa fa-google-plus my-float">亲子指导</i>
        </router-link>
      </li>
      <li>
        <router-link :to="ebookRoute">
          <i class="fa fa-twitter my-float">E-book</i>
        </router-link>
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  name: 'floatBtn',
  props: {
    back: {
      type: String,
      default: ``
    },
    assignment: {
      type: String,
      default: ``
    },
    guidance: {
      type: String,
      default: ``
    },
    ebook: {
      type: String,
      default: ``
    }
  },
  data () {
    return {
      backRoute: ``,
      assignmentRoute: ``,
      guidanceRoute: ``,
      ebookeRoute: ``
    }
  },
  created () {
    this.backRoute = this.back
    this.assignmentRoute = this.assignment
    this.guidanceRoute = this.guidance
    this.ebookRoute = this.ebook
  }
}
</script>
<style scoped>
.label-container{
  position:fixed;
  bottom:48px;
  right:105px;
  display:table;
  visibility: hidden;
}

.label-text{
  color:#FFF;
  background:rgba(51,51,51,0.5);
  display:table-cell;
  vertical-align:middle;
  padding:10px;
  border-radius:3px;
}

.label-arrow{
  display:table-cell;
  vertical-align:middle;
  color:#333;
  opacity:0.5;
}

.float{
  position:fixed;
  width:60px;
  height:60px;
  bottom:40px;
  right:40px;
  background-color:rgb(85, 86, 87);
  color:#FFF;
  border-radius:50px;
  text-align:center;
  box-shadow: 2px 2px 3px #999;
  z-index:1000;
  animation: bot-to-top 2s ease-out;
  padding-top: 21px;
}

ul{
  position:fixed;
  right:40px;
  padding-bottom:20px;
  bottom:80px;
  z-index:100;
}

ul li{
  list-style:none;
  margin-bottom:10px;
}

ul li a{
  background-color:#828488fc;
  color:#FFF;
  border-radius:50px;
  text-align:center;
  box-shadow: 2px 2px 3px #999;
  width:60px;
  height:60px;
  display:block;
  padding-top: 21px;
}

ul:hover{
  visibility:visible!important;
  opacity:1!important;
}

.my-float{
  font-size:10px;
  margin-top:100px;
  text-align: center;
}

a#menu-share + ul{
  visibility: hidden;
}

a#menu-share:hover + ul{
  visibility: visible;
  animation: scale-in 0.5s;
}

a#menu-share i{
  animation: rotate-in 0.5s;
}

a#menu-share:hover > i{
  animation: rotate-out 0.5s;
}

@keyframes bot-to-top {
    0%   {bottom:-40px}
    50%  {bottom:40px}
}

@keyframes scale-in {
    from {transform: scale(0);opacity: 0;}
    to {transform: scale(1);opacity: 1;}
}

@keyframes rotate-in {
    from {transform: rotate(0deg);}
    to {transform: rotate(360deg);}
}

@keyframes rotate-out {
    from {transform: rotate(360deg);}
    to {transform: rotate(0deg);}
}
</style>
