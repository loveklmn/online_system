
<template>
  <div>
    <i-cell-group>
      <i-panel title="您当前的等级为">
      <i-cell title="K1">
          <i-switch :value="switch1" @click="onChange1" slot="footer"></i-switch>
      </i-cell>
      <i-cell title="K2">
          <i-switch :value="switch2" @click="onChange2" slot="footer"></i-switch>
      </i-cell>
      <i-cell title="K3">
          <i-switch :value="switch3" @click="onChange3" slot="footer"></i-switch>
      </i-cell>
      <i-cell title="K4">
          <i-switch :value="switch4" @click="onChange4" slot="footer"></i-switch>
      </i-cell>
      </i-panel>
    </i-cell-group>
    <div class="page">
    <div class="intro">
      <div>
        <div class="intro">
            <div class="home_step w1600">
                <!--幼儿阶段课程-->
                <div class="home_s step_k">
                    <div class="step_info">
                        <img alt="3-6岁幼儿英语" src="https://www.vronedu.com/vronedu/images/yzyxart_k.png"></em>
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
                            <img alt="6-7岁幼小衔接英语" src="https://www.vronedu.com/vronedu/images/yzyxart_o.png"></em>
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
                               <img alt="7-13岁少儿英语" src="https://www.vronedu.com/vronedu/images/yzyxart_u.png"></em>
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
                                    <img alt="13-18岁青少年英语" src="https://www.vronedu.com/vronedu/images/yzyxart_i.png"></em>
                                    <div class="step_title">
                                        <h4 class="fsize24">
                                            11-18岁青少年英语</h4>
                                        <p>
                                            <span>提高综合能力，体验学习乐趣！</span></p>
                                    </div>
                                </div>
                                <div class="step_mess pt10"><span>弗恩英语青少年阶段课程设置更注重技能的学习。课程中除了会采用先进国际化的教材之外，弗恩英语老师还会结合公立学校教材知识的重难点进行知识讲授，让孩子在轻松愉快的学习氛围中全面提高英语综合能力，体验英语学习乐趣。</span></div><br>
                            </div>

                        </div>
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
export default {
  data () {
    return {
      level: 'K1',
      switch1: true,
      switch2: false,
      switch3: false,
      switch4: false,
      disable: [true, true, true, true]
    }
  },

  methods: {
    setZero () {
      this.switch1 = false
      this.switch2 = false
      this.switch3 = false
      this.switch4 = false
    },
    onChange1 (e) {
      if (!this.disable[0]) {
        this.setZero()
        this.switch1 = !this.switch1
      }
    },
    onChange2 (e) {
      if (!this.disable[1]) {
        this.setZero()
        this.switch2 = !this.switch2
      }
    },
    onChange3 (e) {
      if (!this.disable[2]) {
        this.setZero()
        this.switch3 = !this.switch3
      }
    },
    onChange4 (e) {
      if (!this.disable[3]) {
        this.setZero()
        this.switch4 = !this.switch4
      }
    }
  }
}
</script>
<style>
.page {
  padding-bottom: 200rpx;
}
img {
  width: 40%;
  height: 80%;
}

.intro{
  font-family: -apple-system-font,Helvetica Neue,Helvetica,sans-serif;
  padding-right: 40rpx
}

.home_step{ clear:both; margin-top:40rpx;}
.fsize24{ text-align: right; padding-right: 40rpx;}
.step_k{ margin-left: 44px}
.step_info{ border-radius:6px; height:122px; position:relative; width:280px;}
.step_k .step_info,.step_k .step_more span{ background-color:#ea5413;}
.step_o .step_info,.step_o .step_more span{ background-color:#156bab;}
.step_u .step_info,.step_u .step_more span{ background-color:#eeab39;}
.step_i .step_info,.step_i .step_more span{ background-color:#8eb82e; }
.step_info em{ position:absolute; top:-60%; left:35%;}
.step_info .step_title{ color:#fff; position:absolute; width:100%; top:46%; text-align:center; font-size:17px; line-height:31px;}
.step_mess{ font-size:15px; color:#222; line-height:27px; height:120px;}
.step_more{ height:36px; margin-top:16px; text-align:center;}
.step_more span{ border-radius:6px; padding:6px 12px; color:#fff; font-size:14px;}
</style>
