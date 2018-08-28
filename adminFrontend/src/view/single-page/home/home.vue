<template>
<div class='main-content'>
  <div class='first-part'>
    <h1>活跃用户</h1>
    <Divider />
    <Card class='navCard'>
      <Row :gutter='20' class='first-row'>
        <i-col span='6' v-for='(infor, i) in inforCardData' :key='`infor-${i}`' class='quick-tip-card'>
          <infor-card shadow :color='infor.color' :icon='infor.icon' :icon-size='36'>
            <count-to :end='infor.count' count-class='count-style'/>
            <p>{{ infor.title }}</p>
          </infor-card>
        </i-col>
      </Row>
    </Card>
  </div>
  <div class='second-part'>
    <!--用户总数统计-->
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
// import axios from '@/libs/api.request'
export default {
  data () {
    return {
      all_user: 8,
      activity_user: {
        day: 2,
        week: 4,
        month: 4
      },
      level_user: {
        '1': 7,
        '2': 1,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0
      },
      level_book: {
        '1': 4,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0
      },
      inforCardData: [
      ],
      userPieData: [
        {value: 3, name: 'k1'},
        {value: 5, name: 'k2'},
        {value: 7, name: 'k3'},
        {value: 9, name: 'k4'},
        {value: 10, name: 'k5'}
      ]
    }
  },
  mounted () {
    let inforData = [
      { title: '累计用户数', icon: 'md-person-add', count: this.all_user, color: '#2d8cf0' },
      { title: '用户日活动量', icon: 'md-locate', count: this.activity_user.day, color: '#19be6b' },
      { title: '用户周活动量', icon: 'md-person-add', count: this.activity_user.week, color: '#19be6b' },
      { title: '用户月活动量', icon: 'md-locate', count: this.activity_user.month, color: '#2d8cf0' }
    ]
    this.inforCardData = inforData
    // should be solved
    // for (let key in this.level_user) {
    //   this.userPieData.push({
    //     name: key,
    //     value: this.level_user(key)
    //   })
    // }
  },
  components: {
    ChartPie,
    ChartBar,
    InforCard,
    CountTo
  }
  // for save
  // beforeRouteEnter (to, from, next) {
  //   axios.request({
  //     url: 'statistic/',
  //     method: 'get'
  //   }).then(data => {
  //     console.log(data)
  //     next(vm => {
  //       vm.all_user = data.all_user
  //       vm.activity_user = data.activity_user
  //       for (let key in data.level_user) {
  //         vm.level_user.push({
  //           name: key,
  //           value: data.level_user(key)
  //         })
  //       }
  //       for (let key in data.level_book) {
  //         vm.level_book.push(data.level_book(key))
  //       }
  //     })
  //   }).catch(error => {
  //     console.log(error)
  //   })
  // }
}
</script>
<style scoped>
.main-content {
  margin-top: 2%;
  margin-left: 2%;
}
.second-part {
  margin-top: 2%;
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
</style>
