<template>
<div class="main-content">
  <div class="first-part">
    <h1>学生基本信息</h1>
    <Divider />
    <Card>
      <h3 class="name-title">姓名:&nbsp;&nbsp;{{ student.username }}</h3>
      <h3 class="name-title">昵称：&nbsp;&nbsp;{{ student.nickname }}</h3>
      <h3 class="name-title">级别：&nbsp;&nbsp; {{ student.level }}</h3>
      <h3 class="name-title">分数：&nbsp;&nbsp;{{ student.score }}</h3>
    </Card>
  </div>
  <div class="second-part">
    <h1>学生作业批阅</h1>
    <Divider />
    <Card>
      <filter-table
        :data="homework"
        :columns="columns"
        :search="condition"
        :pageSize="6">
      </filter-table>
    </Card>
  </div>
  <div class="third-part">
    <Row :gutter="20" style="margin-top: 20px;">
        <i-col span="8">
        <h1>本周学习时长</h1>
        <Divider />
          <Card shadow>
            <chart-pie class="pie" :value="pieData" text="各模块学习时长"></chart-pie>
          </Card>
        </i-col>
        <i-col span="16">
          <h1>阅读进度统计</h1>
          <Divider />
          <Card shadow>
            <chart-bar class="bar" :value="barData" text="各书目阅读统计"/>
          </Card>
        </i-col>
    </Row>
    <Row :gutter="20" style="margin-top: 20px;">
        <i-col span="12">
          <Card shadow>
            <filter-table
              :data="timeData"
              :columns="timeColumns"
              :search="condition"
              :pageSize="6">
            </filter-table>
          </Card>
        </i-col>
        <i-col span="12">
          <Card shadow>
            <filter-table
              :data="progressData"
              :columns="progressColumns"
              :search="condition"
              :pageSize="6">
            </filter-table>
          </Card>
        </i-col>
    </Row>
  </div>
</div>
</template>
<script>
import { ChartPie, ChartBar } from '_c/charts'
import FilterTable from '_c/filter-table'
const selectList = {
  0: {
    value: '0',
    name: '全部'
  },
  1: {
    value: '1',
    name: '是'
  },
  2: {
    value: '2',
    name: '否'
  }
}
export default {
  data () {
    return {
      condition: {},
      student: {
        username: 'song',
        nickname: 'elsa',
        level: 'k1',
        score: 0
      },
      pieData: [
        {value: 335, name: '亲子阅读指导'},
        {value: 310, name: 'e-book'},
        {value: 234, name: '课后练习'},
        {value: 135, name: '社群打卡'},
        {value: 1548, name: '作业提交'}
      ],
      barData: {
        book1: 1,
        book2: 0.79,
        book3: 0.63,
        book4: 0.2,
        book5: 0.3,
        book6: 0.90,
        book7: 0.51
      },
      columns: [
        {
          title: '书名',
          key: 'bookname',
          filter: {
            type: 'Input'
          }
        },
        {
          title: '是否打卡',
          key: 'submit',
          filter: {
            type: 'Select',
            option: selectList
          }
        },
        {
          title: '批阅作业',
          key: 'handle',
          render: (h, params) => {
            return h('Button', {
              props: {
                type: 'primary',
                value: '查看作业'
              },
              style: {
                margin: '5%'
              },
              on: {
                click: () => {
                  this.turnToDetailPage(params)
                }
              }
            }, '批阅作业')
          }
        }
      ],
      homework: [
        {
          bookname: '哈哈哈',
          submit: '是'
        }
      ],
      timeColumns: [
        {
          title: '模块名',
          key: 'modulename',
          filter: {
            type: 'Input'
          }
        },
        {
          title: '本周学习时长',
          key: 'spendTime',
          filter: {
            type: 'Select',
            option: selectList
          }
        }
      ],
      timeData: [
        {
          modulename: '亲子阅读指导',
          spendTime: 2.3
        }
      ],
      progressColumns: [
        {
          title: '书名',
          key: 'bookname'
        },
        {
          title: '进度',
          key: 'progress'
        }
      ],
      progressData: [
        {
          bookname: '哈哈哈',
          progress: 0.8
        }
      ]
    }
  },
  components: {
    ChartPie,
    ChartBar,
    FilterTable
  }
}
</script>
<style scoped>
.main-content {
  margin-top: 2%;
  margin-left: 2%;
}
.first-part {
  margin-top: 2%;
  width: 40%;
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
</style>
