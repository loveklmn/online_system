<template>
<div>
  <Divider class="first-divider" orientation="left"><h1>发布新消息</h1></Divider>
  <div class="new-messsage">
    <Input class="new-input"
    v-model="newNotice"
    type="textarea"
    :rows="4"
    placeholder="输入你的消息..." />
    <Card class="new-card">
      <Button type="primary" class="send-btn" @click="handleSubmit">发布</Button>
    </Card>
  </div>
  <Divider class="second-divider" orientation="left"><h1>最近一周发布消息</h1></Divider>
  <div
    class="single-message"
    v-for="notice in noticeList"
    :key="notice.id">
    <Card :title="notice.created_time" class="message-card">
      <p class="notice-content">{{ notice.content }}</p>
    </Card>
  </div>
  <Divider dashed/>
</div>
</template>
<script>
import axios from '@/libs/api.request'
export default {
  name: 'sendNotice',
  data () {
    return {
      newNotice: '',
      noticeList: []
    }
  },
  created () {
    axios.request({
      url: 'notices',
      method: 'get'
    }).then(data => {
      data.sort(function (a, b) {
        let d1 = new Date(a.created_time)
        let d2 = new Date(b.created_time)
        return d1 < d2 ? 1 : -1
      })
      this.noticeList.push.apply(this.noticeList, data)
      this.noticeList = this.noticeList.map(notice => {
        let time = new Date(notice.created_time)
        let year = time.getFullYear()
        let month = time.getMonth()
        let date = time.getDate()
        notice.created_time = `${year}年${month + 1}月${date}日`
        return notice
      })
    }).catch(error => {
      console.log(error)
    })
  },
  methods: {
    handleSubmit () {
      console.log(this.newNotice)
      axios.request({
        data: {
          content: this.newNotice
        },
        url: 'notices/',
        method: 'post'
      }).then((data) => {
        this.$Message.success('上传成功')
      })
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
  margin-top: 3%;
  margin-left: 4.5%;
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
.send-tip {
  display: inline-block;
  margin-right: 1%;
}
Button:focus {
  background-color:olive;
}
</style>
