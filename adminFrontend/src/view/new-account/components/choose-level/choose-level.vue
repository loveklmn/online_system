<template>
<Row class="mainPanel">
  <Col span="18">
    <Card title="级别选择">
      <Row>
        <p class="description">你可以在这里选择一个级别，不同的级别......</p>
      </Row>
      <Row>
        <Select v-model="level" :lable-width="200" class="level-selector">
          <Option value="k1">k1</Option>
          <Option value="k2">k2</Option>
          <Option value="k3">k3</Option>
        </Select>
      </Row>
      <Row>
        <Button type="primary" @click="next" class="next-step-btn">下一步</Button>
        <Button type="warning" @click="reset" class="next-step-btn">返回首页</Button>
      </Row>
    </Card>
  </Col>
  <Col span="6">
    <Card class="quick-tip" title="温馨提示">
      <p>如果您想要为已有账号的用户申请更多的权限，建议您选择更改用户权限</p>
      <Button class="redirect-btn"> 去更改用户权限 </Button>
    </Card>
  </Col>
</Row>
</template>
<script>
export default {
  name: 'chooseLevel',
  props: [
    'accountsLevel'
  ],
  data () {
    return {
      order: 1,
      level: ''
    }
  },
  created: function () {
    this.level = this.accountsLevel
  },
  methods: {
    next () {
      this.$emit('on-select', this.level)
    },
    reset () {
      this.$router.push('/home')
    }
  }
}
</script>
