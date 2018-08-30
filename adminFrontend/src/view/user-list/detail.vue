<template>
<content-layout
title="信息详情">
<div class="main-content" slot="content">
  <div class="second-part">
    <p class="title-font">学生作业批阅</p>
    <Divider />
    <Card>
      <!-- :data="allHomeworks" -->
      <filter-table
        @load="loadData"
        :data="selectedHomeworks"
        :columns="columns"
        :search="condition"
        :pageSize="6">
      </filter-table>
    </Card>
  </div>
  <div class="third-part">
    <Row :gutter="20" style="margin-top: 20px;">
        <i-col span="16">
          <p class="title-font">阅读进度统计</p>
          <Divider />
          <Card shadow>
            <chart-bar class="bar" :value="barData" text="各书目阅读统计"/>
          </Card>
        </i-col>
    </Row>
    <Row :gutter="20" style="margin-top: 20px;">
        <i-col span="16">
          <Card shadow>
            <tables
              :value="progressData"
              :columns="progressColumns"
              :pageSize="6">
            </tables>
          </Card>
        </i-col>
    </Row>
  </div>
  <backhome-btn
    back="/student/userlist"
    name="学生列表"/>
</div>
</content-layout>
</template>
<script>
import { ChartBar } from '_c/charts'
import FilterTable from '_c/filter-table'
import axios from '@/libs/api.request'
import contentLayout from '_c/content-layout'
import Tables from '_c/tables'
import backhomeBtn from '_c/backhome-btn'
const selectList = {
  0: {
    value: '',
    name: '全部'
  },
  1: {
    value: '是',
    name: '是'
  },
  2: {
    value: '否',
    name: '否'
  }
}
export default {
  data () {
    return {
      condition: {},
      student: {},
      wholeProgress: [],
      barData: {},
      columns: [
        {
          title: '序号',
          key: 'bookid',
          filter: {
            type: 'Input'
          }
        },
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
        }
      ],
      selectedHomeworks: [],
      allHomeworks: [],
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
      progressData: []
    }
  },
  components: {
    ChartBar,
    FilterTable,
    contentLayout,
    Tables,
    backhomeBtn
  },
  beforeRouteEnter (to, from, next) {
    axios.request({
      url: `progress/${to.params.id}/`,
      method: 'get',
      data: {
        id: to.params.id
      }
    }).then(data => {
      next(vm => {
        vm.wholeProgress = data
        for (let key in data) {
          let item = data[key]
          vm.allHomeworks.push({
            bookid: item.id,
            bookname: item.cover,
            submit: item.homework !== -1 ? '是' : '否'
          })
          vm.selectedHomeworks = vm.allHomeworks
          vm.progressData.push({
            bookid: item.id,
            bookname: item.cover,
            progress: item.pages_num === 0 ? 0 : (item.progress.current_page) / item.pages_num
          })
        }
        for (let key in vm.progressData) {
          vm.barData[vm.progressData[key].bookname] = vm.progressData[key].progress
        }
      })
    })
  },
  methods: {
    loadData () {
      this.selectedHomeworks = this.allHomeworks.filter(this.isSelected)
    },
    isSelected (homework) {
      if (this.condition.bookid && homework.bookid !== parseInt(this.condition.bookid)) {
        return false
      }
      if (this.condition.bookname && homework.bookname.indexOf(this.condition.bookname) === -1) {
        return false
      }
      if (this.condition.submit && homework.submit !== this.condition.submit) {
        return false
      }
      return true
    }
  }
}
</script>
<style scoped>
.main-content {
  margin-top: 2%;
  margin-left: 2%;
}

.first-part {
  width: 40%;
  margin-top: 2%;
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

.title-font {
  margin-top: 1%;
  margin-bottom: 2%;
  font-size: 15px;
  font-weight: bold;
  margin-left: 2.7%;
}

</style>
