<template>
<div class="main">
  <div class="step-row">
    <Steps :current="1" class="steps">
      <Step title="填写生成账号信息"></Step>
      <Step title="确认生成账号信息"></Step>
      <Step title="账号生成成功"></Step>
    </Steps>
  </div>
  <Divider />
  <div class="content-row">
    <Card title="确认信息" class="mainPanel">
      <div class="verify-info" title="请确认以下信息">
        <Card title="请确认生成信息">
          <p>级别：&nbsp;&nbsp;&nbsp;&nbsp; {{ level }}</p>
          <Divider />
          <p>数量：&nbsp;&nbsp;&nbsp;&nbsp; {{ amount }}</p>
          </Card>
      </div>
      <div>
        <Button type="primary" class="next-step-btn" @click="handleSubmit" :loading="loadingStatus">{{ loadingStatus ? '生成中...' :  '确定生成'}}</Button>
        <Button type="warning" class="next-step-btn" @click="returnLast">上一步</Button>
      </div>
        </Card>
      </div>
    </Card>
  </div>
</div>
</template>
<script>
import './format.less'
export default {
  name: 'secondStep',
  props: {
    accountLevel: {
      type: Number,
      default: 2
    },
    accountAmount: {
      type: Number,
      default: 2
    }
  },
  data () {
    return {
      level: this.accountLevel,
      amount: this.accountAmount,
      loadingStatus: false
    }
  },
  methods: {
    handleSubmit () {
      this.loadingStatus = true
      setTimeout(() => {
        this.loadingStatus = false
      }, 20000)
      this.$emit('secondDone', {'level': this.level, 'amount': this.amount})
    },
    returnLast () {
      this.$emit('secondBack', {'level': this.level, 'amount': this.amount})
    }
  }
}
</script>
