<template>
<content-layout
  title="消息管理">
  <Card slot="content">
    <div class="top-menu">
      <Button class="top-menu-btn" @click="sendNewMessage">发布新消息</Button>
      <Button class="top-menu-btn" @click="queryHistory">历史消息管理</Button>
      <Divider class="top-menu-divider"/>
      <Divider />
      <send-notice v-if="pageOne" />
      <notice-table v-if="pageTwo" />
    </div>
  </Card>
</content-layout>
</template>
<script>
import sendNotice from './send-notice.vue'
import noticeTable from './notice-table.vue'
import contentLayout from '_c/content-layout'
export default {
  data () {
    return {
      pageOne: true,
      pageTwo: false
    }
  },
  components: {
    sendNotice,
    noticeTable,
    contentLayout
  },
  methods: {
    queryHistory () {
      this.pageOne = false
      this.pageTwo = true
    },
    sendNewMessage () {
      this.pageOne = true
      this.pageTwo = false
    }
  }
}
</script>
<style scoped>
.top-menu {
  margin-top: 2%;
}
.top-menu-btn {
  display: inline-block;
  width: 15%;
  height: 13%;
  background-color: #4693db;
  margin-left: 0px;
  margin-right: 0px;
}
.top-menu-divider {
  margin: 0px;
  background-color: #b4babf;
}
</style>
