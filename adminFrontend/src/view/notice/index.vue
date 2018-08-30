<template>
<content-layout
  title="消息管理">
  <div slot="content">
    <Row :gutter="22" class="demo-tabs-style1 main-content" style="background: #e3e8ee;padding:16px;">
      <Tabs type="card" @on-click="handleClick">
        <TabPane label="发布新消息" >
          <send-notice v-if="pageOne"/>
        </TabPane>
        <TabPane label="历史消息管理">
          <notice-table v-if="pageTwo"/>
        </TabPane>
      </Tabs>
    </Row>
    <backhome-btn
      back="/home"
      name="回首页"></backhome-btn>
  </div>
</content-layout>
</template>
<script>
import sendNotice from './send-notice.vue'
import noticeTable from './notice-table.vue'
import contentLayout from '_c/content-layout'
import backhomeBtn from '_c/backhome-btn'
export default {
  data () {
    return {
      pageOne: true,
      pageTwo: true
    }
  },
  components: {
    sendNotice,
    noticeTable,
    contentLayout,
    backhomeBtn
  },
  methods: {
    handleClick (name) {
      if (name === 0) {
        this.pageOne = true
        this.pageTwo = false
      } else {
        this.pageOne = false
        this.pageTwo = true
      }
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
  margin-right: 0;
  margin-left: 0;
  background-color: #4693db;
}

.top-menu-divider {
  margin: 0;
  background-color: #b4babf;
}
.main-content {
  margin-left: 1%;
}

.demo-tabs-style1 > .ivu-tabs-card > .ivu-tabs-content {
        height: 120px;
        margin-top: -16px;
    }

    .demo-tabs-style1 > .ivu-tabs-card > .ivu-tabs-content > .ivu-tabs-tabpane {
        background: #fff;
        padding: 16px;
    }

    .demo-tabs-style1 > .ivu-tabs.ivu-tabs-card > .ivu-tabs-bar .ivu-tabs-tab {
        border-color: transparent;
    }

    .demo-tabs-style1 > .ivu-tabs-card > .ivu-tabs-bar .ivu-tabs-tab-active {
        border-color: #fff;
    }
</style>
