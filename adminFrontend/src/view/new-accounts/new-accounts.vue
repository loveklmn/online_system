<template>
<div class="main">
  <div class="step-row">
    <Steps :current="0" class="steps">
      <Step title="填写生成账号信息"></Step>
      <Step title="确认生成账号信息"></Step>
      <Step title="账号生成成功"></Step>
    </Steps>
  </div>
  <Divider />
  <div class="content-row">
    <Card title="填写生成激活码相关信息" class="mainPanel">
      <div>
        <p class="description">请选择生成激活码所在级别:&nbsp;&nbsp;</p>
        <InputNumber :max="10" :min="1" v-model="level"></InputNumber>
      </div>
      <div>
        <p class="description">请输入您想要生成激活码的数量(不多于500个):&nbsp;&nbsp;&nbsp;</p>
        <InputNumber :max="500" :min="1" v-model="amount"></InputNumber>
      </div>
      <div>
        <Button type="primary" class="next-step-btn" @click="nextPage">下一步</Button>
        <Button type="warning" class="next-step-btn" @click="reset">返回首页</Button>
      </div>
    </Card>
  </div>
</div>
</template>
<script>
import './format.less'
export default {
  data () {
    return {
      level: 1,
      amount: 1
    }
  },
  created () {
    if (this.$route.query) {
      this.level = this.$route.query.level || this.level
      this.amount = this.$route.query.amount || this.amount
    }
  },
  methods: {
    nextPage () {
      if (this.level === null) {
        this.$Message.error('级别值不能是空')
      } else if (this.amount === null) {
        this.$Message.error('生成账号数量不能为空')
      } else {
        this.$router.push({
          name: 'generate',
          query: {
            level: this.level,
            amount: this.amount
          }
        })
      }
    },
    reset () {
      this.$router.push({
        path: '/home'
      })
    }
  }
}
</script>
