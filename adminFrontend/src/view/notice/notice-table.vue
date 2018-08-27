<template>
<div class="main-content">
  <Divider class="first-divider" orientation="left"><h1>历史消息统计</h1></Divider>
  <Card>
    <filter-table
      @load="loadData"
      :data="noticeList"
      :columns="columns"
      :search="condition">
    </filter-table>
  </Card>
</div>
</template>
<script>
import FilterTable from '_c/filter-table'
const timeList = {
  0: {
    value: '0',
    name: '全部'
  },
  1: {
    value: '1',
    name: '今天'
  },
  2: {
    value: '2',
    name: '三天内'
  },
  3: {
    value: '3',
    name: '一周内'
  }
}
export default {
  name: 'noticeName',
  data () {
    return {
      condition: {},
      columns: [
        {
          title: '消息内容',
          key: 'content',
          filter: {
            type: 'Input'
          }
        },
        {
          title: '发布时间',
          key: 'created_time',
          filter: {
            type: 'Select',
            option: timeList
          }
        },
        {
          title: '删除',
          key: 'handle',
          render: (h, params) => {
            return h('Button', {
              props: {
                type: 'primary',
                value: '删除消息'
              },
              style: {
                margin: '5%'
              },
              on: {
                click: () => {
                  this.handleDelete()
                }
              }
            }, '删除消息')
          }
        }
      ],
      noticeList: [
        {
          content: '完了完了',
          created_time: '2018/18/18'
        }
      ]
    }
  },
  components: {
    FilterTable
  },
  created () {
    // get notice list
    // get the avatar of the current manager
  },
  methods: {
    handleDelete (params) {
      // 删除对应消息
    },
    loadData () {
      this.selectedNotice = this.allNotice.filter(this.isSelected)
    },
    isSelected (currentStudent) {
      if (this.condition.id && currentStudent.id !== parseInt(this.condition.id)) {
        return false
      }
      if (this.condition.level && currentStudent.level !== this.condition.level) {
        return false
      }
      if (this.condition.title && currentStudent.title.indexOf(this.condition.title) === -1) {
        return false
      }
      if (this.condition.type && currentStudent.type !== this.condition.type) {
        return false
      }
      return true
    }
  }
}
</script>
<style scoped>
.first-divider {
  margin-bottom: 2%;
}
</style>
