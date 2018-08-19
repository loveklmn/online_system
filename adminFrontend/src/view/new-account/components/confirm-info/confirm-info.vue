<template>
<Row class="mainPanel">
  <Col span="18">
    <Card title="生成结果">
      <Row>
        <p>请确认以下生成信息</p>
      </Row>
      <Row>
        级别：&nbsp; {{ level }} &nbsp;&nbsp;&nbsp;&nbsp;
        数量：&nbsp; {{ amount }}
      </Row>
      <Row>
        <Button type="primary" class="next-step-btn" @click="handleSubmit">确定</Button>
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
  name: 'confirmInfo',
  props: [
    'accountsLevel',
    'accountsAmount'
  ],
  data () {
    return {
      level: '',
      amount: 0
    }
  },
  created: function () {
    this.level = this.accountsLevel
    this.amount = this.accountsAmount
  },
  methods: {
    reset () {
      this.$emit('go-back')
    },
    handleSubmit () {
      this.$emit('on-select')
    }
  }
}
</script>
