<template>
<div class="main">
  <div class="step-row">
    <Steps :current="current" class="steps">
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
  name: 'new-accounts',
  data () {
    return {
      level: '',
      amount: '',
      current: 1,
      loadingStatus: false,
      accountsList: [{
        accountNumber: '123455'
      }
      ]
    }
  },
  created () {
    this.level = this.$route.query.level
    this.amount = this.$route.query.amount
  },
  methods: {
    handleSubmit () {
      // generate accounts (level, amount)
      // accountsList.append(res)
      this.loadingStatus = true
      setTimeout(() => {
        this.current = 2
        this.loadingStatus = false
      }, 500000)
      this.$router.push({
        name: 'generate_result',
        query: {
          level: this.level,
          amount: this.amount,
          accountsList: this.accountsList
        }
      })
    },
    returnLast () {
      this.$router.push({
        name: 'fill_info'
        // save message
      })
    }
  }
}
</script>
