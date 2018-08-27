
<template>
  <div>
            <div>
                <div class="intro">
                    <div class="home_step w1600">
                        <!--幼儿阶段课程-->
                        <div class="home_s step_k">
                            <div class="step_info">
                                <img alt="3-6岁幼儿英语" src="https://www.vronedu.com/vronedu/images/yzyxart_k.png">
                                <div class="step_title">
                                    <h4 class="fsize24"> 3-6岁幼儿英语 </h4>
                                    <p><span>建立英语思维，开发语言能力！</span></p>
                                </div>
                            </div>
                            <div class="step_mess pt10"><span>适用于3-6岁孩子，在课程设置上重在培养孩子的学习兴趣和基本的语言、阅读、审美能力，并通过数百种专业教具、上千个课堂活动以及3000多个互动教学课件构建英语环境，帮助孩子养成良好的发音习惯和准确语调。</span></div>
                            <br>
                            <div class="step_more mt14">
                            </div>
                            <!--幼小衔接课程详情-->
                            <div class="home_s step_o">
                                <div class="step_info">
                                    <img alt="6-7岁幼小衔接英语" src="https://www.vronedu.com/vronedu/images/yzyxart_o.png">
                                    <div class="step_title">
                                        <h4 class="fsize24">
                                            6-7岁幼小衔接英语
                                        </h4>
                                        <p>
                                            <span>学习英语拼读，奠定语言基础！</span></p>
                                    </div>
                                </div>
                                <div class="step_mess pt10"><span>适用于步入小学阶段、英语零基础的孩子，帮助这一阶段的孩子奠定语言基础。老师会通过phonics教学法帮助学员熟悉精准的字母拼读等基本功，并通过逐渐的学习与反复练习，全面提高英文的听说读写能力。</span></div>
                                <br>
                                <div class="step_more mt14">
                                </div>
                                <!--少儿阶段课程-->
                                <div class="home_s step_u">
                                    <div class="step_info">
                                        <img alt="7-13岁少儿英语" src="https://www.vronedu.com/vronedu/images/yzyxart_u.png">
                                        <div class="step_title">
                                            <h4 class="fsize24">
                                                7-13岁少儿英语
                                            </h4>
                                            <p>
                                                <span>培养英语习惯，促成灵活运用！</span></p>
                                        </div>
                                    </div>
                                    <div class="step_mess pt10"><span>适用于7-13岁孩子，重在培养孩子英语运用能力。以浸入式学习环境结合主题情景式教学方式培养孩子的英语思维，并通过科学的“预讲演练”闭环式教学体系和个性化在线学习工具帮助孩子完成知识积累，实现灵活运用。</span></div>
                                    <br>
                                    <div class="step_more mt14">
                                    </div>
                                    <!--青少年阶段课程-->
                                    <div class="home_s step_i">
                                        <div class="step_info">
                                            <img alt="13-18岁青少年英语" src="https://www.vronedu.com/vronedu/images/yzyxart_i.png">
                                            <div class="step_title">
                                                <h4 class="fsize24">
                                                    11-18岁青少年英语</h4>
                                                <p>
                                                    <span>提高综合能力，体验学习乐趣！</span></p>
                                            </div>
                                        </div>
                                        <div class="step_mess pt10"><span>弗恩英语青少年阶段课程设置更注重技能的学习。课程中除了会采用先进国际化的教材之外，弗恩英语老师还会结合公立学校教材知识的重难点进行知识讲授，让孩子在轻松愉快的学习氛围中全面提高英语综合能力，体验英语学习乐趣。</span></div>
                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
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
  padding-top: 30rpx;
}

input {
  padding-left: 40rpx;
}

img {
  width: 50%;
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
  margin-left: 20px;
  margin-right: 20px;
}

.step_info{
  border-radius: 6px;
  height: 250rpx;
  position: relative;
  width: 670rpx;
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
  font-size:14px;
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
