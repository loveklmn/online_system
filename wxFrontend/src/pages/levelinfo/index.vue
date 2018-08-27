
<template>
  <div class="container">
    <toast :message="msg" :visible.sync="visible"></toast>
    <div class="content">
    <i-cell-group>
        <i-panel title="您当前的等级为">
            <i-cell title=" K1" v-if="l1 === true">
                <i-switch :value="switch1" @click="onChange1" slot="footer"></i-switch>
            </i-cell>
            <i-cell title="K2" v-if="l2">
                <i-switch :value="switch2" @click="onChange2" slot="footer"></i-switch>
            </i-cell>
            <i-cell title="K3" v-if="l3">
                <i-switch :value="switch3" @click="onChange3" slot="footer"></i-switch>
            </i-cell>
            <i-cell title=" K4" v-if="l4">
                <i-switch :value="switch4" @click="onChange4" slot="footer"></i-switch>
            </i-cell>
        </i-panel>
    </i-cell-group>
    </div>
     <i-panel title="想解锁新等级?">
            <input v-if="!(l1 && l2 && l3 && l4)" v-model.trim="code" placeholder="请输入激活码" />
            <i-button type="info" @click="activate">确定</i-button>
            <p>想要了解<a href="../level/main">等级</a>?</p>
     </i-panel>


  </div>
</template>
<script>
import request from '@/utils/request'
import toast from 'mpvue-toast'
export default {
  data () {
    return {
      level: [],
      switch1: true,
      switch2: false,
      switch3: false,
      switch4: false,
      code: '',
      msg: '',
      visible: false
    }
  },
  components: {
    toast
  },
  computed: {
    l1: function () {
      return this.level.indexOf(1) !== -1
    },
    l2: function () {
      return this.level.indexOf(2) !== -1
    },
    l3: function () {
      return this.level.indexOf(3) !== -1
    },
    l4: function () {
      return this.level.indexOf(4) !== -1
    }
  },
  onShow () {
    this.getlevel()
  },
  methods: {
    setZero () {
      this.switch1 = false
      this.switch2 = false
      this.switch3 = false
      this.switch4 = false
    },
    onChange1 (e) {
      this.setZero()
      this.switch1 = !this.switch1
      let url = 'userinfo/level/'
      request.post(url, {level: 1})
    },
    onChange2 (e) {
      this.setZero()
      this.switch2 = !this.switch2
      let url = 'userinfo/level/'
      request.post(url, {level: 2})
    },
    onChange3 (e) {
      this.setZero()
      this.switch3 = !this.switch3
      let url = 'userinfo/level/'
      request.post(url, {level: 3})
    },
    onChange4 (e) {
      this.setZero()
      this.switch4 = !this.switch4
      let url = 'userinfo/level/'
      request.post(url, {level: 4})
    },
    setVisible () {
      this.visible = !this.visible
    },
    activate () {
      let vm = this
      let url = 'userinfo/level/update/'
      if (this.code !== '') {
        request
          .post(url, {code: this.code})
          .then(res => {
            console.log(res)
            if (res.data.level) {
              vm.msg = '你解锁了L' + res.data.level + '!'
              vm.setVisible()
              vm.getlevel()
            } else {
              vm.msg = res.data.msg
              vm.setVisible()
            }
          })
      } else {
        vm.msg = '请输入激活码哦'
        vm.setVisible()
      }
    },
    getlevel () {
      let url = 'userinfo/level/'
      request
        .get(url)
        .then(res => {
          console.log(res.data)
          if (res.data.length > 0) {
            this.level = res.data
          }
        })
    }
  }
}
</script>
<style>
page {
  padding-top: 60rpx;
}

.content {
  padding-bottom: 60rpx;
}

input {
  padding-left: 20rpx;
  margin-left: 10rpx;
  padding-top: 10rpx;
  padding-bottom: 10rpx;
  font-size: 14px;
}

p {
  font-size: 14px;
  display: flex;
  padding-left: 30rpx;
  line-height:1;
  color:#1c2438;
  padding-bottom: 1167rpx;
}

p>a {
  color: red;
}
img {
  width: 40%;
  height: 80%;
}

.intro{
  font-family: -apple-system-font,Helvetica Neue,Helvetica,sans-serif;
  text-align:justify;
}

.home_step{
  clear:both;
  margin-top:40rpx;
  padding-bottom: 100rpx;
}

.fsize24{
  text-align: right;
}

.step_k{
  margin-left: 30px;
  margin-right: 30px;
}

.step_info{
  border-radius: 6px;
  height: 250rpx;
  position: relative;
  width: 650rpx;
}

.step_k .step_info,.step_k .step_more span{
  background-color:#ea5413;
}

.step_o .step_info,.step_o .step_more span{
  background-color:#156bab;
}

.step_u .step_info,.step_u .step_more span{
  background-color:#eeab39;
}

.step_i .step_info,.step_i .step_more span{
  background-color:#8eb82e;
}

.step_info em{
  position:absolute;
  top:-60%;
  left:35%;
}

.step_info .step_title{
  color:#fff;
  position:absolute;
  width:100%;
  top:46%;
  text-align:center;
  font-size:17px;
  line-height:31px;
}

.step_mess{
  font-size:15px;
  color:#222;
  line-height:27px;
  height: 240rpx;
}

.step_more{
  height:36px;
  margin-top:16px;
  text-align:center;
}

.step_more span{
  border-radius:6px;
  color:#fff;
  font-size:14px;
}
</style>
