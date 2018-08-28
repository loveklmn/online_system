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
import axios from '@/libs/api.request'
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
          title: '序号',
          key: 'id',
          filter: {
            type: 'Input'
          }
        },
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
                  this.handleDelete(params)
                }
              }
            }, '删除消息')
          }
        }
      ],
      noticeList: []
    }
  },
  components: {
    FilterTable
  },
  created () {
    axios.request({
      url: 'notices',
      method: 'get'
    }).then(data => {
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
      this.$Message.error(error)
    })
  },
  methods: {
    handleDelete (params) {
      axios.request({
        url: `notices/${params.row.id}/`,
        method: 'get'
      }).then(() => {
        this.$Message.suceed('删除成功！')
      }).catch(msg => {
        this.$Message.error('msg')
      })
    },
    loadData () {
      this.selectedNotice = this.allNotice.filter(this.isSelected)
    },
    isSelected (currentStudent) {
      if (this.condition.id && currentStudent.id !== parseInt(this.condition.id)) {
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
