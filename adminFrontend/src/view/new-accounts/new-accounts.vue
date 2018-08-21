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
    <Card title="填写生成激活码相关信息" class="mainPanel">
      <div>
        <p class="description">请选择生成激活码所在级别:&nbsp;&nbsp;</p>
        <Select v-model="level" :lable-width="200" class="level-selector">
          <Option value="k1">k1</Option>
          <Option value="k2">k2</Option>
          <Option value="k3">k3</Option>
        </Select>
      </div>
      <div>
        <p class="description">请输入您想要生成激活码的数量(不多于233个):&nbsp;&nbsp;&nbsp;</p>
        <Input v-model="amount" placeholder="输入你想要生成的账户数量" class="amount-input"/>
      </div>
      <div>
        <Button type="primary" @click="nextPage" class="next-step-btn">下一步</Button>
        <Button type="warning" @click="reset" class="next-step-btn">返回首页</Button>
      </div>
    </Card>
  </div>
</div>
</template>
<script>
import './format.less'
export default {
  name: 'fill-info',
  data () {
    return {
      level: 'k1',
      amount: 1,
      current: 0
    }
  },
  created () {
    if (this.$route.query) {
      this.level = this.$route.query.level
      this.amount = this.$route.query.amount
    }
  },
  methods: {
    nextPage () {
      this.$router.push({
        name: 'generate',
        query: {
          level: this.level,
          amount: this.amount
        }
      })
    },
    reset () {
      this.$router.push({
        path: '/home'
      })
    }
  }
}
</script>
