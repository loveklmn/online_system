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
        <Button type="primary" class="next-step-btn" @click="nextStep">下一步</Button>
      </div>
    </Card>
  </div>
</div>
</template>
<script>
import './format.less'
export default {
  name: 'firstStep',
  props: {
    accountLevel: {
      type: Number,
      default: 1
    },
    accountAmount: {
      type: Number,
      default: 1
    }
  },
  data () {
    return {
      level: this.accountLevel,
      amount: this.accountAmount
    }
  },
  methods: {
    nextStep () {
      if (!isNaN(this.level) && !isNaN(this.amount)) {
        this.$emit('firstDone', {'level': this.level, 'amount': this.amount})
      } else {
        this.$Message.error('请检查输入数据的正确性')
      }
    },
    reset () {
      this.$router.replace({
        path: '/home'
      })
    }
  }
}
</script>
