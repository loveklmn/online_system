<template>
<div class='main-content'>
  <div class='first-part'>
    <h1>活跃用户</h1>
    <Divider />
    <Card class='navCard'>
      <Row :gutter='20' class='first-row'>
        <i-col span='6' v-for='(infor, i) in inforCardData' :key='`infor-${i}`' class='quick-tip-card'>
          <infor-card shadow :color='infor.color' :icon='infor.icon' :icon-size='36' class="count-card">
            <count-to :end='infor.count' count-class='count-style'/>
            <p>{{ infor.title }}</p>
          </infor-card>
        </i-col>
      </Row>
    </Card>
  </div>
  <div class='third-part'>
    <Row :gutter='20' class="dataStatistic">
        <i-col span='8'>
          <h1>各级用户占比分析</h1>
          <Divider />
          <Card shadow>
            <chart-pie class='pie' :value='userPieData' text='各级用户数量'></chart-pie>
          </Card>
        </i-col>
        <i-col span='16'>
          <h1>各级书目数量统计</h1>
          <Divider />
          <Card shadow>
            <chart-bar class='bar' :value='level_book' text='各级书目数量'/>
          </Card>
        </i-col>
    </Row>
  </div>
</div>
</template>
<script>
import InforCard from '_c/info-card'
import CountTo from '_c/count-to'
import { ChartPie, ChartBar } from '_c/charts'
import axios from '@/libs/api.request'
export default {
  data () {
    return {
      all_user: 0,
      activity_user: {},
      level_user: {},
      level_book: {},
      inforCardData: [],
      userPieData: []
    }
  },
  components: {
    ChartPie,
    ChartBar,
    InforCard,
    CountTo
  },
  beforeRouteEnter (to, from, next) {
    axios.request({
      url: 'statistic/',
      method: 'get'
    }).then(data => {
      next(vm => {
        vm.initData(data)
      })
    }).catch(error => {
      console.log(error)
    })
  },
  methods: {
    initData (data) {
      this.all_user = data.all_user
      this.activity_user = data.activity_user
      for (let key in data.level_user) {
        this.level_user[key] = data.level_user[key]
        this.userPieData.push({
          name: 'k' + key,
          value: data.level_user[key]
        })
      }
      for (let key in data.level_book) {
        this.level_book[key] = data.level_book[key]
      }
      let inforData = [
        { title: '累计用户数', icon: 'md-person-add', count: this.all_user, color: '#2d8cf0' },
        { title: '用户日活动量', icon: 'md-locate', count: this.activity_user.day, color: '#19be6b' },
        { title: '用户周活动量', icon: 'md-person-add', count: this.activity_user.week, color: '#19be6b' },
        { title: '用户月活动量', icon: 'md-locate', count: this.activity_user.month, color: '#2d8cf0' }
      ]
      this.inforCardData = inforData
    }
  }
}
</script>
<style scoped>
.main-content {
  margin-top: 2%;
  margin-left: 2%;
}
.third-part {
  margin-top: 2%;
}
.e-title {
  margin: 2%;
}
.pie {
  height: 300px;
}
.bar {
  height: 300px;
  font-size: 23px;
}
.first-row {
  width: 100%;
}
.quick-tip-card {
  height: 120px;
}
.third-part {
  margin-top: 5%;
}
.dataStatistic {
  margin-top: 20px;
}
.count-card {
  font-size: 24px;
}
</style>
