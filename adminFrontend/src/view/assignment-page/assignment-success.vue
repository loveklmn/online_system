<template>
  <div class="assignment-success">
    <Card title="上传结果">
      <div class="success-tip">
        <Icon type="md-checkmark-circle" color="green" size="10px"/>
        <p>生成成功!</p>
      </div>
      <div class="operator-btns">
        <Button type="primary" class="continue-btn" @click="generateAgain">继续导入</Button>
        <Button type="warning" class="back-btn" @click="reset">返回书架</Button>
      </div>
    </Card>
  </div>
</template>
<script>
import './format.less'
export default {
  name: 'assignment_success',
  methods: {
    generateAgain () {
      this.$router.push({
        name: 'import_assignment'
      })
    },
    reset () {
      this.$router.push({
        name: 'book_detail_info'
      })
    }
  }
}
</script>

<style scoped>

</style>
