<template>
<Row class="mainPanel">
  <Col span="18">
    <Card title="填写生成账号数量">
      <Row>
        <p class="description">你可以一次生成多个账号用于线下分发，但是......</p>
      </Row>
      <Row>
        数量：
        <Input v-model.number="amount" placeholder="输入你想要生成的账户数量" class="amount-input"/>
      </Row>
      <Row>
        <Button type="primary" @click="next" class="next-step-btn">下一步</Button>
        <Button type="warning" @click="reset" class="next-step-btn">上一步</Button>
      </Row>
    </Card>
  </Col>
  <Col span="6">
    <Card class="quick-tip" title="温馨提示">
      <p>一些提示信息</p>
      <Button class="redirect-btn"> 跳转按钮 </Button>
    </Card>
  </Col>
</Row>
</template>
<script>
export default {
  name: 'inputAmount',
  props: [
    'accountsAmount'
  ],
  data () {
    return {
      order: 2,
      amount: 0
    }
  },
  created: function () {
    console.log('amount input')
    this.amount = this.accountsAmount
    console.log(this.amount)
  },
  methods: {
    next () {
      this.$emit('on-select', this.amount)
    },
    reset () {
      // return to the select progress
      this.amount = 0
      this.$emit('go-back')
    }
  }
}
</script>
