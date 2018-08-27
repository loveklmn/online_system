<template>
<div>
  <Divider class="first-divider" orientation="left"><h1>发布新消息</h1></Divider>
  <div class="new-messsage">
    <Input class="new-input" v-model="newNotice" type="textarea" :rows="4" placeholder="输入你的消息..." />
    <Card class="new-card">
      <p class="send-tip">发布范围：</p>
      <Select v-model="sendLevel" class="send-level">
        <Option v-for="item in levelList" :value="item" :key="item">{{ item }}</Option>
      </Select>
      <Divider type="vertical"/>
      <Button type="primary" class="send-btn" @click="handleSubmit">发布</Button>
    </Card>
  </div>
  <Divider class="second-divider" orientation="left"><h1>最近一周发布消息</h1></Divider>
  <div
    class="single-message"
    v-for="notice in noticeList"
    :key="notice">
    <img class="avatar-btn"/>
    <Card :title="notice.created_time" class="message-card">
      <p class="notice-content">{{ notice.content }}</p>
    </Card>
  </div>
  <Divider dashed/>
</div>
</template>
<script>
export default {
  name: 'sendNotice',
  data () {
    return {
      sendLevel: 'k1',
      levelList: [
        'k1', 'k2', 'k3', 'k4'
      ],
      newNotice: '',
      noticeList: [
        {
          imgsrc: 'a',
          content: 'hello',
          created_time: '2018/18/18'
        },
        {
          imgsrc: 'b',
          content: 'nice',
          created_time: '2018/20/20'
        },
        {
          imgsrc: 'b',
          content: 'nice',
          created_time: '2018/20/20'
        },
        {
          imgsrc: 'b',
          content: 'nice',
          created_time: '2018/20/20'
        },
        {
          imgsrc: 'b',
          content: 'nice',
          created_time: '2018/20/20'
        },
        {
          imgsrc: 'b',
          content: 'nice',
          created_time: '2018/20/20'
        },
        {
          imgsrc: 'b',
          content: 'nice',
          created_time: '2018/20/20'
        }
      ]
    }
  },
  created () {
    // get notice list
    // get the avatar of the current manager
  },
  methods: {
    handleSubmit () {
      // sendNotice(sendLevel, notice)
    }
  }
}
</script>
<style scoped>
.avatar-btn {
  flex-grow: 1;
  margin-left: 5%;
  margin-right: 2%;
  max-width: 60px;
  max-height: 60px;
  width: auto;
  height: auto;
}
.message-card {
  flex-grow: 13;
  margin-right: 10%;
}
.single-message {
  display: flex;
  flex-direction: row;
  margin-top: 3%;
}
.notice-content {
  display: inline-block;
}
.detail-icon {
  margin-right: 5px;
}
.ivu-card-head {
  background-color: #f0f1f3
}
.new-message {
  margin-left: 5%;
  width: 65%;
  margin-bottom: 20px;
}
.new-input {
  width: 75%;
  margin-left: 5%;
  margin-left: 5%;
}
.new-card {
  width: 75%;
  margin-left: 5%;
  text-align: right;
}
.send-btn {
  width: 10%;
}
.first-divider {
  margin-bottom: 2%;
}
.second-divider {
  margin-top: 5%;
}
.send-level {
  display: inline-block;
  width: 10%;
  text-align-last: center;
}
.send-tip {
  display: inline-block;
  margin-right: 1%;
}
Button:focus {
  background-color:olive;
}
</style>
