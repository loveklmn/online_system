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
  data () {
    return {
      level: '',
      amount: '',
      loadingStatus: false
    }
  },
  created () {
    this.level = this.$route.query.level
    this.amount = this.$route.query.amount
  },
  methods: {
    handleSubmit () {
      this.loadingStatus = true
      setTimeout(() => {
        this.loadingStatus = false
      }, 20000)
      this.$router.push({
        name: 'generate_result',
        query: {
          level: this.level,
          amount: this.amount
        }
      })
    },
    returnLast () {
      this.$router.replace({
        name: 'fill_generate_info',
        query: {
          level: this.level,
          amount: this.amount
        }
      })
    }
  }
}
</script>
