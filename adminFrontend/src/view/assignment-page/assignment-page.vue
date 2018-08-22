<template>
  <div class="main-layout">
    <div class="top-title">
      <Card class="top-title-card">
        <p>阅读拓展导入</p>
      </Card>
    </div>
    <div class="center-body">
      <div class="left-menu-card">
        <Button type="text" class="left-menu-btn" @click="currentStatus">当前状态</Button>
        <Button type="text" class="left-menu-btn" @click="importAgain">重新导入</Button>
        <Button type="text" class="left-menu-btn" @click="modifyMaterial">修改素材</Button>
        <Button type="text" class="left-menu-btn" @click="clearHistory">清除历史</Button>
      </div>
      <div class="right-content">
        <Card title="输入题目描述" class="right-content-card">
          <editor class="input-editor" v-model="assignment" @on-change="handleChange"/>
          <div class="operation-btns">
            <Button @click="handleCommit" class="op-btn">确认提交</Button>
            <Button @click="handleReset" class="op-btn">返回书架</Button>
          </div>
        </Card>
      </div>
    </div>
    <Modal
      v-model="reviewMode">
      <Card title="当前阅读拓展内容" class="assignmentReview">
        {{ assignment }}
      </Card>
    </Modal>
    <Modal
      v-model="resetMode"
      @on-ok="ok">
      <p>你确定放弃编辑退出吗？</p>
    </Modal>
    <Modal
      v-model="warningMode"
      @on-ok="confirmClear">
      <Card title="以下是当前阅读拓展内容" class="assignmentReview">
        {{ assignment }}
      </Card>
      <Divider> 你确定永久删除吗？</Divider>
    </Modal>
  </div>
</template>
<script>
import Editor from '_c/editor'
import './format.less'
export default {
  name: 'assignment_page',
  components: {
    Editor
  },
  data () {
    return {
      resetMode: false,
      reviewMode: false,
      warningMode: false,
      assignment: '',
      currentBook: null
    }
  },
  created () {
    this.currentBook = this.$route.query.book
  },
  methods: {
    handleChange (html, text) {
      this.assignment = html
    },
    sendContent () {
      // url: /vron/books/<bookid: int>/homework/
      // axios.post(url, {
      //   assignment: this.assignment
      // }).then()(function (response) {
      //   this.$Message.success('上传成功！')
      // }).catch(function (error) {
      //   this.$Message.error(error)
      // })
    },
    handleCommit () {
      this.sendContent()
      this.$router.push({
        name: 'assignment_success',
        query: this.currentBook
      })
    },
    handleReset () {
      this.resetMode = true
    },
    ok () {
      this.$router.push({
        name: 'book_detail_info'
      })
    },
    currentStatus () {
      this.reviewMode = true
    },
    modifyMaterial () {
      if (this.currentBook !== null) {
        this.assignment = this.currentBook.assignment
      } else {
        this.$Message.error('error')
      }
    },
    clearHistory () {
      if (this.currentBook == null) {
        this.$Message.warning('当前没有阅读拓展记录！')
      } else {
        this.warningMode = true
      }
    },
    confirmClear () {
      this.$Message.success('清除成功，本书当前没有阅读拓展记录')
    },
    importAgain () {
      this.$Message.success('在右侧区域编辑文本或者上传图片')
    }
  }
}
</script>

<style scoped>

</style>
