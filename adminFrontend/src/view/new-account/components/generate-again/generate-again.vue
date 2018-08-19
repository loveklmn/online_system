<template>
<Row class="mainPanel">
  <Col span="18">
    <Card title="生成结果">
      <Row>
        <p>生成成功！以下是本次生成账号信息！</p>
      </Row>
      <Row>
        <Table height="200" :columns="tableList" :data="accountsList"></Table>
      </Row>
      <Row>
        <Button type="primary" class="next-step-btn" @click="generateAgain">继续生成账号</Button>
        <Button type="warning" @click="reset" class="next-step-btn">返回首页</Button>
      </Row>
    </Card>
  </Col>
  <Col span="6">
    <Card class="quick-tip" title="温馨提示">
      <p>查看历史生成信息</p>
      <Button class="redirect-btn"> 查看历史生成信息 </Button>
    </Card>
  </Col>
</Row>
</template>
<script>
export default {
  name: 'generateAgain',
  props: [
    'level',
    'amount'
  ],
  data () {
    return {
      tableList: [
        {
          title: '账号',
          key: 'accountNumber'
        }
      ],
      accountsList: [
        {
          accountNumber: '123455'
        }
      ]
    }
  },
  created: function () {
    console.log('generate' + this.amount + 'accounts  for level: ' + this.level)
  },
  methods: {
    generateAgain () {
      this.$router.push('/manage_user_page')
    },
    reset () {
      this.$router.push('/home')
    }
  }
}
</script>
