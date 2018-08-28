<template>
<content-layout
title="信息详情">
<div class="main-content" slot="content">
  <div class="second-part">
    <h1>学生作业批阅</h1>
    <Divider />
    <Card>
      <filter-table
        :data="allHomeworks"
        :columns="columns"
        :search="condition"
        :pageSize="6">
      </filter-table>
    </Card>
  </div>
  <div class="third-part">
    <Row :gutter="20" style="margin-top: 20px;">
        <i-col span="16">
          <h1>阅读进度统计</h1>
          <Divider />
          <Card shadow>
            <chart-bar class="bar" :value="barData" text="各书目阅读统计"/>
          </Card>
        </i-col>
    </Row>
    <Row :gutter="20" style="margin-top: 20px;">
        <i-col span="16">
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
</content-layout>
</template>
<script>
import { ChartBar } from '_c/charts'
import FilterTable from '_c/filter-table'
import axios from '@/libs/api.request'
import contentLayout from '_c/content-layout'
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
    contentLayout
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
  methods: {}
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
</style>
